from urllib.request import urlopen

page = urlopen("https://www.youtube.com/c/MrGamingFreak")
print(page.headers)
print(page.read())