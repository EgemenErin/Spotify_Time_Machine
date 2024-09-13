# Billboard Top 100 to Spotify Playlist 🎵

Create a Spotify playlist of the Billboard Hot 100 songs from any date you choose.

![Spotify Playlist](https://your-image-link.com/playlist-screenshot.png)

*Note: Replace the image link above with a screenshot of your Spotify playlist once created.*

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

This project allows you to travel back in time and create a Spotify playlist of the top 100 songs from the Billboard Hot 100 chart on a specific date. Simply input the date you're interested in, and the script will:

- Scrape the Billboard Hot 100 chart for that date.
- Search for each song on Spotify.
- Create a new playlist in your Spotify account.
- Add all found songs to your new playlist.

## Features

- **Date Selection**: Input any date in the past to retrieve the Billboard Hot 100 chart.
- **Automated Playlist Creation**: Automatically generates a Spotify playlist with the top songs.
- **Error Handling**: Skips songs not found on Spotify and notifies the user.
- **Secure Authentication**: Uses OAuth 2.0 for secure access to your Spotify account.
- **Environment Variables**: Keeps sensitive information secure using a `.env` file.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.6 or higher installed on your machine.
- A [Spotify Developer Account](https://developer.spotify.com/dashboard/).
- Your Spotify app's `Client ID`, `Client Secret`, and `Redirect URI`.
- An active internet connection.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/billboard-spotify-playlist.git
cd billboard-spotify-playlist
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory:

```bash
touch .env
```

Add the following lines to the `.env` file, replacing the placeholders with your Spotify credentials:

```env
SPOTIPY_CLIENT_ID='your_spotify_client_id'
SPOTIPY_CLIENT_SECRET='your_spotify_client_secret'
SPOTIPY_REDIRECT_URI='http://localhost:8000/callback'
```

*Note:* Ensure that the `Redirect URI` matches exactly with what you've set in your Spotify Developer Dashboard.

### 5. Update Redirect URI in Spotify Dashboard

- Log in to your [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
- Navigate to your app and click on **"Edit Settings"**.
- In the **Redirect URIs** section, add `http://localhost:8000/callback`.
- Click **"Save"**.

## Usage

Run the script using the following command:

```bash
python main.py
```

When prompted, enter the date you wish to travel back to in the format `YYYY-MM-DD`:

```bash
Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 1995-06-15
```

### Authentication

A browser window will open prompting you to log in to your Spotify account and authorize the app. Once authenticated, the script will proceed to create your playlist.

### Enjoy Your Playlist!

After the script finishes running, you'll have a new playlist in your Spotify account named after the date you provided.

![Playlist Screenshot](https://your-image-link.com/playlist-screenshot.png)

*Note: Replace the image link above with an actual screenshot of your created playlist.*

## Project Structure

```
├── README.md
├── main.py
├── requirements.txt
├── .env
└── .gitignore
```

- `main.py`: The main script containing the logic for scraping and playlist creation.
- `requirements.txt`: A list of Python dependencies required for the project.
- `.env`: File containing environment variables (not to be shared publicly).
- `.gitignore`: Specifies intentionally untracked files to ignore.

## Technologies Used

- **Python 3**: The programming language used.
- **BeautifulSoup4**: For web scraping the Billboard website.
- **Requests**: To make HTTP requests to websites.
- **Spotipy**: A lightweight Python library for the Spotify Web API.
- **dotenv**: To manage environment variables securely.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- [Billboard](https://www.billboard.com/) for providing the music charts.
- [Spotify](https://www.spotify.com/) for the music streaming platform and API.
- [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/) for simplifying Spotify API calls.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for web scraping assistance.
- [Markdown Badges](https://github.com/Ileriayo/markdown-badges) for the cool badges.
