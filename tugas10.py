# mengimpor modul tkinter dan sqlite3
import tkinter as tk
import sqlite3

def hasil_prediksi():
    # Mendapatkan nilai dari input
    nama = entry_nama.get()
    # Input pengguna.
    nilai_biologi = float(entry_biologi.get())
    nilai_fisika = float(entry_fisika.get())
    nilai_inggris = float(entry_inggris.get())
    nilai_mtk = float(entry_mtk.get())
    nilai_kimia = float(entry_kimia.get())
    nilai_sejarah = float(entry_sejarah.get())
    nilai_geografi = float(entry_geografi.get())
    nilai_seni = float(entry_seni.get())
    nilai_olahraga = float(entry_olahraga.get())
    nilai_bahasa = float(entry_bahasa.get())

    # Menentukan hasil prediksi berdasarkan nilai tertinggi
    # Membandingkan nilai dari 13 mata pelajaran
    nilai_tinggi = max(nilai_biologi, nilai_fisika, nilai_inggris, nilai_mtk, nilai_kimia,
                       nilai_sejarah, nilai_geografi, nilai_seni, nilai_olahraga,
                       nilai_bahasa)
    
    # mendefinisikan fungsi prediksi()
    #Fungsi ini digunakan untuk memprediksi nilai siswa untuk masuk ke fakultas 
    if nilai_tinggi == nilai_biologi:
        hasil_prodi = "Kedokteran"
    elif nilai_tinggi == nilai_fisika:
        hasil_prodi = "Teknik"
    elif nilai_tinggi == nilai_inggris:
        hasil_prodi = "Bahasa"
    elif nilai_tinggi == nilai_mtk:
        hasil_prodi = "Teknik"
    elif nilai_tinggi == nilai_kimia:
        hasil_prodi = "Kedokteran"
    elif nilai_tinggi == nilai_sejarah:
        hasil_prodi = "Bahasa"
    elif nilai_tinggi == nilai_geografi:
        hasil_prodi = "Fisipol"
    elif nilai_tinggi == nilai_seni:
        hasil_prodi = "Ilmu Budaya"
    elif nilai_tinggi == nilai_olahraga:
        hasil_prodi = "Keolahragaan"
    elif nilai_tinggi == nilai_bahasa:
        hasil_prodi = "Bahasa"    
    # Tambahkan kondisi untuk prodi berdasarkan nilai tertinggi dari mata pelajaran lainnya
    else:
        hasil_prodi = "Belum dapat diprediksi"

    # Menampilkan hasil prediksi
    hasil.config(text=f"Prodi Pilihan: {hasil_prodi}")

    # Menyimpan data ke SQLite
    conn = sqlite3.connect('data_nilai_siswa.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama_siswa TEXT,
                        biologi REAL,
                        fisika REAL,
                        inggris REAL,
                        mtk REAL,
                        kimia REAL,
                        sejarah REAL,
                        geografi REAL,
                        seni REAL,
                        olahraga REAL,
                        bahasa REAL,
                        prediksi_fakultas TEXT
                    )''')
    cursor.execute('''INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, mtk,
                    kimia, sejarah, geografi, seni, olahraga, Bahasa, prediksi_fakultas)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (nama, nilai_biologi, nilai_fisika, nilai_inggris, nilai_mtk, nilai_kimia,
                    nilai_sejarah, nilai_geografi, nilai_seni, nilai_olahraga,
                    nilai_bahasa, hasil_prodi))
    conn.commit()
    conn.close()

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Prediksi Prodi Anda Sekarang",)
root.geometry("1000x500")  # Mengatur ukuran jendela
root.attributes("-fullscreen", True) # Full Screen

# Label judul
label_judul = tk.Label(root, text="Prediksi Prodi Anda sekarang", font=("Times New Roman", 16))
label_judul.pack(pady=10)

# Input nilai mata pelajaran
label_nama = tk.Label(root, text="Nama Siswa: ")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

# Membuat 10 label dan entry baru untuk 10 mata pelajaran tambahan
label_biologi = tk.Label(root, text="Nilai Biologi: ")
label_biologi.pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

label_fisika = tk.Label(root, text="Nilai Fisika: ")
label_fisika.pack()
entry_fisika = tk.Entry(root)
entry_fisika.pack()

label_inggris = tk.Label(root, text="Nilai Inggris: ")
label_inggris.pack()
entry_inggris = tk.Entry(root)
entry_inggris.pack()

label_mtk = tk.Label(root, text="Nilai Mtk: ")
label_mtk.pack()
entry_mtk = tk.Entry(root)
entry_mtk.pack()

label_kimia = tk.Label(root, text="Nilai Kimia: ")
label_kimia.pack()
entry_kimia = tk.Entry(root)
entry_kimia.pack()

label_sejarah = tk.Label(root, text="Nilai Sejarah: ")
label_sejarah.pack()
entry_sejarah = tk.Entry(root)
entry_sejarah.pack()

label_geografi = tk.Label(root, text="Nilai Geografi: ")
label_geografi.pack()
entry_geografi = tk.Entry(root)
entry_geografi.pack()

label_seni = tk.Label(root, text="Nilai Seni: ")
label_seni.pack()
entry_seni = tk.Entry(root)
entry_seni.pack()

label_olahraga = tk.Label(root, text="Nilai Olahraga: ")
label_olahraga.pack()
entry_olahraga = tk.Entry(root)
entry_olahraga.pack()

label_bahasa = tk.Label(root, text="Nilai Bahasa: ")
label_bahasa.pack()
entry_bahasa = tk.Entry(root)
entry_bahasa.pack()

# Button Submit Nilai
button_submit = tk.Button(root, text="Submit Nilai", command=hasil_prediksi)
button_submit.pack(pady=10)

# Label luaran hasil prediksi
hasil = tk.Label(root, text="Prodi Pilihan: ", font=("Arial", 12))
hasil.pack()

root.mainloop()