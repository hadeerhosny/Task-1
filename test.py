from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.google.com/search?q=")
browser.find_element_by_css_selector(".gLFyf gsfi").send_keys("Z2data")
browser.find_element_by_css_selector(".QCzoEc z1asCe MZy1Rb").click()
browser.implicitly_wait(5)
browser.find_element_by_css_selector(".LC20lb MBeuO DKV0Md").click()
