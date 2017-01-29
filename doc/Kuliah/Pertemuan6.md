**PENDAHULUAN**

**Latar Belakang:**

- Apa itu Map Proxy?
- Apa itu Map Server?
- Bagaimana cara install Map Proxy?
- Bagaimana cara install Map Server?

**ISI:**

Map Server adalah sebuah lingkungan pengembangan open source untuk membangun aplikasi internet spasial diaktifkan. Hal ini dapat dijalankan sebagai program CGI atau melalui Mapscript yang mendukung beberapa bahasa pemrograman (menggunakan SWIG). MapServer dikembangkan oleh University of Minnesota - jadi, sering dan lebih khusus disebut sebagai &quot;UMN MapServer&quot;, untuk membedakannya dari komersial &quot;peta server&quot;. MapServer awalnya dikembangkan dengan dukungan dari NASA, yang membutuhkan cara untuk membuat citra satelit yang tersedia untuk umum.

Map Proxy (mapproxy.org) adalah open source ubin geospasial proxy yang mendukung proyeksi ulang. Awalnya dikembangkan oleh Omniscale Mapproxy adalah server proxy python untuk gambar geospasial. Hal ini dapat membaca data dari WMS, ubin, mapserver dan mapnik, dan cache dan melayani data bahwa sebagai WMS, WMTS, TMS dan KML. Hal ini juga dapat melakukan reprojections antara berbagai sistem koordinat referensi

Cara Installasi Map server &amp; map proxy di Ubuntu:

1. Persiapkan terlebih dahulu sistem operasi ubuntu (bisa menggunakan versi linux yang lain, karena perintahnya kurang lebih sama).
2. Buka terminal kemudian masukkan perintah :
sudo apt-get install cgi-mapserver
3. Untuk mengetahui struktur direktori Map Server, gunakan perintah :
dpkg -L cgi-mapserver
4. Karena saya mengeksekusinya menggunakan python, install python juga dengan perintah :
sudo apt-get install python-pip python-dev
5. Kemudian install uwsgi, dengan perintah :
sudo pip install uwsgi
6. Kemudian install Map Proxy, dengan perintah :
sudo pip install MapProxy

**PENUTUP**

**Kesimpulan:**

Pada kali ini kita bisa mengetahui bagaimana cara menginstall map proxy dan map server di ubuntu.

**Saran:**

Sebaiknya lebih diperdalam untuk mempelajari tentang map server dan map proxy.