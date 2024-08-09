#!/usr/bin/env/python3
# This Python file uses the following encoding: utf-8

from __future__ import print_function
import sys
import time
from googlesearch import search

class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"

def animate_loading():
    frames = [
        '🐇    ',
        ' 🐇   ',
        '  🐇  ',
        '   🐇 ',
        '    🐇'
    ]
    for _ in range(3):  
        for frame in frames:
            sys.stdout.write('\r' + frame)
            sys.stdout.flush()
            time.sleep(0.2)
    sys.stdout.write('\r' + ' ' * len(frames[-1]) + '\n')  

try:
    data = input("\n[+] Dosyayı kaydetmek ister misiniz? (E/H) ").strip()
    l0g = ("")
except KeyboardInterrupt:
    print("\n")
    print("\033[1;91m[!] Çıkış yapıldı! \033[0m")
    time.sleep(0.5)
    print("\n\n\t\033[1;91m[!] İyi çalışmalar dilerim, 😃\n\n")
    time.sleep(0.5)
    sys.exit(1)

def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()

if data.lower().startswith("e"):
    l0g = input("[~] Dosyaya bir isim verin: ")
    print("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print("[!] Kaydetme atlandı...")
    print("\n" + "  " + "»" * 78 + "\n")

def read_dorks(file_path):
    with open(file_path, 'r') as file:
        dorks = file.read().splitlines()
    return dorks

def dorks():
    try:
        domain = input("\n[+] Alan adını girin: ")
        print("\nDork Tipini Seçin:")
        print("1. Genel Bilgiler")
        print("2. Alan Adına Yönelik Aramalar")
        print("3. Email ve Kimlik Bilgileri")
        print("4. Dosya ve Dizin Aramaları")
        print("5. Diğer Alan Adları Üzerinden Aramalar")
        print("6. Özel Arama Kombinasyonları")
        
        choice = input("\n[+] Seçiminizi Girin: ").strip()
        
        amount = input("[+] Gösterilecek Web Sitesi Sayısını Girin: ")
        print("\n ")
        
        animate_loading()  
        
        dork_list = read_dorks('dorks.txt')
        
        dork_type = {
            "1": slice(0, 5),
            "2": slice(5, 13),
            "3": slice(13, 20),
            "4": slice(20, 28),
            "5": slice(28, 33),
            "6": slice(33, None)
        }

        selected_dorks = dork_list[dork_type[choice]]
        requ = 0
        counter = 0
        found = False

        for dork in selected_dorks:
            query = f'{dork} site:{domain}'
            for results in search(query, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
                counter += 1
                print("[+] ", counter, results)
                time.sleep(0.1)
                requ += 1
                found = True
                if requ >= int(amount):
                    break

                data = (counter, results)
                logger(data)
                time.sleep(0.1)
        
        if not found:
            print("\nBulgu bulunamadı.")

    except KeyboardInterrupt:
        print("\n")
        print("\033[1;91m[!] Kullanıcı Kesintisi Algılandı..!\033[0m")
        time.sleep(0.5)
        print("\n\n\t\033[1;91m[!] İyi çalışmalar dilerim, 😃\n\n")
        time.sleep(0.5)
        sys.exit(1)

    print("[•] Tamamlandı... Çıkılıyor...")
    print("\n\t\t\t\t\033[34mLastDork\033[0m")
    print("\t\t\033[1;91m[!] İyi çalışmalar dilerim, 😃\n\n")
    sys.exit()

if __name__ == "__main__":
    dorks()
