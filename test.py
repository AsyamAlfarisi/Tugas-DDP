motor = ["R15","Sport","155cc","Biru"]
motor.append("Rp33.500.000")
motor.append("Tipe155cc")
motor.insert(2,"Yamaha")
print(motor)

print("""
      Ini adalah program penghitung otomatis
      1. Hitung Persegi
      2. Hitung Lingkaran
      3. Hitung Segitiga 
      """)

pilihan = input("Masukan Pilihan: ")
match pilihan:
    case "1":
        s = int(input("Masukan Sisi:" ))
        persegi = s*s 
        print('luas persegi', persegi)
    case "2":
        phi = 3.14
        r = int(input("Masukan jari: "))
        lingkaran = phi*r*r
        print('luas lingkaran', lingkaran)
    case "3":
        a = int(input("Masukan Alas"))
        t = int(input("Masukan Tinggi"))
        I = 1/2 
        segitiga = a*t*I
        print('luas segitiga', segitiga )
    case _:
        print("tidak ada opsi")


