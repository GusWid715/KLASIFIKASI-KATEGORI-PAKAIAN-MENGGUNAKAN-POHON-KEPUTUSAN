# 1. Import Pustaka yang dibutuhkan
# Pandas untuk membuat tabel data
import pandas as pd
# Tree untuk membuat pohon keputusan
from sklearn import tree
# Preprocessing untuk mengubah kata menjadi angka
from sklearn import preprocessing

# 2. Menyiapkan Data (Sesuai Soal Tugas)
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

# 3. Preprocessing (Mengubah Kata jadi Angka)
# Komputer tidak mengerti kata "Merah" atau "S", jadi kita ubah ke angka.
# Contoh: Merah jadi 0, Biru jadi 1, dst.
le = preprocessing.LabelEncoder()

# Kita buat salinan data untuk diubah ke angka
df_encoded = df.copy()

# Proses pengubahan untuk setiap kolom
df_encoded['Warna'] = le.fit_transform(df['Warna'])
df_encoded['Ukuran'] = le.fit_transform(df['Ukuran'])
df_encoded['Bahan'] = le.fit_transform(df['Bahan'])
df_encoded['Kategori'] = le.fit_transform(df['Kategori'])

print("=== Data Setelah Diubah ke Angka ===")
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

# 6. Menampilkan Aturan Pohon (Rules)
from sklearn.tree import export_text
# Kita berikan nama fitur agar hasil bacanya mudah
r = export_text(clf, feature_names=['Warna', 'Ukuran', 'Bahan'])

print("=== Hasil Pohon Keputusan (Rules) ===")
print(r)