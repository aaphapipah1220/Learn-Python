#belajar input data


print('silahkan masukkan nama anda')
nama = input()

print(f'hai {nama}, selamat belajar. semangat yah!')

#belajar input data number

print('Angka pertama : ')
a = input()

print('angka kedua : ')
b = input()

hasil = a+b
print(f'hasil {a} + {b} = {hasil}')

print('dasarnya jika kita menggunakan input() itu adalah tipe data string atau text, jika ingin dibaya sebagai angka maka harus diubah menjadi integer dengan cara didepan input ditambah int(input())')
print('Angka pertama : ')
a = int(input())

print('angka kedua : ')
b = int(input())

hasil = a+b
print(f'hasil {a} + {b} = {hasil}')