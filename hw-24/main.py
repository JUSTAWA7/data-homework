#  1.Ism-sharif: toliq_ism funksiyasini yarating. U ism va familiya qabul qilsin, lekin familiya kiritilmasa, u standart bo'sh matn "" bo'lsin. Funksiya birlashtirilgan matnni qaytarsin.

# def ism_sharif(ism,familiya=""):
#     if familiya=="" :
#         return ism
#     else:
#         return ism+familiya
# print(ism_sharif("azz","bdd"))


# 2.Valyuta konvertori: kurs_hisobla funksiyasi miqdor va kurs (standart qiymati 12600) qabul qilsin. Funksiya so'mga aylantirilgan qiymatni qaytarsin.

# def kurs_hisobla(miqdor,kurs=12600):
#     return miqdor*kurs
# print(kurs_hisobla(20))


# 3.Do'kon cheki: hisob_kitob funksiyasi mahsulot, narh, soni va chegirma (standart 0) parametrlarini qabul qilsin. Argumentlarni uzatishda ularning tartibini aralashtirib yuboring (masalan, birinchi chegirma, keyin mahsulot). Funksiya jami summani matn ko'rinishida qaytarsin.

# def hisob_kitob(mahsulot,narh,soni,chegirma):
#     kop = narh * soni
#     jami = kop - (kop * chegirma / 100)
#     return mahsulot+" jami summa: "+str(jami)

# print(hisob_kitob("Anor",32,15,10))

