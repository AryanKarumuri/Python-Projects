from googlesearch import search
query = "Aryan Karumuri"

for i in search(query, start=0, pause=2):
    print(i)