def checkout(cart):
    print("=== CHECKOUT ===")

    total = 0

    for item in cart:
        print(f"{item['nama']} - Rp{item['harga']:,}")
        total += item["harga"]

    print(f"Total pembayaran: Rp{total:,}")
    print("Checkout berhasil!")


cart = [
    {
        "nama": "Laptop",
        "harga": 7000000
    },
    {
        "nama": "Mouse",
        "harga": 150000
    }
]

checkout(cart)