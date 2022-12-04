#Hazırlayan:Nurullah Budakoğlu

duzlestirilmisListe=[]
def ListeyiDuzlestirenFonksiyon(liste):

    for i in liste:   # i tek tek liste elamanlarında gezer
        if type(i)==type(list()): # eğer i olan elemanın kendisi de bir liste ise
            ListeyiDuzlestirenFonksiyon(i) # o elemanı düzleştirmek üzere aynı fonksiyona yollanır
        elif type(i)==type("string") or type(i)==type(1): #eğer string veya int ise
            duzlestirilmisListe.append(i)                 #düzleştirilmiş listeye eklenir

def ListeyiTersineCevirenFonksiyon(liste):

    for i in range(len(liste)): #i tek tek liste elamanlarının indexlerinde gezer
        if type(liste[i]) == type(list()): #eğer listedeki o eleman bir baska liste ise
            liste[i].reverse() #o liste olan elemanı reverse ile tersine çevirerek,günceller(inplace)
            for j in range(len(liste[i])): #sonra tersine çevrilmiş liste olan elaman içerisinde tek tek gezilir
                if type(liste[i][j]) == type(list()): #eğer yine bir listeye denk gelirse
                    ListeyiTersineCevirenFonksiyon(liste[i][j]) #bu kez o liste olan elamanı tekrar aynı fonksiyona yollanır.
                else: #değilse herhangi bir işlem yapmaz
                    continue
        else:#değilse herhangi bir işlem yapmaz
            continue
    liste.reverse() #ve en son olarak listenin tamamını reverse(tersine çevirme) işlemi uygulanarak güncellenir(inplace)

if __name__ == '__main__':
    print ("Soru 1: Bir listeyi düzleştiren (flatten) fonksiyon yazın.")
    liste=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    print("Düzlestirilcek Liste:",end="")
    print(liste)
    ListeyiDuzlestirenFonksiyon(liste)
    print("Düzlestirilcek Liste:", end="")
    print(duzlestirilmisListe)
    #####################################################################################
    print("\n")
    print("Soru 2: Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.")
    liste2=[[1, 2], [3, 4], [5, 6, 7]]
    print("Tersine Cevrilcek Liste:", end="")
    print(liste2)
    ListeyiTersineCevirenFonksiyon(liste2)
    print("Tersine Cevrilmis Liste:", end="")
    print(liste2)


