import tkinter as tk
from tkinter import messagebox
from commonproducts import common_products, partial_common_products  # Ortak ürünler ve kısmi ürünleri içe aktar

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Market Fiyat Karşılaştırma")
root.geometry("400x400")

# Hem common_products hem de partial_common_products'tan ürünleri birleştir
urunler = [product["name"] for product in common_products] + [product["name"] for product in partial_common_products]

# Ürün seçim için dropdown menü
urun_secenekleri = tk.StringVar()
urun_secenekleri.set("Ürün Seçin")  # Varsayılan metin
urun_dropdown = tk.OptionMenu(root, urun_secenekleri, *urunler)
urun_dropdown.pack(pady=20)

# Seçilen ürünün fiyatlarını gösterme fonksiyonu
def fiyatlari_karsilastir():
    secilen_urun = urun_secenekleri.get()
    
    if secilen_urun and secilen_urun != "Ürün Seçin":
        # common_products ve partial_common_products içinde arama yap
        for product in common_products + partial_common_products:
            if product["name"] == secilen_urun:
                fiyat_bilgisi = (
                    f"{secilen_urun} Fiyatları:\n\n"
                    f"🛒 Migros: {product.get('migros_price', 'Veri bulunamadı')} \n"
                    f"🛒 A101: {product.get('a101_price', 'Veri bulunamadı')} TL\n"
                    f"🛒 ŞOK: {product.get('sok_price', 'Veri bulunamadı')}"
                )
                messagebox.showinfo("Fiyat Karşılaştırma", fiyat_bilgisi)
                return
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir ürün seçin.")

# Fiyatları karşılaştırmak için buton
fiyat_karsilastir_button = tk.Button(root, text="Fiyatları Karşılaştır", command=fiyatlari_karsilastir)
fiyat_karsilastir_button.pack(pady=20)

# Arayüzü başlat
root.mainloop()