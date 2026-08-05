import os
from datetime import datetime
from urllib.parse import urlparse

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

DEFAULT_QUERY = "technology"
INTERESTS = [
    {"label": "AI", "query": "artificial intelligence"},
    {"label": "Startups", "query": "startups"},
    {"label": "Finance", "query": "finance"},
    {"label": "Health", "query": "healthcare"},
    {"label": "Sports", "query": "sports"},
    {"label": "Movies", "query": "cinema"},
    {"label": "Climate", "query": "climate"},
    {"label": "Gaming", "query": "gaming"},
]


def format_published_date(raw_value: str) -> str:
    if not raw_value:
        return "Fresh update"

    try:
        published_at = datetime.fromisoformat(raw_value.replace("Z", "+00:00"))
    except ValueError:
        return "Fresh update"

    return published_at.strftime("%d %b %Y")


def estimate_read_time(article: dict) -> str:
    words = " ".join(
        filter(
            None,
            [
                article.get("title", ""),
                article.get("description", ""),
                article.get("content", ""),
            ],
        )
    ).split()
    minutes = max(1, round(len(words) / 180))
    return f"{minutes} min read"


def normalize_article(article: dict) -> dict:
    source_name = article.get("source", {}).get("name") or "Global Desk"
    image_url = article.get("urlToImage") or ""
    article_url = article.get("url") or "#"

    return {
        "title": article.get("title") or "Untitled story",
        "description": article.get("description")
        or "Open the full report to read the complete story.",
        "source": source_name,
        "url": article_url,
        "image_url": image_url,
        "published_at": format_published_date(article.get("publishedAt", "")),
        "read_time": estimate_read_time(article),
        "domain": urlparse(article_url).netloc.replace("www.", "") or source_name,
    }


def fetch_news(query: str) -> tuple[list[dict], str | None]:
    # api_key = os.getenv("8b4272f38c7641e585d204eb543ef7c8")
    api_key="8b4272f38c7641e585d204eb543ef7c8"
    if not api_key:
        return [], "Set the NEWS_API_KEY environment variable to load live stories."

    try:
        response = requests.get(
            "https://newsapi.org/v2/everything",
            params={
                "q": query,
                "language": "en",
                "sortBy": "publishedAt",
                "pageSize": 18,
                "apiKey": api_key,
            },
            timeout=12,
        )
        response.raise_for_status()
        payload = response.json()
    except requests.RequestException:
        return [], "News service is unavailable right now. Please try again in a moment."

    if payload.get("status") != "ok":
        return [], payload.get("message", "Could not load stories at the moment.")

    articles = []
    for item in payload.get("articles", []):
        if not item.get("title") or not item.get("url"):
            continue
        articles.append(normalize_article(item))

    return articles, None


@app.route("/", methods=["GET"])
def home():
    selected_query = request.args.get("query", DEFAULT_QUERY).strip() or DEFAULT_QUERY
    articles, error_message = fetch_news(selected_query)
    featured_article = articles[0] if articles else None
    more_articles = articles[1:] if len(articles) > 1 else []

    return render_template(
        "index.html",
        interests=INTERESTS,
        selected_query=selected_query,
        featured_article=featured_article,
        articles=more_articles,
        article_count=len(articles),
        error_message=error_message,
    )


if __name__ == "__main__":
    app.run(debug=True)
