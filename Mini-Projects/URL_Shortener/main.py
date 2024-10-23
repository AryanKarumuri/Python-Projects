import pyshorteners
url = input("Enter the url: ")
shortener = pyshorteners.Shortener()
print(shortener.tinyurl.short(url))