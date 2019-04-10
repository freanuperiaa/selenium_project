from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('http://google.com')
print(driver.title)
inputElement = driver.find_element_by_name('q')
inputElement.send_keys('Cheese!')
inputElement.submit()
try:
    WebDriverWait(driver, 10).until(EC.title_contains("Cheese!"))
    print(driver.title)
finally:
    driver.quit()