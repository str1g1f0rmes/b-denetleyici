print("""
     ........          
      .****.      |             |                                     |      |
       .**.       |             |     ___      _______      ___       |      |     ___                O     _____   O
        ..        |____     ____|    /   \    |       |    /   \   ___|___   |    /   \               |    /        |
        ..        |    \___/    |   /_____\   |       |   /_____\     |      |   /_____\              |   /         |
       .  .       |    /   \    |   \         |       |   \           |      |   \         |      |   |   \         |
      . ** .      |___/     \___|    \_____   |       |    \_____     |      |    \_____   |______|   |    \_____   |
     ........                                                                                     |
                                                                                            ______|
""")


import time as t
import os
import ctypes

print("""
Kronometreyi dakika olarak mı, saat olarak mı ayarlamak istersiniz?
===================================================================
1- Dakika
2- Saat
""")

süre = input("(1/2): ")
süre_1= int(süre)


print("""
Süre bitince ne yapılmasını istersiniz?
=======================================
1- Kilitle
2- Kapat
""")

eylem = input("(1/2): ")
eylem_1= int(eylem)

if eylem_1==1:
    
    if süre_1==1:
        dakika = input("\nBilgisayar kaç dakika sonra kilitlensin?: ")
        print("\nBilgisayar "+dakika+" saat sonra kilitlenecek.")
        dakika_1 = float(dakika)*60
        t.sleep(dakika_1)
        ctypes.windll.user32.LockWorkStation()
    
    elif süre_1==2:
        saat = input("\nBilgisayar kaç saat sonra kilitlensin?: ")
        print("\nBilgisayar "+saat+" saat sonra kilitlenicek.")
        saat_1 = float(saat)*3600
        t.sleep(saat_1)
        ctypes.windll.user32.LockWorkStation()

    else:
        print("\nGirilen değer geçersizdir. Uygulama kapatılıyor.")
        exit()


elif eylem_1==2:
    
    if süre_1==1:
        dakika = input("\nBilgisayar kaç dakika sonra kapatılsın?: ")
        print("\nBilgisayar "+dakika+" dakika sonra kapatılacak.")
        dakika_1 = float(dakika)*60
        t.sleep(dakika_1)
        os.system("shutdown -s -f")
    
    elif süre_1==2:
        saat = input("\nBilgisayar kaç saat sonra kapatılsın?: ")
        print("\nBilgisayar "+saat+" saat sonra kapatılacak.")
        saat_1 = float(saat)*3600
        t.sleep(saat_1)
        os.system("shutdown -s -f")

    else:
        print("\nGirilen değer geçersizdir. Uygulama kapatılıyor.")
        exit()


else:
    print("\nGirilen değer geçersizdir. Uygulama kapatılıyor.")
    exit()