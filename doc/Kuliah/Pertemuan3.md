Latar Belakang:
1. Apa saja 4 jenis manipulasi data?
2. Apa itu shapefile?
3. Bagaimana menghitung jumlah record pada file .shp menggunakan python?

Isi:
Ada 4 jenis manipulasi data yaitu:
•	Create = Membuat data baru
•	Retrieve/Read = Membaca atau Menampilkan data
•	Update = Mengedit atau Merubah data
•	Delete = Menghapus data
Shapefile (ESRI Shapefile) adalah sebuah format data vektor dalam geospasial,format data ini yang lebih populer di data vektor.Format data ini dikembangkan oleh perusahaan ESRI.
Cara Menghitung jumlah record dari File .shp menggunakan python
1.	Install Python terlebih dahulu
2.	Install PIP di python 
3.	Buka cmd lalu ketik: Python –m pip install pyshp ,lalu enter
4.	Kemudian upgrade pip dengan mengetikkan di cmd: Python –m pip install - -upgrade pip ,lalu enter
5.	Lalu masuk ke python
6.	Ketikkan script berikut:
import shapefile  ,klik enter
f = shapefile.Reader("lokasi file .shp") ,klik enter
shapes = f.shapes()  ,klik enter
print len (shapes)
7.	Lalu klik enter,maka akan keluar hasil nya,disini kita menghitung jumlah record yang ada di dalam file .shp
Membuka file shapefile juga dapat kita lakukan dengan membuat file .py(python),dimana didalam file .py berisikan script untuk membuka file .shp sama seperti script di atas.
Penutup:
Kesimpulan:
Dengan script diatas kita dapat mengetahui jumlah record yang ada pada file shp yang kita buka
Saran:
Sebaiknya langsung dipraktekkan dan dipahami ,atau bisa dibandingkan dengan membuka file shp tersebut menggunakan QGIS.

