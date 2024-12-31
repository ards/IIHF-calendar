# IIHF Calendar Scraper

This script scrapes the IIHF website (https://www.iihf.com/en/events/2024/wm/schedule) for game schedules and creates an .ical calendar file with all the games.

## Functionality

The script uses the BeautifulSoup library to parse the HTML of the IIHF website and extract the game details. It then creates a calendar event for each game and adds it to an iCalendar file.

You can customize the script to suit your needs:

- **Year**: Specify year as parameter when executing script, if parameter is not provided will use current year.
- **Event Types**: The script supports multiple event types: wm (World Men), ww (Women's Worlds), wm20 (World Men U20), wm18 (World Men U18), and ww18 (World Women's U18). By default, it processes all event types. You can specify a single event type by passing it as a command-line argument.
- **Output Time Zone**: The script converts the game times to the 'Europe/Riga' timezone. You can change this to your preferred timezone by modifying the `localTimezone` variable.
- **Favorite Team**: You can set your favorite team by modifying the `favoriteTeam` variable. The script will then set a reminder 24 hours before each game that involves your favorite team, allowing you to plan in advance.

## Dependencies

This script requires the following Python libraries:

- beautifulsoup4
- requests
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

This will generate calendars for all event types for the current year.

To specify a different year:

```bash
python IIHF_calendar_scraper.py 2025
```

To specify a different year and event type:

```bash
python IIHF_calendar_scraper.py 2025 wm
```

## License
  - GPL-3.0
