import time
import csv
import sys
import matplotlib.pyplot as plt

# Meningkatkan batas rekursi untuk menangani dataset yang besar
sys.setrecursionlimit(1000000)

# Konfigurasi Dataset
MaxData = 1000
jumlahDataAwal = 10
kelipatan = 10

# List untuk menyimpan hasil
runningTimesIteratif = []
runningTimesRekursif = []
jumlahDataList = []

# --- Fungsi Algoritma Bubble Sort ---

def Iteratif(rawData, arrLength):
    temp = 0
    swapped = 0
    n = arrLength
    while n >= 0:
        k = 0
        while k < n - 1:
            if rawData[k+1] < rawData[k]:
                swapped = 1
                temp = rawData[k+1]
                rawData[k+1] = rawData[k]
                rawData[k] = temp
            k += 1
        n -= 1
        if swapped == 0:
            break
        swapped = 0

def Rekursif(rawData, n, k, swapped):
    if n <= 1:
        return
    
    if k < n - 1:
        if rawData[k + 1] < rawData[k]:
            swapped = 1
            temp = rawData[k + 1]
            rawData[k + 1] = rawData[k]
            rawData[k] = temp
        Rekursif(rawData, n, k + 1, swapped)
    else:
        if swapped == 1:
            Rekursif(rawData, n - 1, 0, 0)

# --- Proses Membaca Data CSV ---

rawData = []
try:
    # Ganti 'katalog_gempa.csv' dengan file Anda
    with open('katalog_gempa.csv', mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if len(rawData) < MaxData:
                # Mengambil kolom ke-6 (indeks 5) yang berisi magnitude/data angka
                if len(row) > 5 and row[5]:
                    try:
                        rawData.append(float(row[5]))
                    except ValueError:
                        continue 
            else:
                break
except Exception as e:
    print(f"Error saat membaca file: {e}")
    sys.exit(1)

# --- Eksekusi Pengukuran Waktu ---

# Running rekursif
print("===== Run Rekursif =====")
arrLength = jumlahDataAwal
while arrLength <= len(rawData):
    print("Rekursif | Sort data sebanyak : ", arrLength)
    start_time = time.time()
    dataCopy = rawData[:arrLength].copy()
    Rekursif(dataCopy, arrLength, 0, 0)
    elapsed_time = time.time() - start_time
    
    runningTimesRekursif.append(elapsed_time)
    jumlahDataList.append(arrLength)
    arrLength += kelipatan

# Running iteratif
print("===== Run Iteratif =====")
arrLength = jumlahDataAwal
while arrLength <= len(rawData):
    print("Iteratif | Sort data sebanyak : ", arrLength)
    start_time = time.time()
    dataCopy = rawData[:arrLength].copy()
    Iteratif(dataCopy, arrLength)
    elapsed_time = time.time() - start_time
    
    runningTimesIteratif.append(elapsed_time)
    arrLength += kelipatan

# --- Output Tabel di Terminal ---

display_n = [10, 20, 200, 400, 600, 800, 1000]
print("\n+------+----------------------+----------------------+")
print("| n    | Recursive Time (ms)  | Iterative Time (ms)  |")
print("+------+----------------------+----------------------+")

for i, n_val in enumerate(jumlahDataList):
    if n_val in display_n:
        print(f"| {n_val:<4} | {runningTimesRekursif[i]*1000:<20.5f} | {runningTimesIteratif[i]*1000:<20.5f} |")

print("+------+----------------------+----------------------+")

# --- Visualisasi Grafik ---

# Konversi detik ke milidetik (ms) untuk grafik
y_rekursif_ms = [t * 1000 for t in runningTimesRekursif]
y_iteratif_ms = [t * 1000 for t in runningTimesIteratif]

plt.figure(figsize=(10, 6))

# Plotting
plt.plot(jumlahDataList, y_iteratif_ms, label='Iterative', color='blue')
plt.plot(jumlahDataList, y_rekursif_ms, label='Recursive', color='green',linestyle='--')

x_display = [n for n in display_n if n in jumlahDataList]
y_iter_display = [y_iteratif_ms[jumlahDataList.index(n)] for n in x_display]
y_rek_display = [y_rekursif_ms[jumlahDataList.index(n)] for n in x_display]
plt.scatter(x_display, y_iter_display, color='blue', marker='o', s=30, zorder=5)
plt.scatter(x_display, y_rek_display, color='green', marker='s', s=30, zorder=5)


# plt.plot(jumlahDataList, y_iteratif_ms, label='Iterative', color='blue', marker='o', markersize=4)
# plt.plot(jumlahDataList, y_rekursif_ms, label='Recursive', color='green', marker='s', linestyle='--', markersize=4)

# Menambahkan anotasi pada titik
for i in display_n :
    idx = jumlahDataList.index(i)
    plt.text(i, y_iteratif_ms[idx], f' {y_iteratif_ms[idx]:.2f}', color='blue', fontweight='bold')
    plt.text(i, y_rekursif_ms[idx], f' {y_rekursif_ms[idx]:.2f}', color='green', fontweight='bold')
    
# Pengaturan Label dan Judul
plt.title('Perbandingan Waktu Eksekusi Bubble Sort: Iteratif vs Rekursif', fontsize=14)
plt.xlabel('Data Size (n)', fontsize=12)
plt.ylabel('Execution Time (ms)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.tight_layout()
plt.show()