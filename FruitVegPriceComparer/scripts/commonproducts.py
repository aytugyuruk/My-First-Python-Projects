from thefuzz import fuzz
from migros import migros_products
from a101 import a101_products
from sok import sok_products

common_products = []
partial_common_products = []

SIMILARITY_THRESHOLD = 100  

def find_similar_product(product_name, product_list):
    for product in product_list:
        similarity = fuzz.ratio(product_name.lower(), product['name'].lower())
        if similarity >= SIMILARITY_THRESHOLD:
            return product
    return None

for migros_product in migros_products:
    sok_match = find_similar_product(migros_product['name'], sok_products)
    a101_match = find_similar_product(migros_product['name'], a101_products)

    if sok_match and a101_match:
        common_product = {
            "name": migros_product['name'],
            "migros_price": migros_product['price'],
            "a101_price": a101_match['price'],
            "sok_price": sok_match['price']
        }
        common_products.append(common_product)
    elif sok_match and not a101_match:
        partial_common_products.append({
            "name": migros_product['name'],
            "migros_price": migros_product['price'],
            "sok_price": sok_match['price'],
            "a101_price": None
        })
    elif a101_match and not sok_match:
        partial_common_products.append({
            "name": migros_product['name'],
            "migros_price": migros_product['price'],
            "a101_price": a101_match['price'],
            "sok_price": None
        })

for sok_product in sok_products:
    a101_match = find_similar_product(sok_product['name'], a101_products)
    migros_match = find_similar_product(sok_product['name'], migros_products)

    if a101_match and not migros_match:
        partial_common_products.append({
            "name": sok_product['name'],
            "sok_price": sok_product['price'],
            "a101_price": a101_match['price'],
            "migros_price": None
        })

print("Ortak Ürünler:")
for product in common_products:
    print(f"Ürün: {product['name']}, Migros Fiyat: {product['migros_price']}, A101 Fiyat: {product['a101_price']}, ŞOK Fiyat: {product['sok_price']}")

print("\nİki Markette Ortak Olan Ürünler:")
for product in partial_common_products:
    print(f"Ürün: {product['name']}, Migros Fiyat: {product.get('migros_price', 'Yok')}, A101 Fiyat: {product.get('a101_price', 'Yok')}, ŞOK Fiyat: {product.get('sok_price', 'Yok')}")
