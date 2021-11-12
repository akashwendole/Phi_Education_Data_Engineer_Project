import tkinter as tk
from bs4 import BeautifulSoup
import requests
import csv

window = tk.Tk()
window.geometry("1200x700")

csv_file = open("google_scrape.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["title", "description", "link"])


def button_command():
    query_google = query.get()
    url = f"https://www.google.com/search?q={query_google}&ie=utf-8&oe=utf-8"
    site = requests.get(url).content
    doc = BeautifulSoup(site, "html.parser")
    f = doc.find("div", id="main")
    lists = []
    for i in range(1, len(f) - 1):
        try:
            g = f.find_all(class_="ZINbbc xpd O9g5cc uUPGi")[i]
            title = g.find(class_="BNeawe vvjwJb AP7Wnd").getText()
            description = g.find(class_="BNeawe s3v9rd AP7Wnd").getText()
            link = g.find('a')['href'][7:]
            lists.append((title, link, description))
            csv_writer.writerow([title, description, link])
        except:
            continue

    printing_tables(lists)

    csv_writer.writerow('')
    csv_writer.writerow('')
    csv_writer.writerow('')
    csv_writer.writerow(['People also ask for'])
    also_ask = f.find_all(class_="Lt3Tzc")
    i = 0
    for result in also_ask:
        csv_writer.writerow([result.getText()])
        frame = tk.Frame(relief='sunken', borderwidth=1)
        cell = tk.Label(master=frame, text=result.getText(), height=5, width=30, anchor="nw", wraplength=200)
        cell.pack(side=tk.LEFT)
        frame.grid(row=i + 2, column=4, padx=25)
        frame_title = tk.Frame(relief='sunken', borderwidth=1)
        title = tk.Label(master=frame_title, text="People also asked for", height=1, width=30, wraplength=200)
        title.pack(side=tk.LEFT)
        frame_title.grid(row=1, column=4, padx=25)
        i += 1

    # Related searches
    csv_writer.writerow('')
    csv_writer.writerow('')
    csv_writer.writerow('')
    csv_writer.writerow(['Related searches'])
    related_searches = f.find_all(class_="BNeawe s3v9rd AP7Wnd lRVwie")
    i = 0
    for related in related_searches:
        csv_writer.writerow([related.getText()])
        frame = tk.Frame(relief='sunken', borderwidth=1)
        cell = tk.Label(master=frame, text=related.getText(), height=5, width=30, anchor="nw", wraplength=200)
        cell.pack(side=tk.LEFT)
        frame.grid(row=i + 2, column=5)
        frame_title = tk.Frame(relief='sunken', borderwidth=1)
        title = tk.Label(master=frame_title, text="Related Searches", height=1, width=30, wraplength=200)
        title.pack(side=tk.LEFT)
        frame_title.grid(row=1, column=5)
        i += 1

    return None


def printing_tables(search_results):
    blank_frame = tk.Frame()
    blank_frame.grid(pady=50)
    titles = ['Title', 'Link', 'Description']
    for i in range(len(search_results)):
        for j in range(len(search_results[0])):
            frame = tk.Frame(relief='sunken', borderwidth=1)
            cells = tk.Label(master=frame, text=search_results[i][j], height=5, width=30, anchor="nw", wraplength=237)
            cells.pack(side=tk.LEFT)
            frame.grid(row=i + 2, column=j)
            frame_title = tk.Frame(relief='sunken', borderwidth=1)
            title = tk.Label(master=frame_title, text=titles[j], height=1, width=30, wraplength=200)
            title.pack(side=tk.LEFT)
            frame_title.grid(row=1, column=j)


input_frame = tk.Frame()
label = tk.Label(master=input_frame, text="Enter the query which you want to search for:", font=('arial', 14, 'bold'))
query = tk.Entry(master=input_frame, width=20)
label.pack(side=tk.LEFT)
query.pack(side=tk.LEFT)
input_frame.place(x=0, y=0)
button_frame = tk.Frame()
scrape = tk.Button(master=button_frame, text="Scrape", command=button_command, font=('arial', 14, 'bold'))
scrape.pack(side=tk.BOTTOM)
button_frame.place(x=170, y=30)

window.mainloop()
