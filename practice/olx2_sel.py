from selenium import webdriver
from selenium.webdriver.common.by import By


titles, locations, price = [], [], []


def scrape(driver):
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


def main():
    driver = webdriver.Chrome()
    driver.get('https://www.olx.ph/all-results?q=3ds')
    scrape(driver)
    while True:
        try:
            next_button = driver.find_element(By.CSS_SELECTOR,
                                              'div.paging.text-center '
                                              'ul.pagination.text-center li.'
                                              'pagination-next a')
        except:
            next_button = None
        if next_button is not None:
            #next_button.click()
            driver.execute_script("arguments[0].click();", next_button)
            scrape(driver)
        else:
            driver.quit()
            break
    for x in range(len(titles)):
        print('Title:', titles[x], ', Location:', locations[x],
              ', Price:', price[x])


if __name__ == '__main__':
    main()
