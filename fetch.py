import requests
import csv
from datetime import datetime

# Define URL and headers
url = "https://api.datawrapper.de/v3/charts/SeEnU/data"
headers = {'Authorization': 'Bearer 1LeiLX5fjdzFsAeAZhgzV1F04ispFRsj0KCAAOuIHwFS5s7xz85Hr4Z3wlBtLwTT'}


# Fetch data
response = requests.request("GET", url, headers=headers)
data = response.content.decode('utf-8')

# Write data
def latest_update():
    filename = "countrylist.csv"
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        reader = csv.reader(data.splitlines())
        for row in reader:
            writer.writerow(row)

def historical_update():
    filename = "countrylist_historical.csv"
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        lines = data.splitlines()
        reader = csv.reader(lines[1:])
        for row in reader:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current timestamp
            writer.writerow([timestamp] + row)  # Add the timestamp as the first column in each row


latest_update()
historical_update()