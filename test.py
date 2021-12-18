from selenium import webdriver
search_string = input("Input the URL or string you want to search for:")
search_string = search_string.replace(' ', '+')
driver = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
for i in range(1):
    matched_elements = browser.get("https://www.google.com/search?q=" +
                                     search_string + "&start=" + str(i))