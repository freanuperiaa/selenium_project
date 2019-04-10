from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://quotes.toscrape.com/')
quote = driver.find_elements(By.CSS_SELECTOR, 'div.quote span.text')
print(quote)
for x in range(len(quote)):
    print(quote[x].text)
names = driver.find_elements(By.CSS_SELECTOR, 'div.quote span small.author ')
for x in range(len(names)):
    print(names[x].text)