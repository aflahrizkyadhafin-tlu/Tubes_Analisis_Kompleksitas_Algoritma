# 📊 Tubes Analisis Kompleksitas Algoritma

> **Tugas Besar:** Analisis Waktu Eksekusi Bubble Sort menggunakan Metode Iteratif dan Rekursif

---

## 👥 Anggota Kelompok

| No | Nama | NIM |
|:--:|------|-----|
| 1 | Muhammad Rizqi Ar Rafi | `103112400218` |
| 2 | Aflah Rizkyadhafin Nurfikri | `103112400223` |
| 3 | Gilar Saputra | `103112400253` |

---

## 📋 Studi Kasus

Studi kasus ini berfokus untuk menganalisis **dataset magnitudo gempa bumi di Indonesia pada tahun 2008-2023**. Studi ini akan menganalisis dan membandingkan waktu eksekusi yang dibutuhkan dari algoritma bubble sort rekursif dan iteratif untuk menentukan algoritma mana yang lebih efisien dalam mengeksekusi dataset dalam jumlah *n* tertentu.

---

## 📈 Analysis And Results

Analisis dan hasil yang kita dapatkan dari penerapan algoritma bubble sort pada studi ini dengan pendekatan **iteratif** dan **rekursif**:

- ✅ Untuk dataset dengan ukuran `n = 0` hingga `n <= 200`, keduanya memiliki waktu eksekusi yang **cepat dan mirip**
- ⚡ Seiring bertambahnya ukuran dataset, waktu eksekusi **iteratif cenderung lebih cepat** dari rekursif
- ⚠️ Metode iteratif lebih **stabil** dari metode rekursif yang memiliki risiko *memory overflow*

> **Catatan:** Dataset maksimal `n = 1000`, dengan perulangan kelipatan 10 (0, 10, 20, 30, … , n max=1000)

---

## 📊 Data Perbandingan Waktu Eksekusi

![Data Perbandingan Waktu Eksekusi](https://github.com/aflahrizkyadhafin-tlu/Tubes_Analisis_Kompleksitas_Algoritma/blob/main/image/Tabel%20Waktu%20Eksekusi.png)

---

## 📉 Grafik Waktu Eksekusi

![Grafik Waktu Eksekusi](https://github.com/aflahrizkyadhafin-tlu/Tubes_Analisis_Kompleksitas_Algoritma/blob/main/image/Grafik%20Waktu%20Eksekusi.png)

---

## ✅ Conclusion

Dari analisis data gempa bumi tahun **2008 - 2023**, dapat ditarik kesimpulan:

| Metode | Waktu Eksekusi (n=1000) | Status |
|--------|:-----------------------:|:------:|
| **Iteratif** | `0,094 detik` | ✅ Lebih Cepat |
| **Rekursif** | `0,295 detik` | ❌ Lebih Lambat |

### Key Findings:
1. **Metode iteratif lebih efektif** daripada metode rekursif
2. Metode iteratif memiliki **alokasi memori tetap** dan terhindar dari risiko *stack overflow*
3. Beban eksekusi di setiap langkah pengurutan sangat memengaruhi kecepatan algoritma

---

## 📚 Reference

1. Astuti, Y. (2023). *Analisis Pengujian Data Algoritma Bubble Sort*. REMIK: Riset dan E-Jurnal Manajemen Informatika Komputer, **7**(3), 1413-1420.

2. Lutfina, E., Inayati, N., & Saraswati, G. W. (2022). *Analisis perbandingan kinerja metode rekursif dan metode iteratif dalam algoritma linear search*. Komputika: Jurnal Sistem Komputer, **11**(2), 143-150.

---

<p align="center">
  <i>Made with ❤️ for Algoritma Kompleksitas Course</i>
</p>
