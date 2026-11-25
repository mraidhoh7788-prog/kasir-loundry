from datetime import datetime

class Layanan:
    """Class untuk merepresentasikan jenis layanan laundry."""
    def __init__(self, kode: str, nama: str, harga_per_kg: int):
        self.kode = kode
        self.nama = nama
        self.harga_per_kg = harga_per_kg

    def __str__(self):
        return f"[{self.kode}] {self.nama} - Rp{self.harga_per_kg:,}/kg"


class Transaksi:
    """Class untuk merepresentasikan satu struk transaksi pelanggan."""
    def __init__(self, id_transaksi: str, nama_pelanggan: str, layanan: Layanan, berat_kg: float):
        self.id_transaksi = id_transaksi
        self.nama_pelanggan = nama_pelanggan
        self.layanan = layanan
        self.berat_kg = berat_kg
        self.tanggal = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.total_harga = self.hitung_total()

    def hitung_total(self) -> float:
        """Menghitung total biaya dengan diskon otomatis jika berat >= 10 kg."""
        subtotal = self.layanan.harga_per_kg * self.berat_kg
        if self.berat_kg >= 10:
            return subtotal * 0.90  # Diskon 10%
        return subtotal

    def cetak_struk(self):
        print("\n" + "=" * 35)
        print("        STRUK KASIR LAUNDRY        ")
        print("=" * 35)
        print(f"ID Transaksi : {self.id_transaksi}")
        print(f"Tanggal      : {self.tanggal}")
        print(f"Pelanggan    : {self.nama_pelanggan}")
        print(f"Layanan      : {self.layanan.nama}")
        print(f"Berat        : {self.berat_kg} kg")
        if self.berat_kg >= 10:
            print("Diskon       : 10% (Min. 10 kg)")
        print("-" * 35)
        print(f"TOTAL BAYAR  : Rp{self.total_harga:,.0f}")
        print("=" * 35 + "\n")
