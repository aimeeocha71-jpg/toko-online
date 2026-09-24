def tambah_cart(cart, produk):
    cart.append(produk)
    return cart


cart = []

cart = tambah_cart(cart, {
    "nama": "Laptop",
    "harga": 7000000
})

cart = tambah_cart(cart, {
    "nama": "Mouse",
    "harga": 150000
})

print("=== KERANJANG ===")

for item in cart:
    print(f"{item['nama']} - Rp{item['harga']:,}")

total = sum(item["harga"] for item in cart)

print(f"Total: Rp{total:,}")