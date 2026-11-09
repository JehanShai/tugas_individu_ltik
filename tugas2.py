# Nama : Jehan Shaima
# Nim :2607795
# kelas :1c 

# a. Perhitungan Biaya Konsumsi
jumlah_peserta = int(input("Masukkan jumlah peserta: "))
jumlah_konsumsi = jumlah_peserta + (jumlah_peserta * 10 / 100)
total_biaya_konsumsi = jumlah_konsumsi * 35000
print("Jumlah konsumsi yang harus disediakan, termasuk cadangan : ", jumlah_konsumsi)
print("Total biaya konsumsi : ", total_biaya_konsumsi)

# b. Perhitungan Kebutuhan Cetak Sertifikat
jumlah_sertifikat = jumlah_peserta + (jumlah_peserta * 5 / 100)
jumlah_rim = jumlah_sertifikat / 500
total_biaya_kertas = jumlah_rim * 65000
print("Jumlah sertifikat yang perlu dicetak : ", jumlah_sertifikat)
print("Jumlah lembar kertas yang dibutuhkan : ", jumlah_sertifikat)
print("Perkiraan jumlah rim kertas yang diperlukan : ", jumlah_rim)
print("Total biaya pembelian kertas : ", total_biaya_kertas)

# c. Perhitungan Biaya Pendaftaran Peserta
biaya_sewa = int(input("Masukkan biaya sewa tempat: Rp "))
biaya_dokumentasi = int(input("Masukkan biaya dokumentasi: Rp "))
total_biaya = total_biaya_konsumsi + total_biaya_kertas + biaya_sewa + biaya_dokumentasi
dana_cadangan = total_biaya * 10 / 100
total_dana = total_biaya + dana_cadangan
biaya_pendaftaran = total_dana / jumlah_peserta

print("Total biaya pendaftaran : ", total_biaya)
print("Dana cadangan : ", dana_cadangan)
print("Total dana : ", total_dana)
print("Biaya pendaftaran per peserta : ", biaya_pendaftaran)