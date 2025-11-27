# 1. Import Pustaka yang dibutuhkan
# Untuk membuat tampilan Web App
import streamlit as st          
# Pandas untuk membuat tabel data
import pandas as pd             
# Tree untuk membuat pohon keputusan
from sklearn import tree        
# Preprocessing untuk mengubah kata menjadi angka
from sklearn import preprocessing 
# Untuk menampilkan aturan teks
from sklearn.tree import export_text 
# Untuk visualisasi grafik pohon
import matplotlib.pyplot as plt 


# 2. Menyiapkan Data 
data = {
    'Warna': ['Merah', 'Biru', 'Hijau', 'Kuning', 'Merah', 'Biru', 'Hijau', 'Kuning'],
    'Ukuran': ['S', 'M', 'L', 'S', 'M', 'L', 'S', 'M'],
    'Bahan': ['Katun', 'Sutra', 'Wol', 'Sutra', 'Katun', 'Wol', 'Katun', 'Sutra'],
    'Kategori': ['Casual', 'Formal', 'Casual', 'Casual', 'Casual', 'Formal', 'Casual', 'Formal']
}

# Membuat tabel (DataFrame) agar rapi
df = pd.read_json(pd.DataFrame(data).to_json())
print("=== Data Awal ===")
print(df)
print("\n")

# 3. Preprocessing (Mengubah Kata menjadi Angka)
# LabelEncoder terpisah untuk setiap kolom agar bisa dibalikkan nanti
le_warna = preprocessing.LabelEncoder()
le_ukuran = preprocessing.LabelEncoder()
le_bahan = preprocessing.LabelEncoder()
le_kategori = preprocessing.LabelEncoder() # Penting: Simpan encoder kategori

# Buat salinan tabel untuk menampung angka
df_encoded = df.copy()

# Lakukan transformasi (Kata -> Angka)
df_encoded['Warna'] = le_warna.fit_transform(df['Warna'])
df_encoded['Ukuran'] = le_ukuran.fit_transform(df['Ukuran'])
df_encoded['Bahan'] = le_bahan.fit_transform(df['Bahan'])
df_encoded['Kategori'] = le_kategori.fit_transform(df['Kategori'])

print("=== Data Siap Hitung (Angka) ===")
print(df_encoded)
print("\n")

# 4. Memisahkan Data
# Fitur: Data penentu (Warna, Ukuran, Bahan)
features = df_encoded[['Warna', 'Ukuran', 'Bahan']]
# Target: Hasil yang dicari (Kategori)
target = df_encoded['Kategori']

# 5. Membuat Model Pohon Keputusan (ID3)
# criterion='entropy' digunakan agar mirip dengan rumus ID3 manual
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(features, target)

# 6. Menampilkan Hasil Pohon (Rules)
from sklearn.tree import export_text

# Mengambil nama fitur agar aturan mudah dibaca
r = export_text(clf, feature_names=['Warna', 'Ukuran', 'Bahan'])

# --- TRIK AGAR OUTPUT BUKAN ANGKA ---
# Kita ambil daftar nama kategori asli: ['Casual', 'Formal']
# Karena Casual urutan abjad pertama, dia jadi 0. Formal jadi 1.
daftar_kategori = list(le_kategori.classes_) 

# Kita ganti teks "class: 0" menjadi "class: Casual", dst.
for i, nama in enumerate(daftar_kategori):
    # Logika: ganti tulisan 'class: 0' dengan 'class: Casual'
    r = r.replace(f"class: {i}", f"class: {nama}")

print("=== Hasil Pohon Keputusan (Rules) ===")
print(r)