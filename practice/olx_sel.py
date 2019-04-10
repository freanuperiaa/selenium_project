from selenium import webdriver
from selenium.webdriver.common.by import By


titles, locations, price = [], [], []


def scrape(url):
    driver = webdriver.Chrome()
    driver.get(url)
    curr_titles = driver.find_elements(By.CSS_SELECTOR,
                                       'div.item div.link a span.title')
    curr_locations = driver.find_elements(By.CSS_SELECTOR,
                                          'div.item div.link span.location')
    curr_prices = driver.find_elements(By.CSS_SELECTOR,
                                       'div.item div.link span.price')
    for x in range(len(curr_prices)):
        titles.append(curr_titles[x].text)
        locations.append(curr_locations[x].text)
        price.append(curr_prices[x].text)

    try:
        next_page = driver.find_element(By.CSS_SELECTOR,
                                        'div.paging.text-center '
                                        'li.pagination-next a')
    except:
        next_page = None

    if next_page is not None:
        print(next_page.get_attribute('href'))
        scrape(next_page.get_attribute('href'))
    driver.quit()
    for x in range(len(titles)):
        print('Title:', titles[x], ', Location:', locations[x],
              ', Price:', price[x])


scrape('https://www.olx.ph/all-results?q=3ds')
