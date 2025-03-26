Pada program sederhana yang dibuat ini mengimplementasikan konsep:
1. Struktur kontrol, yang mana menggunakan:
   - percabangan if else, di mana digunakan untuk menangani menu.
   - perulangan for, di mana digunakan untuk menampilkan list tugas.
   - perulangan while, di mana digunakan untuk menjalankan menu utama secara secara terus menerus hingga _user_ memilih opsi keluar.
   - kontrol perulangan break
   - dua function, yaitu:
     - built-in function
       - print(...) 
     - user-defined function
       - tambahTask(...): di mana ini merupakan fungsi untuk menambahkan tugas, dengan membuat dictionary tugas **(dataTask)** menggunakan id, task, & data_added, yang kemudian menambahkan dictionary tersebut ke dalam list **tasks**, lalu akan menampilkan pesan sukes setelah tugas ditambahkan.
       - lihatTasks(): di mana ini merupakan fungsi untuk menampilkan daftar tugas, dengan mengecek dulu apakah **tasks** kosong, setelah itu, jika iya maka akan menampilkan pesan, sedangkan jika tidak, maka akan melakukan iterasi setiap tugas dalam **tasks**, kemudian cetak detail tugas.
       - hapusTask(...): di mana ini merupakan fungsi untuk menghapus tugas, dengan mencari tugas berdasarkan ID di dalam **tasks** terlebih dulu, kemudian jika ditemukan, maka akan di_remove_ dari list, sedangkan jika tidak, maka akan menampilkan pesan.
2. Struktur Data, yang mana menggunakan:
   - list, di mana digunakan untuk menyimpan tugas dalam bentuk dictionary:
      (tasks = []), di mana tasks adalah list kosong untuk menyimpan semua tugas yang telah ditambahkan oleh _user_.
    - dictionary, di mana digunakan untuk menyimpan data dalam bentuk pasangan key: value, yang ciri-cirinya menggunakan kurung kurawal.
3. Library, yang mana menggunakan:
   - import random, untuk membuat ID yang unik untuk setiap tugas
   - import datetime, untuk mencatat waktu ketika tugas ditambahkan

Pada program ini memungkinkan _user_ untuk:
1. Menambahkan tugas
2. Melihat daftar tugas
3. Menghapus tugas berdasarkan ID
4. keluar dari program

Penjelasan singkat mengenai _source code_ pada program ini sebagai berikut:
1. Mengimpor library
2. Membuat struktur data "tasks = []" untuk menyimpan tugas
3. Membuat fungsi, seperti tambahTask untuk menambahkan tugas, lihatTasks untuk melihat daftar tugas, dan hapusTask untuk menghapus tugas berdasarkan ID
4. Membuat program utama, yang mana akan menampilan menu utama yang meminta _user_ untuk memilih opsi. Jika _user_ memilih 1, maka akan diminta memasukkan naam tugas, lalu fungsi **tambahTask(namaTaasks)** dipanggil. Jika _user_ memilih 2, maka fungsi **lihatTasks()** akan dipanggil untuk menampilkan daftar tugas. Jika _user_ memilih 3, maka _user_ diharuskan memasukkan ID tugas yang ingin dihapus. Jika _user_ memilih 4, maka program akan menampilkan pesan "Terima kasih!" dan keluar dari loop. Jika _user_ memilih menu yang tidak valid, maka program akan menampilkan pesan error.
