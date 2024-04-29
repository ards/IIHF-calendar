from bs4 import BeautifulSoup
import requests
import pytz
from datetime import datetime, timedelta
from icalendar import Calendar, Event, Alarm

# Set your favorite team here (3-letter country code), so that you get reminder 1 day before the game.
# If you don't want reminders, set it to None.
# All other games will have reminders 1 hour and 15 minutes before the game.
# List of country codes: https://en.wikipedia.org/wiki/List_of_IOC_country_codes
favoriteTeam = 'LAT'
# Set the year of the IIHF World Championship, should also work for years in past.
year = '2024'

# Fetch and parse the schedule page
url = f"https://www.iihf.com/en/events/{year}/wm/schedule"
print(f"Fetching data from {url}...")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Create a new calendar
cal = Calendar()
cal.add('prodid', '-//IIHF 2024 Games Calendar//mxm.dk//')
cal.add('version', '2.0')

# Timezone settings
# Set your preferred timezone here
# List of timezones: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
localTimezone = pytz.timezone('Europe/Riga')

# Extract game details
game_cards = soup.find_all('div', class_='b-card-schedule')

for game in game_cards:
    team_a = game['data-hometeam']
    team_b = game['data-guestteam']
    game_date_utc = game['data-date-utc']
    game_time_utc = game['data-time-utc']

    datetime_utc = datetime.fromisoformat(f"{game_date_utc} {game_time_utc}")
    utc = pytz.timezone('UTC')
    datetime_utc = utc.localize(datetime_utc)

    local_datetime = datetime_utc.astimezone(localTimezone)

    # Create the calendar event
    event = Event()

    if favoriteTeam in [team_a, team_b]:
        event.add('summary', f"🌟Hockey: {team_a} vs {team_b}🌟")    
    else:
        event.add('summary', f"Hockey: {team_a} vs {team_b}")

    event.add('dtstart', local_datetime)
    event.add('dtend', local_datetime + timedelta(hours=2))  # Assuming each game lasts about 2 hours
    event.add('dtstamp', datetime.now())
    event['uid'] = game['data-game-id']

    # Set reminders for favorite games
    if favoriteTeam in [team_a, team_b]:
        # Reminder 1 day before
        alarm1 = Alarm()
        alarm1.add("trigger", timedelta(days=-1))
        alarm1.add("action", "DISPLAY")
        alarm1.add('description', "Reminder: Game starts in 24 hours")
        event.add_component(alarm1)

    alarm2 = Alarm()
    alarm2.add("trigger", timedelta(hours=-1))
    alarm2.add("action", "DISPLAY")
    alarm2.add('description', "Reminder: Game starts in 1 hour")
    event.add_component(alarm2)    

    alarm3 = Alarm()
    alarm3.add("trigger", timedelta(minutes=-15))
    alarm3.add("action", "DISPLAY")
    alarm3.add('description', "Reminder: Game starts in 15 minutes!")
    event.add_component(alarm3)   

    cal.add_component(event)

# Save the calendar to a file
if favoriteTeam:
    filename = f"IIHF_2024_Games_Calendar_{favoriteTeam}.ics"
else:
    filename = f"IIHF_2024_Games_Calendar.ics"

with open(filename, 'wb') as f:
    f.write(cal.to_ical())

print(f"Calendar file '{filename}' created successfully.")
