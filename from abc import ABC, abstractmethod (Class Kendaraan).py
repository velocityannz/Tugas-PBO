from abc import ABC, abstractmethod

# Abstract class Kendaraan
class Kendaraan(ABC):
    @abstractmethod
    def jenis_bahan_bakar(self):
        pass

    @abstractmethod
    def kapasitas_penumpang(self):
        pass

# Subclass Mobil yang mengimplementasikan abstract method dari Kendaraan
class Mobil(Kendaraan):
    def __init__(self, bahan_bakar, kapasitas):
        self.bahan_bakar = bahan_bakar
        self.kapasitas = kapasitas
    
    def jenis_bahan_bakar(self):
        return f"Mobil ini menggunakan {self.bahan_bakar}."
    
    def kapasitas_penumpang(self):
        return f"Mobil ini memiliki kapasitas {self.kapasitas} penumpang."

# Subclass Motor yang mengimplementasikan abstract method dari Kendaraan
class Motor(Kendaraan):
    def __init__(self, bahan_bakar, kapasitas):
        self.bahan_bakar = bahan_bakar
        self.kapasitas = kapasitas

    def jenis_bahan_bakar(self):
        return f"Motor ini menggunakan {self.bahan_bakar}."

    def kapasitas_penumpang(self):
        return f"Motor ini memiliki kapasitas {self.kapasitas} penumpang."

# Objek dari subclass
mobil = Mobil("Bensin", 5)
motor = Motor("Bensin", 2)

# Menampilkan hasil
print(mobil.jenis_bahan_bakar())
print(mobil.kapasitas_penumpang())
print(motor.jenis_bahan_bakar())
print(motor.kapasitas_penumpang())
