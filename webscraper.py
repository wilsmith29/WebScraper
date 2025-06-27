import requests
from bs4 import BeautifulSoup

url = "https://forecast.weather.gov/MapClick.php?lat=45.516018&lon=-122.681425"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

forecast = soup.find(id="seven-day-forecast")
items = forecast.find_all(class_="tombstone-container")

for item in items:
    period = item.find(class_="period-name").text
    short_desc = item.find(class_="short-desc").text
    temp = item.find(class_="temp").text
    print(f"{period}: {short_desc}, {temp}")