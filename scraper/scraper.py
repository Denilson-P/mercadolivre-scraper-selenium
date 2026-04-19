from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def get_optional_text(card, selector):
    try:
        return card.find_element(By.CSS_SELECTOR, selector).text
    except NoSuchElementException:
        return None


def get_products(driver):
    products = []

    cards = driver.find_elements(By.CSS_SELECTOR, ".poly-card")

    for card in cards:
        try:
            link_element = card.find_element(By.CSS_SELECTOR, "a.poly-component__title")

            title = link_element.text
            link = link_element.get_attribute("href")

            price_whole = card.find_element(By.CSS_SELECTOR, ".andes-money-amount__fraction").text
        except Exception as e:
            continue
        price = price_whole
            
        rating = get_optional_text(card, ".poly-reviews__rating")
        review_count = get_optional_text(card, ".poly-reviews__total")
        shipping = get_optional_text(card, ".poly-component__shipping")


            

        products.append({
            "title": title,
            "price": price,
            "rating": rating,
            "review_count": review_count,
            "shipping": shipping,
            "link": link

        })


    return products