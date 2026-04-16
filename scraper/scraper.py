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
            title = card.find_element(
                By.CSS_SELECTOR, ".poly-component__title"
            ).text

            price_whole = card.find_element(
                By.CSS_SELECTOR, ".andes-money-amount__fraction"
                ).text
                
            cents = card.find_element(
                    By.CSS_SELECTOR, ".andes-money-amount__cents"
                ).text
            price = f"{price_whole},{cents}"
            
            rating = get_optional_text(card, ".ui-pdp-review__rating")
            review_count = get_optional_text(
                card, ".ui-review-capability__rating__label"
            )
            shipping = get_optional_text(card, ".poly-component__shipping")


            link = card.find_element(By.PARTIAL_LINK_TEXT, "a-link-normal").get_attribute("href")

            products.append({
                "title": title,
                "price_whole": price_whole,
                "rating": rating,
                "review_count": review_count,
                "shipping": shipping,
                "link": link

            })


    return products
