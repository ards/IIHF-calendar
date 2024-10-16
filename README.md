# IIHF Calendar Scraper

This script scrapes the IIHF website (https://www.iihf.com/en/events/2024/wm/schedule) for game schedules and creates an .ical calendar file with all the games.

## Functionality

The script uses the BeautifulSoup library to parse the HTML of the IIHF website and extract the game details. It then creates a calendar event for each game and adds it to an iCalendar file.

You can customize the script to suit your needs:

- **Year**: The script is currently set to scrape the 2024 games. You can change the year by modifying the URL in the script.
- **Output Time Zone**: The script converts the game times to the 'Europe/Riga' timezone. You can change this to your preferred timezone by modifying the `localTimezone` variable.
- **Favorite Team**: You can set your favorite team by modifying the `favoriteTeam` variable. The script will then set a reminder 24 hours before each game that involves your favorite team, allowing you to plan in advance.

## Dependencies

This script requires the following Python libraries:

- beautifulsoup4
- pytz
- icalendar
- requests

You can install these dependencies using pip, the Python package installer. Open a terminal and type:

```bash
pip install -r requirements.txt
```

## How to Run

To run the script, open a terminal in the directory where the script is located and type:

```bash
python.exe IIHF_calendar_scraper.py
```

## License
  - GPL-3.0
