import requests
import bs4 as bs

response = requests.get("https://mrkrishna.me/30DaysOfCode")

print(response.text)

soup = bs.BeautifulSoup(response.text, "html.parser")
print("Listening to: ", soup.title.text)

print(soup.title.text)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(response.close)
print("Connection closed")