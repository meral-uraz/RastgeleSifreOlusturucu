import random
import string

adet = int(input("Oluşturulacak şifre sayısını girin: "))

karakter_sayisi = int(input("Şifrelerin kaç karakterli olması gerektiğini girin (en az 4 karakter olmalı): "))
while karakter_sayisi < 4:
    print("Şifre uzunluğu en az 4 karakter olmalıdır.")
    karakter_sayisi = int(input("Lütfen en az 4 karakter uzunluğunda bir değer girin: "))

print("""Şifre tipini seçin:
1. Tip : En az 1 büyük harf, 1 küçük harf, 1 rakam, 1 simge
2. Tip : En az 1 büyük harf, 1 küçük harf, 1 rakam
3. Tip : En az 1 büyük harf, 1 küçük harf, 1 simge
4. Tip : En az 1 büyük harf, 1 küçük harf
5. Tip : Tamamen rakam""")
tip = int(input("Seçiminizi girin (1-5): "))

buyuk_harfler = string.ascii_uppercase
kucuk_harfler = string.ascii_lowercase
rakamlar = string.digits
semboller = string.punctuation

def sifre_olustur(adet, karakter_sayisi, tip):
    for _ in range(adet):
        sifre = []

        # Seçilen şifre tipine göre gerekli karakterleri ekle
        if tip == 1:
            sifre = [
                random.choice(buyuk_harfler),
                random.choice(kucuk_harfler),
                random.choice(rakamlar),
                random.choice(semboller)
            ]
            tum_karakterler = buyuk_harfler + kucuk_harfler + rakamlar + semboller
        elif tip == 2:
            sifre = [
                random.choice(buyuk_harfler),
                random.choice(kucuk_harfler),
                random.choice(rakamlar)
            ]
            tum_karakterler = buyuk_harfler + kucuk_harfler + rakamlar
        elif tip == 3:
            sifre = [
                random.choice(buyuk_harfler),
                random.choice(kucuk_harfler),
                random.choice(semboller)
            ]
            tum_karakterler = buyuk_harfler + kucuk_harfler + semboller
        elif tip == 4:
            sifre = [
                random.choice(buyuk_harfler),
                random.choice(kucuk_harfler)
            ]
            tum_karakterler = buyuk_harfler + kucuk_harfler
        elif tip == 5:
            sifre = [random.choice(rakamlar) for _ in range(karakter_sayisi)]
            tum_karakterler = rakamlar
        else:
            print("Geçersiz seçim! Lütfen 1 ile 5 arasında bir değer girin.")
            return

        if tip != 5:
            # Geri kalan karakterleri rastgele seç
            geri_kalan_karakter_sayisi = karakter_sayisi - len(sifre)
            sifre += random.choices(tum_karakterler, k=geri_kalan_karakter_sayisi)
        
            # Şifreyi karıştır
            random.shuffle(sifre)

        sifre = ''.join(sifre)
        print(sifre)

sifre_olustur(adet, karakter_sayisi, tip)

while True:
    devam = input("Aynı özelliklerle yeniden şifre oluşturmak ister misiniz? (E/H): ").strip().lower()
    if devam == 'e':
        sifre_olustur(adet, karakter_sayisi, tip)
    elif devam == 'h':
        print("Programdan çıkılıyor.")
        break
    else:
        print("Lütfen 'Evet' veya 'Hayır' olarak cevap verin.")