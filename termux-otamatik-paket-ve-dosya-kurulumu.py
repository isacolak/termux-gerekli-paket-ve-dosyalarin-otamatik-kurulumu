import os
import time

os.system('cd')
os.system('clear')
print ("\033[1;93m  <───────[ Hoş Geldin ]───────>")
time.sleep(0.5)
print ('')
print ("Bu Program Termux'da Gerekli Olan Paketleri ve Dosyaları Otamatik Yükler.")
time.sleep(1)
print ('')

print ('Python Yükleniyor.')
time.sleep(0.5)
print ('')
print ('Lütfen Bekle ...')
time.sleep(0.5)
os.system('pkg install python -y')

print ('Python2 Yükleniyor.')
time.sleep(0.5)
print ('')
print ('Lütfen Bekle ...')
time.sleep(0.5)
os.system('pkg install python2 -y')

print ('Github Yükleniyor.')
time.sleep(0.5)
print ('')
print ('Lütfen Bekle ...')
time.sleep(0.5)
os.system('pkg install git -y')

print ('Nano Yükleniyor.')
time.sleep(0.5)
print ('')
print ('Lütfen Bekle ...')
time.sleep(0.5)
os.system('pkg install nano -y')

print ('Curl Yükleniyor.')
time.sleep(0.5)
print ('')
print ('Lütfen Bekle ...')
time.sleep(0.5)
os.system('pkg install curl -y')

g = str(input("\033[1;93mGiriş Scrip'i Kurulsun mu? (e/h) \033[1;91m: "))

if g=='e':
	print ("Giriş Script'i Yükleniyor.")
	time.sleep(0.5)
	print ('')
	print ('Lütfen Bekle ...')
	time.sleep(0.5)
	os.system('git clone https://github.com/isacolak/giris-scripti')
	os.system('cd giris-scripti')
	os.sysyem('chmod +x *')
	os.system('sh install.sh')
	os.system('cd')

m = str(input("\033[1;93mMetasploit2 Kurulsun mu? (e/h) \033[1;91m: "))

if m=='e':
        print ("Giriş Script'i Yükleniyor.")
        time.sleep(0.5)
        print ('')
        print ('Lütfen Bekle ...')
        time.sleep(0.5)
        os.system('git clone https://github.com/Bhai4You/Metasploit-2')
	os.system('cd Metasploit-2')
	os.system('chmod 7777 install.sh kingsploit.sh bundle.sh README.md')
	os.system('bash install.sh')
	os.system('bash bundle.sh')
	os.system('cd')

d = str(input("\033[1;93mDarkFly Tool Kurulsun mu? (e/h) \033[1;91m: "))

if g=='e':
        print ("DarkFly Tool Yükleniyor.")
        time.sleep(0.5)
        print ('')
        print ('Lütfen Bekle ...')
        time.sleep(0.5)
        os.system('git clone https://github.com/Ranginang67/DarkFly-Tool')
        os.system('cd DarkFly-Tool')
        os.sysyem('python2 install.py')
	time.sleep(2)
        os.system('cd')

b = str(input("\033[1;93mÖzelleştirilmiş bash Yüklensin mi? (e/h) \033[1;91m: "))

if g=='e':
        print ("Özelleştirilmiş bash Yükleniyor.")
        time.sleep(0.5)
        print ('')
        print ('Lütfen Bekle ...')
        time.sleep(0.5)
        os.system('rm -r /data/data/com.termux/files/usr/etc/bash.bashrc')
        os.sysyem('mv /data/data/com.termux/files/home/termux-gerekli-paket-ve-dosyalarin-otamatik-kurulumu/bash.bashrc /data/data/com.termux/files/usr/etc')
        os.system('rm -r /data/data/com.termux/files/usr/etc/motd')
	os.system('mv /data/data/com.termux/files/home/termux-gerekli-paket-ve-dosyalarin-otamatik-kurulumu/motd /data/data/com.termux/files/usr/etc/')

