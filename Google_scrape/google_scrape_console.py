from bs4 import BeautifulSoup
import requests
import re
import csv

csv_file = open("google_scrape.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["title", "description", "link"])

query = input("Enter the query")
url = f"https://www.google.com/search?q={query}&ie=utf-8&oe=utf-8"
print(url)
site = requests.get(url).content
doc = BeautifulSoup(site, "html.parser")
f = doc.find("div", id="main")
print("Search")
for i in range(1, len(f) - 1):
    try:
        g = f.find_all(class_="ZINbbc xpd O9g5cc uUPGi")[i]
        title = g.find(class_="BNeawe vvjwJb AP7Wnd").getText()
        description = g.find(class_="BNeawe s3v9rd AP7Wnd").getText()
        link = g.find('a')['href'][7:]
        print(f'\t{title}')
        print(f'\t\t{link}')
        print(f'\t\t{description}\n')
        csv_writer.writerow([title, description, link])
    except:
        continue

# People also ask for
csv_writer.writerow('')
csv_writer.writerow('')
csv_writer.writerow('')
csv_writer.writerow(['People also ask for'])
print("\nPeople also asked for:")
also_ask = f.find_all(class_="Lt3Tzc")
for query in also_ask:
    print('\t', query.getText())
    csv_writer.writerow([query.getText()])

# Related searches
csv_writer.writerow('')
csv_writer.writerow('')
csv_writer.writerow('')
csv_writer.writerow(['Related searches'])
print("\n\nRelated Searches")
related_searches = f.find_all(class_="BNeawe s3v9rd AP7Wnd lRVwie")
for related in related_searches:
    print('\t', related.getText())
    csv_writer.writerow([related.getText()])
