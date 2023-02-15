nomor_telepon = input("Masukkan nomor telepon Anda (12 digit): ")

if len(nomor_telepon) == 12:
    if nomor_telepon[0:4] == "0816":
        print("Operator yang Anda gunakan adalah Indosat")
    elif nomor_telepon[0:4] == "0814":
        print("Operator yang Anda gunakan adalah Telkomsel")
    else:
        print("Operator anda tidak diketahui")
   
    if nomor_telepon[11] == "0" or nomor_telepon[11] == "2" or nomor_telepon[11] == "4" or nomor_telepon[11] == "6" or nomor_telepon[11] == "8":
        print("Nomor telepon berakhiran genap")
    else:
        print("Nomor telepon berakhiran ganjil")
        