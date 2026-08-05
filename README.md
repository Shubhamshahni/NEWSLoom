
# NEWSLoom

`A beautifully designed Flask news app that turns user interests into a live, personalized reading experience.`

## Description

NEWSLoom is a modern Flask-based news website that helps people discover real-time stories based on what they care about most. It uses NewsAPI to fetch fresh headlines and presents them in a clean, magazine-inspired interface with search, quick interest filters, a featured story section, and responsive article cards.

## Features

- Interest-based news discovery
- Search for any topic or keyword
- Live article fetching with NewsAPI
- Featured story highlight section
- Responsive design for desktop and mobile
- Clean editorial-style interface
- Server-side API handling for safer key usage

## Screenshots

> Add the screenshots you shared to `assets/screenshots/` with the filenames below so GitHub can display them in this README.

### Hero Section
<img width="963" height="861" alt="Screenshot 2026-08-06 005738" src="https://github.com/user-attachments/assets/ed923bfa-3d0e-43a2-8c98-236febd60fc4" />



### Featured Story Section
<img width="1349" height="843" alt="Screenshot 2026-08-06 005834" src="https://github.com/user-attachments/assets/9f13f7fe-ae48-435e-b4c9-5f832226380c" />





### News Grid
<img width="990" height="903" alt="Screenshot 2026-08-06 005756" src="https://github.com/user-attachments/assets/39845bef-2dd0-4888-8b33-6c073fd51ebb" />



## Tech Stack

- Python
- Flask
- HTML
- CSS
- Requests
- NewsAPI

## Getting Started

1. Clone the repository:

bash
(https://github.com/Shubhamshahni/NEWSLoom.git)
cd NEWSLoom


2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Get a free API key from `https://newsapi.org/`.

4. Set your `NEWS_API_KEY` environment variable.

For Command Prompt:

```cmd
set NEWS_API_KEY=your_api_key_here
```

For PowerShell:

```powershell
$env:NEWS_API_KEY="your_api_key_here"
```

5. Run the app:

```bash
python main.py
```

6. Open your browser:

```bash
http://127.0.0.1:5000
```

## Project Structure

```text
NEWSLoom/
|-- main.py
|-- requirements.txt
|-- templates/
|   `-- index.html
|-- static/
|   `-- styles.css
`-- README.md
```

## Future Improvements

- User accounts and saved interests
- Bookmark favorite articles
- Category-based homepages
- Dark mode
- Deployment with a custom domain

## License

This project is open for learning, customization, and personal use.
