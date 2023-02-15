jenismember1= 'Daily'
jenismember2 = 'Weekly'
jenismember3 = 'Monthly'
jenismember4 = 'Yearly'
pilihan1 ='menambah_data'
pilihan2= 'menampilkan_data'
pilihan3 = 'keluar'
def tempatgym ():
    print ("!! Selamat datang di H+ GYM !!")
    menu = int(input("Silahkan pilih menu dibawah ini:"))
    print ("1. Menambah data")
    print ("2. Menampilkan data")
    print ("3. Keluar")
    if pilihan1:
        pilihan = int(input("Silahkan masukkan pilihan yang anda inginkan: "))
        namapelanggan = input("Masukkan nama pelanggan:")
        member = input("Masukkan jenis member: ")
        print ("Data sudah berhasil ditambahkan")
    elif pilihan2:
        print ("Pelanggan",namapelanggan,  "Member",member)
    elif pilihan3:
        print ("Sistem berhenti...")
tempatgym()



