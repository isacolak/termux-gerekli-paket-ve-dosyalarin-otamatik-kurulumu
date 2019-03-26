import os
import time

g = str(input("\033[1;93mGiriş Scrip'i Kurulsun mu? (e/h) \033[1;91m: "))

if g=='e':
	print ('')
        print ("Giriş Script'i Yükleniyor.")
        time.sleep(0.5)
        print ('')
        print ('Lütfen Bekle ...')
        time.sleep(0.5)
        os.system('git clone https://github.com/isacolak/giris-scripti')
	time.sleep(2)

m = str(input("\033[1;93mMetasploit2 Kurulsun mu? (e/h) \033[1;91m: "))

if m=='e':
	print ('')
        print ("Metasploit-2 Yükleniyor.")
        time.sleep(0.5)
        print ('')
        print ('Lütfen Bekle ...')
        time.sleep(0.5)
        os.system('git clone https://github.com/Bhai4You/Metasploit-2')
	time.sleep(2)

d = str(input("\033[1;93mDarkFly Tool Kurulsun mu? (e/h) \033[1;91m: "))

if g=='e':
	print ('')
        print ("DarkFly Tool Yükleniyor.")
        time.sleep(0.5)
        print ('')
        print ('Lütfen Bekle ...')
        time.sleep(0.5)
        os.system('git clone https://github.com/Ranginang67/DarkFly-Tool')
        time.sleep(2)

b = str(input("\033[1;93mÖzelleştirilmiş bash Yüklensin mi? (e/h) \033[1;91m: "))

if g=='e':
	print ('')
        print ("Özelleştirilmiş bash Yükleniyor.")
        time.sleep(0.5)
        print ('')
        print ('Lütfen Bekle ...')
        time.sleep(0.5)
        os.system('rm -r /data/data/com.termux/files/usr/etc/bash.bashrc')
        os.sysyem('mv /data/data/com.termux/files/home/termux-gerekli-paket-ve-dosyalarin-otamatik-kurulumu/bash.bashrc /data/data/com.termux/files/usr/etc')
        os.system('rm -r /data/data/com.termux/files/usr/etc/motd')
        os.system('mv /data/data/com.termux/files/home/termux-gerekli-paket-ve-dosyalarin-otamatik-kurulumu/motd /data/data/com.termux/files/usr/etc')
