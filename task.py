from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
search_string = input("Input the URL or string you want to search for: (Z2data)")
search_string = search_string.replace(' ', '+')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
query = 'comprehensive guide to web scraping in python'
links = []
n_pages = 4
for page in range(3, n_pages):
    url = "http://www.google.com/search?q=" + query + "&start=" +str((page - 1) * 10)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')


search = soup.find_all('div', class_="B6fmyf")
for h in search:
    links.append(h.a.get('href'))