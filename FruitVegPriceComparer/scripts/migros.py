from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
migros_products = []

for page in range(1, 7):
    url = f"https://www.migros.com.tr/meyve-sebze-c-2?sayfa={page}"
    driver.get(url)
    
    time.sleep(5)

    product_names = driver.find_elements(By.CSS_SELECTOR, ".product-name")
    try:
        product_prices = driver.find_elements(By.CSS_SELECTOR, ".price.subtitle-1.ng-star-inserted")
    except:
        try:
            product_prices = driver.find_elements(By.CSS_SELECTOR, ".price-content")
        except:
            product_prices = driver.find_elements(By.CSS_SELECTOR, ".sale-price")

    for name, price in zip(product_names, product_prices):
        migros_products.append({"name": name.text, "price": price.text})

print("Migros Ürünleri:")
for product in migros_products:
    print(f"Ürün: {product['name']}, Fiyat: {product['price']}")

driver.quit()