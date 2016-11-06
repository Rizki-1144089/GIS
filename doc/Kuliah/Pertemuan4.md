Latar Belakang:
Apa itu Retrieve Data?
Apa itu Shapefile?
Apa itu Geometri?
Bagaimana Operasi Pengambilan Data?
Buatlah Class Geospatial Editor?
Buat Method Select, Where Negara?

Isi:
Retrieve Data adalah Meretrieve/Membaca Data, kali ini kita akan membaca data vektor yaitu data shapefile.Operasi Retrieve data pada kali ini menggunakan library python yang bernama pyshp
Shapefile (ESRI Shapefile) adalah sebuah format data vektor dalam geospasial,format data ini yang lebih populer di data vektor.Format data ini dikembangkan oleh perusahaan ESRI.Shapefile dibagi menjadi 2 yaitu data geometri(.shp) dan tabel basis data(.dbf).
Geometri merupakan data kordinat yang membentuk bangun datar atau bangun ruang,diantaranya adalah:
Point/titik [1]
Line/garis [3] Shape type
Polygon [5]
Operasi Pengambilan Data
Library pyshp class shapefile
Buka/baca


Method DBF:
Fields
Record(n)
Record (n) baris ke (n) records

Method SHP:
Shapes() = menampilkan semuanya
Shape(n) = Menampilkan dengan sebuah parameter
Bbox = batas view peta
Parts = menentukan apakah record ini bagian dari record lain atau pecahan relasi
Points = kordinat pembentukan peta
Shape type = jenis geometri dari points
Praktek:
Membuat Class Geospasial editor 
Buatlah file tugas.py dengan berisikan code sebagai berikut:
--gambar---
Membuat Method Select, Where Negara dengan parameter Indonesia
(arahkan ke lokasi file negara.shp anda)
--gambar—
Outputnya adalah Data Record Negara Indonesia

Penutup:
Kesimpulan:Disini kita membuat sebuah Class kemudian Method dengan parameter untuk menampilkan data record Negara Indonesia.
Saran:Harus lebih sering dipraktekkan dikelas maupun di rumah masing-masing agar dapat memperdalam materi ini.