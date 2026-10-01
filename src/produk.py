def daftar_produk():
    produk = [
        {"nama": "Laptop", "harga": 7000000},
        {"nama": "Mouse", "harga": 150000},
        {"nama": "Keyboard", "harga": 300000},
        {"nama": "Headset", "harga": 250000}
    ]

    print("=== DAFTAR PRODUK ===")

    for i, item in enumerate(produk, 1):
        print(f"{i}. {item['nama']} - Rp{item['harga']:,}")


daftar_produk()