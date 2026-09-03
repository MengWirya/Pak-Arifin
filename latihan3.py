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

# Class Mage adalah anak dari class Hero
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        # Memanggil constructor milik Parent (Hero)
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana:{self.mana}")

    # Mage punya skill khusus
    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke{lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2) # Damage 2x lipat
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")

# -- Main Program Baru --
print("\n--- Update Class Hero ---")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)
eudora.info()
eudora.serang(balmond) # Serangan biasa (warisan dari Hero)
eudora.skill_fireball(balmond) # Skill khusus Mage


# Eksperimen Fungsi super(): Pada class Mage, coba hapus (atau jadikan
# komentar #) baris kode super().__init__(name, hp, attack_power). Kemudian
# jalankan programnya.

# Pertanyaan: Error apa yang muncul saat kamu mencoba melihat info Eudora
# (eudora.info())? Mengapa error tersebut mengatakan Mage object has no
# attribute 'name', padahal kita sudah mengirim nama "Eudora" saat
# pembuatan objek?

# --- Update Class Hero ---
# Traceback (most recent call last):
#   File "c:\Users\mengw\Documents\Personal Project\ALL CODING\Coding!!!\PakArifin\latihan3.py", line 44, in <module>
#     eudora.info()
#     ~~~~~~~~~~~^^
#   File "c:\Users\mengw\Documents\Personal Project\ALL CODING\Coding!!!\PakArifin\latihan3.py", line 29, in info
#     print(f"{self.name} [Mage] | HP: {self.hp} | Mana:{self.mana}")
#              ^^^^^^^^^
# AttributeError: 'Mage' object has no attribute 'name'

# Error ini terjadi dikarenakan subclass Mage tidak memiliki class dari hero karena ia tidak mewariskan attribute
# dari class hero menggunakan super(). Jika tidak menggunakan super() subclass mage hanya memiliki atribute mana saja