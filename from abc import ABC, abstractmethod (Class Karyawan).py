from abc import ABC, abstractmethod

# Abstract class Karyawan
class Karyawan(ABC):
    @abstractmethod
    def hitung_gaji(self):
        pass

    @abstractmethod
    def deskripsi(self):
        pass

# Subclass KaryawanTetap
class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji_bulanan):
        self.nama = nama
        self.gaji_bulanan = gaji_bulanan

    def hitung_gaji(self):
        return self.gaji_bulanan

    def deskripsi(self):
        return f"{self.nama} adalah karyawan tetap dengan gaji bulanan."

# Subclass KaryawanKontrak
class KaryawanKontrak(Karyawan):
    def __init__(self, nama, gaji_harian, jumlah_hari):
        self.nama = nama
        self.gaji_harian = gaji_harian
        self.jumlah_hari = jumlah_hari

    def hitung_gaji(self):
        return self.gaji_harian * self.jumlah_hari

    def deskripsi(self):
        return f"{self.nama} adalah karyawan kontrak yang dibayar berdasarkan jumlah hari kerja."

# Subclass Freelance
class Freelance(Karyawan):
    def __init__(self, nama, tarif_per_jam, jam_kerja):
        self.nama = nama
        self.tarif_per_jam = tarif_per_jam
        self.jam_kerja = jam_kerja

    def hitung_gaji(self):
        return self.tarif_per_jam * self.jam_kerja

    def deskripsi(self):
        return f"{self.nama} adalah karyawan freelance yang dibayar per jam kerja."

# Objek dari subclass
karyawan_tetap = KaryawanTetap("Andi", 8000000)
karyawan_kontrak = KaryawanKontrak("Budi", 150000, 20)
freelance = Freelance("Citra", 50000, 120)

# Menampilkan hasil gaji dan deskripsi
print("Karyawan Tetap:")
print(karyawan_tetap.deskripsi())
print(f"Gaji: Rp{karyawan_tetap.hitung_gaji()}")

print("\nKaryawan Kontrak:")
print(karyawan_kontrak.deskripsi())
print(f"Gaji: Rp{karyawan_kontrak.hitung_gaji()}")

print("\nFreelance:")
print(freelance.deskripsi())
print(f"Gaji: Rp{freelance.hitung_gaji()}")
