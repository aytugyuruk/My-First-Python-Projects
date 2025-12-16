from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.a101.com.tr/kapida/meyve-sebze")

time.sleep(5)
a101_products = []

product_names = driver.find_elements(By.CSS_SELECTOR, "div.mobile\\:text-xs.tablet\\:text-xs.line-clamp-3.h-12.font-medium")
product_prices = driver.find_elements(By.CSS_SELECTOR, "div.text-md.absolute.bottom-0.font-medium.tablet\\:text-base")

for name, price in zip(product_names, product_prices):
    a101_products.append({"name": name.text, "price": price.text})

print("A101 Ürünleri:")
for product in a101_products:
    print(f"Ürün: {product['name']}, Fiyat: {product['price']}")

driver.quit()