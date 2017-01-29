**PENDAHULUAN**

**Latar Belakang:**

Penggunaan Google Maps saat ini sangatlah bermanfaat,baik itu untuk menemukan sebuah daerah,jalan,bangunan,tempat dan lain-lain.Namun apakah anda terbayang untuk dapat membuat &quot;Google Maps&quot; kita sendiri?

**ISI:**

Jalankan Map Proxy dan Map Server di ubuntu,caranya adalah:

1. Untuk meload data geospasial, kita perlu menyiapkannya dulu agar akan ditampilkan nantinya di Map Proxy. Kalian bisa mendownload data geospasial di situs ini,
 [http://www.halaman.download/](http://www.halaman.download/) ,kemudian pilih &quot;Producer&quot; dan klik &quot;Indonesia Mapproxy&quot;.
2. Jika sudah download ekstrak file tersebut (Penting!! Ketahui dimana anda mengekstrak file tersebut, karena path-nya akan digunakan untuk mengedit file yang ada di direktori yang telah di ekstrak tersebut.
Disini saya simpan di direktori Downloads (Huruf kecil dan besar di perhatikan.)
3. Pada file indomap -&gt; mapproxy, akan terdapat 3 file. Buka file agm.yaml
4. Pada file agm.yaml, edit beberapa baris ini sesuai dengan direktori tempat anda menyimpan file tersebut :
- pada baris
binary: /usr/libexec/mapserver
ubah menjadi
binary: /usr/lib/cgi-bin/mapserv
- pada baris
map: var/mapdata/mapfile/indo.map
ubah menjadi
map: /home/ali/Downloads/indomap/mapfile/indo.map
- Kemudian direktori baru dengan nama tmp pada direktori indomap
ubah baris
working\_dir: /var/mapdata/tmp
menjadi
/home/ali/Downloads/indomap/tmp
Kemudian Save
5. Kemudian pada direktori mapproxy(di terminal/cmd), gunakan perintah :
vi mapproxy.ini
edit baris
chdir = /var/mymapproxy/
menjadi
chdir = /home/ali/Downloads/indomap/mapproxy
Kemudian Save
6. Edit file config.py pada direktori mapproxy
ubah
application = make\_wsgi\_app(r&#39;/var/mymapproxy/agm.yaml&#39;)
menjadi
application = make\_wsgi\_app(r&#39;/home/ali/Downloads/indomap/mapproxy/agm.yaml&#39;)
7. Untuk menjalankan programnya gunakan perintah
uwsgi mapproxy.ini
8. Untuk mengecek apakah mapproxy sudah terinsall atau belum, buka browser kemudian ketik localhost:8080
9. Klik demo atau ketik localhost:8080/demo
10. Pada bagian WMTS klik di bawah Image Format yaitu png
11. Tunggu beberapa saat karna datanya sedang di load.
12. Map Peta akan muncul

**PENUTUP**

**Kesimpulan**
jadi pada pertemuan kali ini ,kita tau bagaimana cara menjalankan map server dan map proxy di ubuntu.

**Saran**

Alangkah baiknya dipelajari lebih dalam agar semakin paham cara kerja map server dan map proxy.