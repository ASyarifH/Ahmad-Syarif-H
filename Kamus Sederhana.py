#Kamus Sederhana Dengan Mensorting Urutan Dari A-Z menggunakan Bubble Sort, Selection Sort, Insertion Sort
import csv

with open('kamus Sederhana.csv') as file:
    reader = csv.reader(file)
    data = []
    for row in reader:
        data.append((row[0], row[1]))

#Bubble Sort
def bubble_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

#Selection Sort
def selection_sort(data, key):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j][key] < data[min_idx][key]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

#Insertion Sort
def insertion_sort(data, key):
    n = len(data)
    for i in range(1, n):
        j = i-1
        key_value = data[i][key]
        while j >= 0 and data[j][key] > key_value:
            data[j+1] = list(data[j])
            data[j] = list(data[j])
            data[j+1][key], data[j][key] = data[j][key], key_value
            j -= 1
        data[j+1] = tuple(data[j+1])
    return data


print("Pilih jenis sorting:")
print("1. Berdasarkan kata bahasa Inggris")
print("2. Berdasarkan kata terjemahan")
pilihan = int(input("Masukkan pilihan (1/2): "))

print("Pilih algoritma sorting:")
print("1. Bubble sort")
print("2. Selection sort")
print("3. Insertion sort")
sorting = int(input("Masukkan pilihan (1/2/3): "))

if pilihan == 1:
    if sorting == 1:
        data = bubble_sort(data, 0)
    elif sorting == 2:
        data = selection_sort(data, 0)
    elif sorting == 3:
        data = insertion_sort(data, 0)
elif pilihan == 2:
    if sorting == 1:
        data = bubble_sort(data, 1)
    elif sorting == 2:
        data = selection_sort(data, 1)
    elif sorting == 3:
        data = insertion_sort(data, 1)
else:
    print("Pilihan tidak sesuai dengan Menu yang ada. Coba pilih lagi sesuai dengan menu yang ada")

for row in data:
    if pilihan == 1:
        print(row[0], "Dalam bahasa Indonesia artinya", row[1])
    elif pilihan == 2:
        print(row[1], "In English mean", row[0])
