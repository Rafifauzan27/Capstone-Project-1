### CAPSTONE PROJECT MODUL 1
### DATA NILAI SISWA

from tabulate import tabulate


#  Database Data Siswa
DataSiswa = [
    {"NIM" : 18050522,"Nama" : "Pras", "Mata Kuliah" : "Hukum Aviasi", "Nilai Tugas" : 80, "Nilai UTS" : 60, "Nilai UAS" : 75},
    {"NIM" : 18050578, "Nama" : "Rafi", "Mata Kuliah" : "Dangerous Goods", "Nilai Tugas" : 83, "Nilai UTS" : 70, "Nilai UAS" : 90},
    {"NIM" : 17052312, "Nama" : "Ardian", "Mata Kuliah" : "Ground Operations", "Nilai Tugas" : 85, "Nilai UTS" : 90, "Nilai UAS" : 89}
]
# Memanggil Data
def ShowDataSiswa () :
    # Mendefinisikan header tabel
    header = ["NIM", "Nama", "Mata Kuliah", "Nilai Tugas", "Nilai UTS", "Nilai UAS"]
    row = [[i[key] for key in header] for i in DataSiswa]
    table = tabulate(row, headers=header, tablefmt="grid")
    print(table)

#  Fungsi Mencari NIM pada Menu 1.2
def CariNIM():
    CNIM = input("Masukkan NIM Siswa Yang Ingin Dicari: ")
    if not CNIM.isdigit():
        print("Maaf, NIM Yang Dimasukkan Harus Berupa Angka")
    elif len(CNIM) != 8:
        print("Maaf, NIM harus ada 8 angka")
    else:
        CNIM = int(CNIM)
        for i in DataSiswa:
            if i["NIM"] == CNIM :
                print(f"Data Pencarian Dengan NIM : {CNIM} Telah Ditemukan")
                ShowDataSiswa()
                break
            else :
                print("Maaf, NIM Yang Dimasukkan Tidak Dapat Ditemukan")

#  Fungsi Menambah Data Siswa
def AddDataSiswa () :
   ANIM = int(input("Masukkan NIM Baru: "))
   for angka in DataSiswa :
    if angka["NIM"] == ANIM :
        print(f"Maaf, {ANIM} sudah ada. Harap masukkan NIM yang baru.")
        break

    ANama = input("Masukkan Nama Siswa Baru: ").title()
    AMT = input("Masukkan Mata Kuliah: ").title()
    ANT = int(input("Masukkan Nilai Tugas: "))
    ANUTS = int(input("Masukkan Nilai UTS: "))
    ANUAS = int(input("Masukkan Nilai UAS: "))

    SiswaBaru = {
        "NIM": ANIM,
        "Nama": ANama,
        "MT": AMT,
        "NT": ANT,
        "NUTS": ANUTS,
        "NUAS": ANUAS
    }
    confirm = input("Apakah Data Baru Sudah Benar Dan Ingin Ditambahkan (ya/tidak)? : ").lower()

    if confirm == "ya":
        DataSiswa.append(SiswaBaru)
        print("Data Siswa Baru Sudah Ditambahkan")
        DataSiswa()
        
    elif confirm == "tidak":
        print("Data Batal Untuk Ditambahkan")

        
# Fungsi Menghapus Data Siswa
def DeleteDataSiswa () :
    for i in range(len(DataSiswa)) :
        HNIM = int(input("Masukkan NIM Yang Ingin Di Hapus : "))
        if DataSiswa[i]["NIM"] == HNIM:
            
            confirm = input("Apakah NIM Tersbut Sudah Benar Dan Ingin Dihapuskan (ya/tidak)? : ").lower()

            if confirm == "ya" :
                DataSiswa.pop(i)
                print("Data telah dihapus")
                ShowDataSiswa()
                break
            elif confirm == "tidak" :
                print("NIM Batal Untuk Dihapus")


# Fungsi Update
# def UpdateDataSiswa() :
#     NIMSiswa = int(input("Masukkan NIM Siswa: "))
#     for i in range(len(DataSiswa)):
#         if NIMSiswa == DataSiswa[i]["NIM"]:
#             while True:
#                 updateisi = input("Kolom Apa Yang Ingin Anda Ubah (NIM, Nama, Mata Kuliah, Nilai Tugas, Nilai UTS, Nilai UAS): ").title()
#                 if updateisi in DataSiswa[i]:
#                     rubahisi = input(f"Masukkan {updateisi} baru: ")
#                     DataSiswa[i][updateisi] = rubahisi
#                     print("Data Sudah Diperbaharui")
#                     DataSiswa(UpdateDataSiswa)
#                     break
#                 else:
#                     print("Kolom yang dimasukkan tidak valid. Silakan coba lagi.")


# UpdateDataSiswa()
def UpdateDataSiswa():
    nim = int(input("Masukkan NIM Siswa yang ingin diupdate: "))
    data = next((item for item in DataSiswa if item["NIM"] == nim), None)

    if data is None:
        print("Data tidak ditemukan.")
        return

    update = {}
    for key in data.keys():
        if key == "NIM":
            continue
        update[key] = input(f"Masukkan {key}: ")

    DataSiswa.remove(data)
    DataSiswa.append({**data, **update})
    print("Data berhasil diupdate.")

    ShowDataSiswa(UpdateDataSiswa)

                    
#Menampilkan Menu
def MenuUtama():
            print('''
                =====================================================
                \t Data Mahasiswa Universitas Jatiasih
                =====================================================
                ''')
            print('''List Menu :
                1. Menampilkan Data Siswa
                2. Menambah Data Siswa
                3. Menghapus Data Siswa
                4. Update Data Siswa
                5. Keluar Program  
            ''')
            
            menu = int(input("Masukkan Angka Menu Yang Ingin Dijalankan (1-5): "))
            while True :
                if menu == 1 :
                    while True :
                        print('''
                =====================================================
                \t Menu Data Mahasiswa Universitas Jatiasih
                =====================================================
                ''')
                        print('''List Menu :
                1. Menampilkan Data Siswa
                2. Mencari Dengan NIM Siswa
                3. Kembali Ke Menu Utama
                    ''')
                        menu = int(input("Masukkan Angka Menu Yang Ingin Dijalankan (1-3): "))

                        while True :
                            if menu == 1 :
                                ShowDataSiswa()
                                break
                            elif menu == 2 :
                                CariNIM()
                                break
                            elif menu == 3 :
                                MenuUtama()
                                
                            else :
                                print("Maaf Hanya Bisa Di Input Angka 1-3")

                elif menu == 2 :
                    AddDataSiswa()
                    break

                elif menu == 3 :
                    DeleteDataSiswa()
                    break

                elif menu == 4 :
                    UpdateDataSiswa()
                    break

                elif menu == 5 :
                    print('''
        ================================================================
        Terima Kasih Sudah Menggunakan Data Mahasiswa Universitas Komsen 
        ================================================================
                        ''')
                    
                else : 
                    print(f'Masukkan Angka Menu Yang Benar Dan Tersedia (1-5) ')

MenuUtama()