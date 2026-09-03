class Hero:
    # Constructor: Dijalankan saat Hero baru dibuat
    def __init__(self, name, hp, attack_power):
        self.name = name          # Nama Hero
        self.hp = hp              # Nyawa (Health Point)
        self.attack_power = attack_power # Kekuatan Serangan

    # Method untuk menampilkan info hero (harus menjorok ke dalam class)
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power:{self.attack_power}")

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    # Method diserang: Menerima damage
    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP:{self.hp}")


hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

# Tambah kode Output di akhir program
print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2) # Layla menyerang Zilong
hero2.serang(hero1) # Zilong membalas

hero1.diserang(hero1.attack_power)


# Perhatikan parameter lawan pada method serang. Parameter tersebut
# menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini
# penting?

# Jika kita hanya mengirim string (misalnya "Zilong"), program hanya tahu teks namanya saja. Kita tidak akan bisa mengakses atau mengubah HP "Zilong". Dengan mengirim objek utuh (hero2), objek 'hero1' bisa mengakses atribut (lawan.name) dan memanggil method milik objek lawan (lawan.diserang()). Sehingga perubahan yang akan kita lakukan akan tersimpan secara langsung ke memori objek lawan yang sebenarnya