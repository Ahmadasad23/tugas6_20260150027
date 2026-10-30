import sys
import time

def hitung_persentase_presensi(hadir, total_pertemuan=14):
    persentase_presensi = (hadir / total_pertemuan ) * 100
    return persentase_presensi
def hitung_nilai_akhir(tugas, ucp1, ucp2):
    nilai_akhir = (tugas * 0.20) + (ucp1 * 0.40) + (ucp2 * 0.40)
    return nilai_akhir

def cek_kelayakan_aslab(persentase_presensi, nilai_akhir):
    if persentase_presensi < 75.0:
        return "DITOLAk(KEHADIRAN DI BAWAH 75%)"
    elif persentase_presensi >= 75.0 and nilai_akhir >= 75.0:
        return "DITERIMA(MEMENUHI SYARAT)"
    elif persentase_presensi >= 75.0 and nilai_akhir < 75.0:
        return "DITOLAK(NILAI AKHIR KURANG)"

def minta_input_nilai(NAMA_KOMPONEN):
    while True:
        try:
            #mencoba menerima input dan mengubahnya ke desimal(float)
            teks_input = input(f"Masukkan nilai {NAMA_KOMPONEN} (0-100): ")
            nilai = float(teks_input)

            # Debuggung logika: mencegah nilai di luar range 0-100
            if nilai < 0 or nilai > 100:
                print("[WARNING] Nilai tidak masuk akal! Harap masukan rentahng 0 hingga 100.\n")
                continue

            # Jika semua aman, kembalikan nilai dan hentikan loop
            return nilai
        except ValueError:
            # Menangkap error jika user memasukan huruf (misal: "delapan puluh")
            print("[ERROR SYSTEM] Tipe data salah! Anda memasukan teks, harap masukan ANGKA.\n")