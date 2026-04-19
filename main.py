from pathlib import Path

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import random
import time

from scraper.scraper import get_products
from analysis.analysis import analyze_data, analyze_price_range, generate_report



BASE_URL = "https://lista.mercadolivre.com.br/notebook"
TOTAL_NOTEBOOKS = 50
OUTPUT_DIR = Path("data")
OUTPUT_FILE = OUTPUT_DIR / "df.csv"


def wait_cards(driver, timeout=15):
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.poly-component__title'))
    )


def go_to_next_page(driver, timeout=15):
    next_selectors = [
        "a[title='Seguinte']",
        "a[aria-label='Seguinte']",
        "li.andes-pagination__button.andes-pagination__button--next a",
        ".andes-pagination__button--next a",
    ]

    for selector in next_selectors:
        links = driver.find_elements(By.CSS_SELECTOR, selector)
        if links:
            next_link = links[0].get_attribute("href")
            if next_link:
                driver.get(next_link)
                wait_cards(driver, timeout=timeout)
                return True

    return False


def scrape():
    driver = webdriver.Chrome()

    try:
        driver.get(BASE_URL)
        wait_cards(driver)

        results = []
        seen_links = set()

        while len(results) < TOTAL_NOTEBOOKS:
            products = get_products(driver)

            for product in products:
                link = product.get("link")
                if link and link in seen_links:
                    continue

                if link:
                    seen_links.add(link)

                results.append(product)

                if len(results) >= TOTAL_NOTEBOOKS:
                    break

            if len(results) >= TOTAL_NOTEBOOKS:
                break

            if not go_to_next_page(driver):
                break

        tabela = pd.DataFrame(results[:TOTAL_NOTEBOOKS])
        OUTPUT_DIR.mkdir(exist_ok=True)
        tabela.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

        return tabela
    finally:
        driver.quit()


if __name__ == "__main__":
    try:
        tabela = scrape()

        df, df_sorted, cheapest, most_expensive, average_price, price_by_brand = analyze_data(tabela)

        price_range, _, _ = analyze_price_range(df, 800)

        generate_report(
            df,
            df_sorted,
            price_range,
            average_price,
            cheapest,
            most_expensive,
            price_by_brand,
)

        print(f"Coleta finalizada com {len(tabela)} notebooks.")
        print("Relatório gerado em: reports/relatorio_notebooks.xlsx")
    except TimeoutException:
        print("Nao foi possivel carregar os cards de produtos no tempo esperado.")
 
