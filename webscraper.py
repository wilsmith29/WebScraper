import requests
from bs4 import BeautifulSoup

url = "https://forecast.weather.gov/MapClick.php?lat=45.516018&lon=-122.681425"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("h2")
for title in titles:
    print(title.text.strip())