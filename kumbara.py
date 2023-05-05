def kumbara():
    aylık_para = 0
    hafta1 = 0
    hafta2 = 0
    hafta3 = 0
    hafta4 = 0

    while hafta1 ==0:
        try:
            hafta1 = float(input("Birinci hafta toplanan para: "))
        except ValueError:
            print("Lütfen sadece rakam giriniz.")

    while hafta2 ==0:
        try:
            hafta2 = float(input("İkinci hafta toplanan para: "))
        except ValueError:
            print("Lütfen rakam giriniz.")

    while hafta3 ==0:
        try:
            hafta3 = float(input("Üçüncü hafta toplanan para: "))
        except ValueError:
            print("Lütfen rakam giriniz.")

    while hafta4 ==0:
        try:
            hafta4 = float(input("Dördüncü hafta toplanan para: "))
        except ValueError:
            print("Lütfen rakam giriniz.")
    aylık_para = hafta1 + hafta2 + hafta3 + hafta4
    print("Aylık para: ", aylık_para)
    return aylık_para

print("Ocak ayı toplanan para")
Ocak = kumbara()

print("Şubat ayı toplanan para")
Subat = kumbara()

print("Mart ayı toplanan para")
Mart = kumbara()

toplam = Ocak + Subat + Mart
print("Toplam para: ", toplam)
