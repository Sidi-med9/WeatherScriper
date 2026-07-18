# WeatherScriper

A Python weather scraping application that automatically collects weather forecasts from **world-weather.info** using Selenium, BeautifulSoup, and Undetected ChromeDriver.

The application extracts weather information for popular cities and exports the results in both **TXT** and **JSON** formats.

## Features

- Scrapes weather information automatically
- Bypasses Cloudflare using Undetected ChromeDriver
- Extracts:
  - City name
  - Temperature (°C)
  - Weather condition
- Saves data as:
  - output.txt
  - output.json
- Uses BeautifulSoup for HTML parsing
- Displays formatted tables using Tabulate

## Technologies

- Python 3.11
- Selenium
- BeautifulSoup4
- Undetected ChromeDriver
- Tabulate

## Project Structure

```
WeatherScriper/
│
├── main.py
├── output.json
├── output.txt
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Sidi-med9/WeatherScriper.git
```

Move to the project directory:

```bash
cd WeatherScriper
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Output

The program generates:

- output.txt
- output.json

Example JSON

```json
{
    "title": "Popular Cities Forecast",
    "date": "18/07/2026",
    "data": [
        {
            "city": "Paris",
            "temp": 28,
            "condition": "Sunny"
        }
    ]
}
```

## Notes

- Internet connection is required.
- Google Chrome must be installed.
- Chrome version should be compatible with Undetected ChromeDriver.

## Author

**Sidi Mohamed Mohamed Lemine**

GitHub:
https://github.com/Sidi-med9

