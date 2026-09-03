class Hero:
    # Constructor: Dijalankan saat Hero baru dibuat
    def __init__(self, name, hp, attack_power):
        self.name = name          # Nama Hero
        self.hp = hp              # Nyawa (Health Point)
        self.attack_power = attack_power # Kekuatan Serangan

    # Method untuk menampilkan info hero (harus menjorok ke dalam class)
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power:{self.attack_power}")

# -- Main Program --
# Membuat Object (Instansiasi)
hero1 = Hero(None, 100, 15)
hero2 = Hero("Zilong", 120, 20)

hero1.hp = 500
# Memanggil Method
hero1.info()
hero2.info()