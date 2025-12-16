from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
sok_products = []

for page in range(1, 3):
    url = f"https://www.sokmarket.com.tr/meyve-ve-sebze-c-20?page={page}"
    driver.get(url)
    
    
    time.sleep(5)

    product_names = driver.find_elements(By.CSS_SELECTOR, "h2.CProductCard-module_title__u8bMW")
    product_prices = driver.find_elements(By.CSS_SELECTOR, "span.CPriceBox-module_price__bYk-c")

    for name, price in zip(product_names, product_prices):
        sok_products.append({"name": name.text, "price": price.text})

print("Șok Ürünleri:")
for product in sok_products:
    print(f"Ürün: {product['name']}, Fiyat: {product['price']}")

driver.quit()