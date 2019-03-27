mv /data/data/com.termux/files/home/termux-gerekli-paket-ve-dosyalarin-otamatik-kurulumu/termux-otamatik-paket-ve-dosya-kurulumu.py /data/data/com.termux/files/home/
mv /data/data/com.termux/files/home/termux-gerekli-paket-ve-dosyalarin-otamatik-kurulumu/dosyalar.py /data/data/com.termux/files/home/
mv /data/data/com.termux/files/home/termux-gerekli-paket-ve-dosyalarin-otamatik-kurulumu/install.sh /data/data/com.termux/files/home/

pkg install python
python /data/data/com.termux/files/home/termux-otamatik-paket-ve-dosya-kurulumu.py

mv /data/data/com.termux/files/home/termux-gerekli-paket-ve-dosyalarin-otamatik-kurulumu/Metasploit-2 /data/data/com.termux/files/home/
mv /data/data/com.termux/files/home/termux-gerekli-paket-ve-dosyalarin-otamatik-kurulumu/DarkFly-Tool /data/data/com.termux/files/home/
mv /data/data/com.termux/files/home/termux-gerekli-paket-ve-dosyalarin-otamatik-kurulumu/giris-scripti /data/data/com.termux/files/home/

rm -r /data/data/com.termux/files/home/install.sh
rm -r /data/data/com.termux/files/home/dosyalar.py
rm -r /data/data/com.termux/files/home/termux-otamatik-paket-ve-dosya-kurulumu.py
rm -rf /data/data/com.termux/files/home/termux-gerekli-paket-ve-dosyalarin-otamatik-kurulumu
