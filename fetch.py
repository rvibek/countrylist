import requests
import csv
from datetime import datetime
import json
import os

auth_key = os.environ.get('AUTHKEY')

# Define URL and headers
url = "https://api.datawrapper.de/v3/charts/SeEnU/data"
headers = {'Authorization': f'Bearer {auth_key}'}


# Fetch data
response = requests.request("GET", url, headers=headers)
data = response.content.decode('utf-8')

# Generate data
def latest_update():
    # Write CSV
    filename = "countrylist.csv"
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        reader = csv.reader(data.splitlines())
        for row in reader:
            writer.writerow(row)
    # Write JSON
    filename = "countrylist.json"
    rows = data.splitlines()
    iso3 = rows[1].strip('"').split(', ')
    json_data = {'ISO3': iso3}
    with open(filename, "w") as file:
        json.dump(json_data, file)

def historical_update():
    filename = "countrylist_historical.csv"
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        lines = data.splitlines()
        reader = csv.reader(lines[1:])
        for row in reader:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current timestamp
            writer.writerow([timestamp] + row)  # Add the timestamp as the first column in each row


# latest_update()
# historical_update()
print(data)
