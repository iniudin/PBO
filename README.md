# PBO - MyHotel
Repository untuk PBO - MyHotel

## Requirements
Sebelum menjalankan program pastikan anda telah menginstall beberapa requirements dibawah ini:

- [Python 3.8.5](https://python.org) - bahasa yang digunakan.  
- [XAMPP](https://www.apachefriends.org/download.html) - Untuk database menggunakan mysql/mariadb.  
- dan beberapa module yang dapat diinstall menggunakan pip dengan cara:  
`python3 -m pip install -r requirements.txt`  
- Kemudian import database `pbomyhotel.sql` dengan nama database yang sama `pbomyhotel`  
## Structure
```raw
.
├── app
│   ├── database
│   │   └── connection.py
│   ├── functions.py
│   ├── __init__.py
│   ├── models
│   │   ├── auth.py
│   │   ├── bills.py
│   │   ├── __init__.py
│   │   ├── reservations.py
│   │   ├── rooms.py
│   │   └── users.py
│   └── views
│       ├── bills.py
│       ├── customers.py
│       ├── employees.py
│       ├── __init__.py
│       ├── reservations.py
│       └── rooms.py
├── main.py
├── pbomyhotel.sql
├── README.md
└── requirements.txt
```

## Features
Berikut adalah fiture program yang akan di implementasikan pada project ini:
- [x] Management Karyawan 
- [x] Management Pelanggan 
- [x] Management Kamar 
- [x] Reservasi 
- [x] Catatan Transaksi
