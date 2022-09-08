import pyshorteners

url = input("Enter the url: ")

s = pyshorteners.Shortener()

print(s.tinyurl.short(url))