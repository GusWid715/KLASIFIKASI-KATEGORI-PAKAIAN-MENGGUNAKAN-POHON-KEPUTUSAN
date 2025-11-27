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