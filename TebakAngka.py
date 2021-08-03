import random 

angka = random.randint(1,100)
for jawab in range(1,10):
    tanya = int(input("\nTebak Angka Berapa ! : "))

    if angka == tanya:
        print("Selamat Kamu Benar")
        break
    elif angka > tanya:
        print("Angka Yang Kamu Masukkan Kekecilan")
    elif angka < tanya:
        print("Angka Yang Kamu Masukkan Kebesaran")
    else:
        print("Kamu Salah Coba Masukkan Angka Yang Lain")
else:
    print("\nJawabannya Adalah = ",angka)