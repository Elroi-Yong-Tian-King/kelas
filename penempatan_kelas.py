#Atur cara menentukan penempatan kels

nama=str(input("Masukkan nama  anda:"))
markah=float(input("Masukkan markah anda:"))

#Kategori kelas
if markah<=40:
    print("Anda ditempatan di kelas Dedikasi")
elif markah<=60:
    print("Anda ditempatan di kelas Cerdik")
elif markah<=80:
    print("Anda ditempatan di kelas Bijak")
elif markah>80:
    print("Anda ditempatan di kelas Amanah")  
