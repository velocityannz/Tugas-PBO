# Class
class Mobil:
    # Atribut
    Merk = ""
    Model = ""

    # Instance
    def __init__(self, tipe):
        self.tipe = tipe

    # Method 1
    def printMbl(self):
        print("Merk Mobil : ", self.Merk)
        print("Model Mobil : ", self.Model)
        print("Tipe Mobil : ", self.tipe)
    
    # Method 2
    def Status(self, kondisi):
        print("Kondisi mobil saat ini:")
        print(kondisi)

# Objek
Mbl1 = Mobil("Sedan")
Mbl2 = Mobil("SUV")

# Value
Mbl1.Merk = "Honda"
Mbl1.Model = "Civic"
Mbl2.Merk = "Honda"
Mbl2.Model = "CR-V"

# Pemanggilan Method
Mbl1.printMbl()
Mbl1.Status("Dalam kondisi baik dan siap digunakan")