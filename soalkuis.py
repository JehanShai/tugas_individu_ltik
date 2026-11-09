# Dictionary menu makanan
menu = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Goreng": 18000,
    "Soto": 13000,
    "Bakso": 14000,
    "Es Teh": 5000,
    "Es Jeruk": 7000
}

total = 0

print("===== MENU MAKANAN =====")

# Menampilkan menu
for makanan, harga in menu.items():
    print(f"{makanan} = Rp{harga:,}")

print("=========================")
print("Masukkan jumlah makanan yang ingin dibeli")
print("Jika tidak membeli, masukkan 0")
print()

# Input jumlah setiap makanan
for makanan, harga in menu.items():
    jumlah = int(input(f"Beli {makanan} berapa: "))

    subtotal = harga * jumlah
    total += subtotal

print()
print("=========================")
print(f"Total harga yang harus dibayar: Rp{total:,}")
print("=========================")
