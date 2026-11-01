import modul_evaluasi

while True:
    try:
        pilihan = int(input("1. Hitung kelayakan, 2. keluar : "))

        if pilihan == 1:
            nama = input("Masukan nama: ")
            nim  = int(input("Masukan nim: "))
            hadir = float(input("Masukan total kehadiran: "))
            if hadir < 0 or hadir > 14:
                print("Hanya masukan angka rentang 0 sampai 14 saja")
                continue
            tugas = modul_evaluasi.minta_input_nilai("TUGAS")
            ucp1  = modul_evaluasi.minta_input_nilai("UCP1")
            ucp2  = modul_evaluasi.minta_input_nilai("UCP2") 

            print("\nSedang memproses data")

            total_hadir = modul_evaluasi.hitung_persentase_presensi(hadir)
            nilai_akhir = modul_evaluasi.hitung_nilai_akhir(tugas, ucp1, ucp2)
            status_akhir = modul_evaluasi.cek_kelayakan_aslab(total_hadir, nilai_akhir)

            print("===============================")
            print(f"HASIL EVALUASI: {nama.upper()}")
            print("===============================")
            print(f"NILAI TOTAL: {nilai_akhir}")
            print(f"STATUS & GRADE: {status_akhir}")
            print("================================")

            pilih = input("Apakah ada yang ingin dihitung lagi?(ya/tidak): ")
            if pilih == "ya":
                continue
            else:
                break
        elif pilihan == 2:
            break
    except ValueError:
        print("[ERROR SYSTEM] Tipe data salah! Anda memasukan teks, harap masukan ANGKA.\n")
