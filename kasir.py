from models import Layanan, Transaksi

class SistemKasir:
    """Class utama untuk mengelola operasional kasir laundry."""
    def __init__(self):
        self.daftar_layanan = {
            "1": Layanan("1", "Cuci Kering Reguler", 6000),
            "2": Layanan("2", "Cuci Setrika Reguler", 8000),
            "3": Layanan("3", "Cuci Setrika Express (1 Hari)", 12000),
            "4": Layanan("4", "Setrika Saja", 5000)
        }
        self.riwayat_transaksi = []

    def tampilkan_layanan(self):
        print("\n--- DAFTAR LAYANAN LAUNDRY ---")
        for layanan in self.daftar_layanan.values():
            print(layanan)
        print("*Promo: Diskon 10% untuk cucian >= 10 kg")

    def buat_transaksi(self, nama_pelanggan: str, kode_layanan: str, berat_kg: float) -> Transaksi | None:
        if kode_layanan not in self.daftar_layanan:
            print("Error: Kode layanan tidak valid!")
            return None
        if berat_kg <= 0:
            print("Error: Berat cucian harus lebih dari 0 kg!")
            return None

        id_trx = f"TRX-{len(self.riwayat_transaksi) + 1:03d}"
        layanan_terpilih = self.daftar_layanan[kode_layanan]
        
        transaksi_baru = Transaksi(id_trx, nama_pelanggan, layanan_terpilih, berat_kg)
        self.riwayat_transaksi.append(transaksi_baru)
        return transaksi_baru

    def tampilkan_riwayat(self):
        print("\n--- RIWAYAT TRANSAKSI ---")
        if not self.riwayat_transaksi:
            print("Belum ada transaksi hari ini.")
            return
        
        total_pendapatan = 0
        for trx in self.riwayat_transaksi:
            print(f"{trx.id_transaksi} | {trx.tanggal} | {trx.nama_pelanggan} | {trx.layanan.nama} ({trx.berat_kg} kg) -> Rp{trx.total_harga:,.0f}")
            total_pendapatan += trx.total_harga
        
        print("-" * 50)
        print(f"Total Pendapatan: Rp{total_pendapatan:,.0f}")
