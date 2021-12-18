import requests, webbrowser
from bs4 import BeautifulSoup

user_input = input("enter something to search: ")
print("googling.....")

google_search = requests.get("https://www.google.com/search?q="+user_input)
soup = BeautifulSoup(google_search.text, 'html.parser')
search_results = soup.select('.r a')

for link in search_results[:1]:
    actual_link = link.get('href')
    webbrowser.open('https://google.com/'+actual_link)