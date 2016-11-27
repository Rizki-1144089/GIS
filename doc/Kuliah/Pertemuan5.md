**PENDAHULUAN**

**Latar Belakang**

- Cara Membuat Data Geospasial
- Editing Data Geospasial

**ISI**

**   A. **   **Cara Membuat Data Geospasial**

Pembuatan data geospasial ini menggunakan libarary pyshp. Untuk membuat data geospasial diperlukan file namafile.shp beserta namafile.dbf.

Adapun langkahnya adalah sebagai berikut:

a.       Import shapefile

b.      Instansiasi writer method

Sf = shapefile.Writer(param)

Dimana param adalah pilih shapetype:

1.       shapeType = 1

2.       shapeType = 3

3.       shapeType = 5

c.       Sama seperti read, kita lakukan metode dbf dan shp.

-          Shapefile (shp)

Untuk menambahkan record tergantung dengan type ESRInya.

 1.  sf.point (x,y)

 3. sf.line = (parts: [[x,y],[z,w],...])

6.  sf.poly = (parts: [[x,y],[z,w],...])

-          Databasefile (dbf)

Tahapannya adalah sebagi berikut:

a.         Membuat atribut dahulu kemudian menambahkan record.

Contoh:

sf.field (&#39;Nama Filed&#39;,&#39;C&#39;,&#39;40&#39;)

Dimana C adalah Character, dan 40 adalah length. Dalam arti nama atribut, nama field dengan panjang 40 karakter.

b.        Tambahkan record dibawah ini

sf.record(&#39;Bandung&#39;)

sf.record(&#39;Bandung&#39;,&#39;Sarijadi&#39;)

c.         Setelah selesai maka simpan, dengan perintah:

sf.save(&#39;namafile.shp&#39;)

**   B. EDITING DATA GEOSPASIAL**

Adapun dalam editing data geospasial hampir sama dengan langkah-langkah membuat data geospasial, yang membedakan adalah:

**sf = shapefile.Writer(param)**

diganti dengan

**sf = shapefile.Editor(param)**

dimana param adalah nama letak file.

Adapun operasi dalam editing pada shp dan dbf sama saja.

| **shp** | **dbf** |
| --- | --- |
| **sf.poly()****sf.line()****sf.point()** | **sf.record()** |
| **sf.delete(n), dimana n adalah baris ke-n dari tabel** |

Dan jika sudah selesai, simpan dengan perintah:

Sf.save(&#39;namafile&#39;)

**PENUTUP**

**Kesimpulan**

Jadi, untuk membuat dan mengedit data geospasial langkah-langkahnya hampir sama. Yang membedakan adalah method yang digunakan. Metgod yang digunakan untuk membuat data geospasial adalah WRITE sedangankan untuk mengedit adalah EDITOR.

**Saran**

Adapun sarannya yaitu untuk memahami lebih lanjut dan lebih rinci tentang cara membuat dan mengedit data geospasial, bisa kita praktekan secara langsung menggunakan bahasa pemrograman python. Hal tesebut harus dicoba guna untuk mengetes langkah-langkah di atas berhasil atau tidak.