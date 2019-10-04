print("MONUR tarafından hazırlanmış adamlık testidir. Lütfen isimleri tam olarak giriniz. Büyük, küçük harflerle ya da bAtUHaN şeklinde girebilirsiniz.")
insanlar = []
n = int(input("Kaç Tane İnsan Girilecek? "))

for i in range (0, n):
    insanlar.append(input(str(i + 1) + ". Kişiyi Giriniz: ").upper())

adamlar = []
for insan in insanlar:
    if insan == "BATUHAN":
        continue
    adamlar.append(insan)

print("Adamlar Listesi: ")
for adam in adamlar:
    if adam == "BATUHAN":
        break # Allah korusun listeye falan girer bir daha emin olalım.
    print(adam)
