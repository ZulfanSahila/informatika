# Kalkulator Sederhana

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Masukan angka selain 0"
    else:
        return x / y

def calculator():
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    choice = input("Masukkan pilihan (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))

        if choice == '1':
            print(f"Hasil: {num1} + {num2} = {tambah(num1, num2)}")

        elif choice == '2':
            print(f"Hasil: {num1} - {num2} = {kurang(num1, num2)}")

        elif choice == '3':
            print(f"Hasil: {num1} * {num2} = {kali(num1, num2)}")

        elif choice == '4':
            print(f"Hasil: {num1} / {num2} = {bagi(num1, num2)}")

    else:
        print("Pilihan tidak valid")

calculator()
