telurbakar = 7000
leleterbang = 10000
escoklatlempus = 5000
esdoger = 13000
print ("============MAKANAN=========")
print (" 1. Telur bakar          :" ,telurbakar)
print ("2. Lele Terbang Mas Bhe  :" ,leleterbang)
print ("3. Es Coklat Lempu       :", escoklatlempus)
print ("4. Es Doger Langensari   :", esdoger)
print ("======================PESANAN=====================")
jumlah_telur_bakar = int(input("Telur Bakar: "))
total_telur_bakar = telurbakar*jumlah_telur_bakar

jumlah_lele_terbang = int(input("Lele Terbang: "))
total_lele_terbang = leleterbang*jumlah_lele_terbang

jumlah_es_coklat = int(input("Es Coklat: "))
total_es_coklat = escoklatlempus*jumlah_es_coklat

jumlah_es_doger = int(input("Es Doger: "))
total_es_doger = esdoger*jumlah_es_doger

total_semua = (total_telur_bakar+total_lele_terbang+total_es_coklat+total_es_doger)

print("TOTAL TELUR BAKAR:", jumlah_telur_bakar)
print("TOTAL LELE TERBANG:", jumlah_lele_terbang)
print("TOTAL ES COKLAT :", jumlah_es_coklat)
print("TOTAL ES DOGER:", jumlah_es_doger)
print("Jumlah total biaya yang harus dibayar adalah Rp",total_semua)
