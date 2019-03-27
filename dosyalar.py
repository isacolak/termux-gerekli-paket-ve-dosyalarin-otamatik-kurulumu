import os
import time

print ('')
g = str(input("\033[1;93mGiriş Scrip'i Kurulsun mu? (e/h)"))

if g=='e':
        print ('')
        print ("Giriş Script'i Yükleniyor.")
        time.sleep(0.5)
        print ('')
        print ('Lütfen Bekle ...')
        time.sleep(0.5)
        print ('')
        os.system('git clone https://github.com/isacolak/giris-scripti')
        time.sleep(2)

print ('')
m = str(input("\033[1;93mMetasploit2 Kurulsun mu? (e/h)"))

if m=='e':
        print ('')
        print ("Metasploit-2 Yükleniyor.")
        time.sleep(0.5)
        print ('')
        print ('Lütfen Bekle ...')
        time.sleep(0.5)
        print ('')
        os.system('git clone https://github.com/Bhai4You/Metasploit-2')
        time.sleep(2)

print ('')
d = str(input("\033[1;93mDarkFly Tool Kurulsun mu? (e/h)"))

if d=='e':
        print ('')
        print ("DarkFly Tool Yükleniyor.")
        time.sleep(0.5)
        print ('')
        print ('Lütfen Bekle ...')
        time.sleep(0.5)
        print ('')
        os.system('git clone https://github.com/Ranginang67/DarkFly-Tool')
        time.sleep(2)