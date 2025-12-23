# Tubes_Analisis_Kompleksitas_Algoritma
Tugas Besar Analisis Waktu Eksekusi Bubble Sort menggunakan metode iteratif dan rekursif

## 👥 Anggota Kelompok
- 👨‍💻 **Muhammad Rizqi Ar Rafi** - `103112400218`  
- 👨‍💻 **Aflah Rizkyadhafin Nurfikri** - `103112400223`  
- 👨‍💻 **Gilar Saputra** - `103112400253`

## Studi Kasus :
Studi kasus ini berfokus untuk menganalisis dataset magnitudo gempa bumi di indonesia pada tahun  2008-2023. studi ini akan menganalisis dan membandingkan waktu eksekusi yang dibutuhkan dari algoritma bubble sort  rekursif dan iteratif untuk menentukan algoritma mana yang lebih efisienm dalam mengeksekusi dataset dalam jumlah n tertentu. 

## Data Perbandingan Waktu Eksekusi
![Data Perbandingan Waktu Eksekusi](https://github.com/aflahrizkyadhafin-tlu/Tubes_Analisis_Kompleksitas_Algoritma/blob/main/image/Tabel%20Waktu%20Eksekusi.png)

## Grafik Waktu Eksekusi
![Grafik Waktu Eksekusi](https://github.com/aflahrizkyadhafin-tlu/Tubes_Analisis_Kompleksitas_Algoritma/blob/main/image/Grafik%20Waktu%20Eksekusi.png)

## Analysis And Results
Analisis dan hasil yang kita dapatkan dari penerapan algoritma bubble sort pada studi ini dengan pendekatan iteratif dan rekursif, keduanya memiliki keunggulan dalam kecepatan dalam mengeksekusi program. Untuk dataset yang kita gunakan maksimal n = 1000, dimana program akan melakukan perulangan dengan kelipatan 10 ( 0, 10, 20, 30, … , n max=1000 ). Untuk dataset dengan ukuran n = 0 hingga n <= 200, keduanya memiliki kecepatan untuk menghasilkan waktu eksekusi yang cepat dan mirip. Tetapi seiring bertambahnya ukuran dataset, waktu eksekusi dari iteratif cenderung lebih cepat dari rekursif . Pada kasus ini, metode iteratif lebih stabil dari metode rekursif yang memiliki resiko memory overflow.

## Conclusion
Dari analisis data gempa bumi tahun 2008 - 2023, bisa kami tarik kesimpulan bahwa metode iteratif itu lebih efektif daripada metode rekursif. Karena pada n = 1000, waktu eksekusi dari metode iteratif hanya memakan waktu 0,094 detik, namun sebaliknya rekursiif membutuhkan waktu yang lebih lama yaitu 0,295 detik. Performa ini juga sejalan dengan penelitian Astuti (2023), yang menyimpulkan bahwa beban dari eksekusi di setiap langkah pengurutan akan sangat memengaruhi kecepatan dari algoritma. Menurut Lutfina et al. (2022), Penggunaan metode iteratif juga lebih stabil karena memiliki alokasi memori tetap dan terhindar dari risiko stack overflow yang di mana sering terjadi pada metode rekursif akibat overhead pemanggilan fungsi.

## Reference
- Astuti, Y. (2023). Analisis Pengujian Data Algoritma Bubble Sort. REMIK: Riset dan E-Jurnal Manajemen Informatika Komputer, 7(3), 1413-1420.
- Lutfina, E., Inayati, N., & Saraswati, G. W. (2022). Analisis perbandingan kinerja metode rekursif dan metode iteratif dalam algoritma linear search. Komputika: Jurnal Sistem Komputer, 11(2), 143-150.

