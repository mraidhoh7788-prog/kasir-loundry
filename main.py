from kasir import SistemKasir

def main():
    kasir = SistemKasir()

    while True:
        print("\n=== APLIKASI KASIR LAUNDRY ===")
        print("1. Lihat Daftar Layanan")
        print("2. Buat Transaksi Baru")
        print("3. Lihat Riwayat & Pendapatan")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            kasir.tampilkan_layanan()
        
        elif pilihan == "2":
            kasir.tampilkan_layanan()
            nama = input("\nMasukkan nama pelanggan : ").strip()
            kode = input("Pilih kode layanan (1-4): ").strip()
            try:
                berat = float(input("Masukkan berat (kg)     : "))
                trx = kasir.buat_transaksi(nama, kode, berat)
                if trx:
                    trx.cetak_struk()
            except ValueError:
                print("Error: Input berat harus berupa angka!")

        elif pilihan == "3":
            kasir.tampilkan_riwayat()

        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi Kasir Laundry.")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
