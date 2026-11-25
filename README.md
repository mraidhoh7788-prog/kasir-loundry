# Sistem Kasir Laundry (Python OOP)

**Nama:** M RAIDHO HERDIANSYAH
**NIM:** 14012500069

## Fitur Utama
- Menampilkan daftar paket layanan laundry beserta harga per kilogram.
- Pembuatan transaksi baru dengan perhitungan total harga otomatis.
- Diskon otomatis 10% untuk cucian dengan berat minimal 10 kg.
- Pencetakan struk transaksi langsung di terminal.
- Rekap riwayat transaksi dan total pendapatan harian.

## Konsep OOP yang Diterapkan
- **Class & Object**: Pemisahan entitas `Layanan`, `Transaksi`, dan `SistemKasir`.
- **Encapsulation & Methods**: Perhitungan harga dan formatting struk dienkapsulasi di dalam class `Transaksi`.
- **Composition**: Class `SistemKasir` mengelola koleksi objek dari `Layanan` dan `Transaksi`.

## Cara Menjalankan
1. Pastikan Python 3.10+ sudah terinstal di komputer Anda.
2. Clone repositori ini:
   ```bash
   git clone [https://github.com/username-anda/kasir-laundry-oop.git](https://github.com/username-anda/kasir-laundry-oop.git)
