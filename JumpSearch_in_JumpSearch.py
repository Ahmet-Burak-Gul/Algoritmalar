import math
#bu jump_search fonksiyonunda oz yineleme kullanılmıştır.
dongu_sayısı=0#kaçtane işlem yaptığını hesaplamak için oluşturulan değişken.
oz_yenileme_sayısı=1#kaçıncı öz yineleme olduğunu belirtmek için oluşturulan değişken.

#jump search'ün gerçekleştirildiği fonksiyon.
def jump_search(list,search,dongu):
    global dongu_sayısı
    global oz_yenileme_sayısı
    oz_yenileme_sayısı += 1
    step = int(math.sqrt(len(list)))#jump search'te atlaması gereken adım büyüklüğü. Listenin uzunluğunun karekökünün tam sayı değeri kadar ileri atlar.
    for i in range(0,len(list),step):#step büyüklüğünde liste bitene kadar arar.
        dongu+=1
        if list[i] > search:#bulunan sayının aranan sayıdan büyük olduğu sorgulaınır. Eğer büyükse döngü sonlandırılır.
            sonadım = i
            break
        if list[i] == search:#eğer aranan sayı bulunursa bulunan sayı döndürülür.
            return i

    list_ls = list[sonadım-step:sonadım]#Aranan sayının bulunduğu aralığı yeni bir listeye atarız ve o listenin içinde o sayıyı ararız.

    print(f"{oz_yenileme_sayısı}.listenin boyutu:",len(list_ls))#kaç kere öz yineleme yaptğını görmek için ve bu öz yinemelerin herbirinde aranan listenin büyüklüğünü görmek için hazırlanan çıktı.

    if len(list_ls)<100:#aranan listenin büyüklüğü 100'den küçük ise listenin içinde istenilen sayı aranır. Değil ise liste öz yineleme ile tekrar jump search uygulanır.
        for i in list_ls:
            dongu+=1
            if i==search:
                index = [i]
    else:
        return jump_search(list_ls,search,dongu)
    dongu_sayısı=dongu
    return index[0]#son olarak bulunan sayı döndürülür.

list = [ i for i in range(1,40000001)]
print(f"{oz_yenileme_sayısı}.listenin boyutu:",len(list))
print("bulunan deger:",jump_search(list, 37215229, dongu_sayısı))
print("sorgulama sayısı:",dongu_sayısı)