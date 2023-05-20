import numpy as np
import random

n = 10 #popilasyon sayisi
m = 2 #popilasyon boyutu
alt_sinir = -5 #parametre alt degerleri
ust_sinir = 5 #parametre ust degerleri

delta = 0.05 #mutasyon komsuluk buyuklugu
iterasyon = 2500
rc = 0.9 #caprazlama orani
rm = 0.08 #mutasyon orani 


popilasyon_başlangıc = np.zeros((n,m))
popilasyon_0 = np.zeros((n,m))
popilasyon_1 = np.zeros((n,m))
popilasyon_2 = np.zeros((n,m))
popilasyon_3 = np.zeros((n,m))


fd = np.zeros((n,1))
fitnes_olasılık = np.zeros((n,1))

#Belirlenen sınırlarda rastgele popilasyon oluşturur
def popilasyon_olustur():
    global popilasyon_başlangıc
    for i in range(n):
        for j in range(m):
            popilasyon_0[i][j] = (random.uniform(alt_sinir,ust_sinir))
    popilasyon_başlangıc = popilasyon_0.copy() 
    
#Fitness Datasını oluşturur
#İşleme göre tüm elemanlar uygunluk değeri alır
#Bu değer ne kadar düşük olurs o kadar uyumludur
def fitness_function():
    for i in range(n):
        fd[i][0] = abs(popilasyon_0[i][0]**3 + popilasyon_0[i][1] -16)


def seleksiyon():
    #fitness değerlerine göre 0-100 değerleri arsı rulet çarkı oluşturur
    #fitness değeri düşük olanların daha yüksek seçilme oranı olacak şekilde rulet çarkı oluşturulur
    fitnes_tpl = 0
    for i in range(n):
        fitnes_tpl = (1/fd[i]) + fitnes_tpl

    for i in range(n):
        fitnes_olasılık[i][0] = (100 * (1 / fd[i]) ) / fitnes_tpl

    for i in range(1,n):
        fitnes_olasılık[i] = (fitnes_olasılık[i-1] + fitnes_olasılık[i])
    
    #0-100 arası raskele değer seçilir ve çarktaki bu değere denk gelen sayı bi sonraki popilasyona aktarılır
    for i in range(n):
        rast = random.uniform(0, 100) 
        for j in range(n):
            if fitnes_olasılık[j][0] >= rast :
                for k in range(m):
                    popilasyon_1[i][k]= popilasyon_0[j][k]
                break

#hayatta kalan genler çapraszlanır
def caprazlama():
    for i in range(0,n,2):
        rast = random.random()
        if rc > rast:
            popilasyon_2[i][0] = popilasyon_1[i+1][0]
            popilasyon_2[i][1] = popilasyon_1[i][1]
            
            popilasyon_2[i+1][0] = popilasyon_1[i][0]
            popilasyon_2[i+1][1] = popilasyon_1[i+1][1]
            
        else:
            popilasyon_2[i][0]=popilasyon_1[i][0]
            popilasyon_2[i][1]=popilasyon_1[i][1]
            
            popilasyon_2[i+1][0]=popilasyon_1[i+1][0]
            popilasyon_2[i+1][1]=popilasyon_1[i+1][1]

#çeşitliliği korumak için mutasyon gerçekleştirilir
def mutasyon():
    global popilasyon_0
    for i in range(n):
        for j in range(m):
            rast_0 = random.random()
            
            #butasyon olasılığından geçen genler -3 ile 3 arasında bir sayı ile toplanır
            if rm > rast_0:
                rast_1 = random.uniform(-3, 3)
                mutasyon_birey = popilasyon_2[i][j] + rast_1
                
                #eğer yeni oluşan gen eşik değerlerini geçerse bu değerlere eşitlenir
                if mutasyon_birey < 5 and mutasyon_birey > -5:
                    popilasyon_3[i][j] = mutasyon_birey
                    
                elif mutasyon_birey < 5:
                    popilasyon_3[i][j] = 5
                    
                else:
                    popilasyon_3[i][j] = -5
                    
            else:
                popilasyon_3[i][j] = popilasyon_2[i][j]
                
    popilasyon_0 = popilasyon_3.copy()
      
#Fonksiyonlar itereasyon miktarınca çalıştırılır          
popilasyon_olustur()
for i in range(iterasyon):
    fitness_function()
    seleksiyon()
    caprazlama()
    mutasyon()
fitness_function()