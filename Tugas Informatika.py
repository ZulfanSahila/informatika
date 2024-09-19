# Contoh Input Output di Python

# Input: Meminta pengguna untuk memasukkan nama dan umur
nama = input("Masukkan nama kamu: ")
umur = int(input("Masukkan umur kamu: "))

# Output: Menampilkan pesan dengan nama dan umur yang dimasukkan
print(f"Halo, {nama}! Umur kamu {umur} tahun.")

# Contoh penggunaan input untuk menghitung
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Output: Menampilkan hasil penjumlahan
hasil = angka1 + angka2
print(f"Hasil penjumlahan {angka1} + {angka2} adalah {hasil}.")






# Contoh operator aritmatika di Python

# Input: Memasukkan dua angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Penjumlahan
penjumlahan = angka1 + angka2
print(f"Hasil dari {angka1} + {angka2} = {penjumlahan}")

# Pengurangan
pengurangan = angka1 - angka2
print(f"Hasil dari {angka1} - {angka2} = {pengurangan}")

# Perkalian
perkalian = angka1 * angka2
print(f"Hasil dari {angka1} * {angka2} = {perkalian}")

# Pembagian
pembagian = angka1 / angka2
print(f"Hasil dari {angka1} / {angka2} = {pembagian}")

# Modulus (sisa bagi)
modulus = angka1 % angka2
print(f"Hasil dari {angka1} % {angka2} = {modulus}")

# Eksponen (pangkat)
eksponen = angka1 ** angka2
print(f"Hasil dari {angka1} ** {angka2} = {eksponen}")

# Pembagian bulat (floor division)
pembagian_bulat = angka1 // angka2
print(f"Hasil dari {angka1} // {angka2} = {pembagian_bulat}")






# Contoh Operator penugasan di Python

# Operator penugasan dasar (=)
x = 10
print(f"Nilai x setelah penugasan (=) adalah {x}")

# Operator penugasan tambah sama dengan (+=)
x += 5  # Sama dengan x = x + 5
print(f"Nilai x setelah penugasan (+=) adalah {x}")

# Operator penugasan kurang sama dengan (-=)
x -= 3  # Sama dengan x = x - 3
print(f"Nilai x setelah penugasan (-=) adalah {x}")

# Operator penugasan kali sama dengan (*=)
x *= 2  # Sama dengan x = x * 2
print(f"Nilai x setelah penugasan (*=) adalah {x}")

# Operator penugasan bagi sama dengan (/=)
x /= 4  # Sama dengan x = x / 4
print(f"Nilai x setelah penugasan (/=) adalah {x}")

# Operator penugasan modulus sama dengan (%=)
x %= 2  # Sama dengan x = x % 2
print(f"Nilai x setelah penugasan (%=) adalah {x}")

# Operator penugasan pangkat sama dengan (**=)
x = 5   # Set ulang nilai x
x **= 2  # Sama dengan x = x ** 2
print(f"Nilai x setelah penugasan (**=) adalah {x}")

# Operator penugasan pembagian bulat sama dengan (//=)
x //= 3  # Sama dengan x = x // 3
print(f"Nilai x setelah penugasan (//=) adalah {x}")







# Contoh Operator Pembanding di Python

a = 10
b = 20

# Operator pembanding sama dengan (==)
print(f"Apakah {a} == {b}? {a == b}")  # False

# Operator pembanding tidak sama dengan (!=)
print(f"Apakah {a} != {b}? {a != b}")  # True

# Operator pembanding lebih besar dari (>)
print(f"Apakah {a} > {b}? {a > b}")    # False

# Operator pembanding lebih kecil dari (<)
print(f"Apakah {a} < {b}? {a < b}")    # True

# Operator pembanding lebih besar atau sama dengan (>=)
print(f"Apakah {a} >= {b}? {a >= b}")  # False

# Operator pembanding lebih kecil atau sama dengan (<=)
print(f"Apakah {a} <= {b}? {a <= b}")  # True







# Operator Logika di Python

x = True
y = False

# Operator logika AND (dan)
print(f"{x} AND {y} = {x and y}")  # False, karena salah satu bernilai False

# Operator logika OR (atau)
print(f"{x} OR {y} = {x or y}")  # True, karena salah satu bernilai True

# Operator logika NOT (kebalikan)
print(f"NOT {x} = {not x}")  # False, kebalikan dari True
print(f"NOT {y} = {not y}")  # True, kebalikan dari False

# Contoh kombinasi operator logika
a = 10
b = 20
c = 30

# Menggunakan operator logika AND dengan operator pembanding
print(f"Apakah {a} < {b} AND {b} < {c}? {(a < b) and (b < c)}")  # True

# Menggunakan operator logika OR dengan operator pembanding
print(f"Apakah {a} > {b} OR {b} < {c}? {(a > b) or (b < c)}")  # True

# Menggunakan operator logika NOT dengan operator pembanding
print(f"Apakah NOT({a} > {b})? {not (a > b)}")  # True, karena a tidak lebih besar dari b







# Operator Bitwise di Python

a = 10  # Dalam biner: 00001010
b = 4   # Dalam biner: 00000100

# Operator bitwise AND (&)
and_result = a & b
print(f"{a} & {b} = {and_result} (biner: {bin(and_result)})")

# Operator bitwise OR (|)
or_result = a | b
print(f"{a} | {b} = {or_result} (biner: {bin(or_result)})")

# Operator bitwise XOR (^)
xor_result = a ^ b
print(f"{a} ^ {b} = {xor_result} (biner: {bin(xor_result)})")

# Operator bitwise NOT (~)
not_result_a = ~a
not_result_b = ~b
print(f"~{a} = {not_result_a} (biner: {bin(not_result_a)})")
print(f"~{b} = {not_result_b} (biner: {bin(not_result_b)})")

# Operator bitwise shift kiri (<<)
shift_left_result = a << 2
print(f"{a} << 2 = {shift_left_result} (biner: {bin(shift_left_result)})")

# Operator bitwise shift kanan (>>)
shift_right_result = a >> 2
print(f"{a} >> 2 = {shift_right_result} (biner: {bin(shift_right_result)})")
