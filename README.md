# 🌳 Klasifikasi Kategori Pakaian (Pohon Keputusan ID3)

**Tugas Kelompok 1**  
Mata Kuliah Pemodelan dan Simulasi  
Program Studi Informatika - Universitas Udayana

---

## 📖 Deskripsi Proyek

Aplikasi ini bertujuan untuk memprediksi kategori pakaian (**Casual** atau **Formal**) berdasarkan karakteristik fisik pakaian seperti **Warna**, **Ukuran**, dan **Bahan**. Sistem ini dibangun menggunakan algoritma **Decision Tree (ID3)** dengan kriteria **Entropy**.

---

## ✨ Fitur Utama

- **Visualisasi Data**: Menampilkan dataset awal pakaian dalam bentuk tabel interaktif
- **Aturan Keputusan (Rules)**: Menampilkan logika "If-Then" yang dihasilkan oleh algoritma ID3 dalam bahasa yang mudah dipahami
- **Grafik Pohon**: Visualisasi grafis struktur pohon keputusan untuk melihat alur logika klasifikasi
- **Simulasi Prediksi**: Pengguna dapat memilih atribut pakaian (Warna, Ukuran, Bahan) dan sistem akan menebak kategorinya secara real-time

---

## 🛠️ Teknologi yang Digunakan

Proyek ini dikembangkan menggunakan bahasa pemrograman **Python** dengan pustaka berikut:

- **Streamlit**: Framework untuk membuat antarmuka web (UI) yang interaktif
- **Scikit-Learn**: Implementasi algoritma Decision Tree Classifier (ID3)
- **Pandas**: Manipulasi dan penyajian data tabel
- **Matplotlib**: Pembuatan grafik visualisasi pohon keputusan

---

## 🚀 Cara Menjalankan Aplikasi

Ikuti langkah-langkah berikut untuk menjalankan aplikasi di komputer lokal Anda.

### 1. Persiapan Environment

Pastikan Anda memiliki Python terinstal. Disarankan menggunakan Virtual Environment agar bersih.

```bash
# Buat environment baru (Windows)
python -m venv myenv

# Aktifkan environment
myenv\Scripts\activate

# Untuk Linux/Mac
source myenv/bin/activate
```

### 2. Instalasi Pustaka

Instal semua dependensi yang diperlukan menggunakan `pip`.

```bash
pip install -r requirements.txt
```

**Catatan**: Jika file `requirements.txt` belum ada, instal manual dengan perintah:

```bash
pip install streamlit pandas scikit-learn matplotlib
```

### 3. Jalankan Program

Gunakan perintah `streamlit` untuk memulai aplikasi.

```bash
streamlit run ID3.py
```

*(Ganti `ID3.py` dengan nama file Python Anda jika berbeda, misal `app.py`)*

Setelah berhasil, browser akan otomatis terbuka di alamat: **http://localhost:8501**

---

## 📂 Struktur File

```
project-root/
│
├── ID3.py               # Kode utama aplikasi (logika ID3 dan UI Streamlit)
├── requirements.txt     # Daftar pustaka Python yang dibutuhkan
└── README.md           # Dokumentasi proyek ini
```

---

## 📦 Isi File `requirements.txt`

```
streamlit
pandas
scikit-learn
matplotlib
```
