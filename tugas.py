from abc import ABC, abstractmethod

class KamarHotel(ABC):
    def __init__(self, roomName, stock, basePrice):
        self.nama_kamar = roomName
        self.__stok = stock
        self.__harga_dasar = basePrice

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah_malam):
        pass

    def getBasePrice(self):
        return self.__harga_dasar

    def getStock(self):
        return self.__stok

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f'Gagal update stok {self.nama_kamar}! Stok tidak boleh negatif ({jumlah})')
        else:
            self.__stok += jumlah
            print(f'Berhasil menambahkan {self.nama_kamar}: {jumlah} unit')

class KamarDeluxe(KamarHotel):
    def __init__(self):
        super().__init__('Kamar Deluxe', 0, 1500000)
        self.fasilitas = ['Private Pool']
        self.tax = 0.1


    def tampilkan_detail(self):
        harga = self.getBasePrice()
        print(f'[DELUXE] Kamar Deluxe Sea View | Fasilitas: {', '.join(self.fasilitas)}')
        print(f"Harga Dasar/Malam: Rp " + f"{harga:_.0f}".replace('_', '.') + " | Pajak(10%): Rp " + f"{(harga * self.tax):_.0f}".replace('_', '.') )

    def hitung_harga_total(self, jumlah_malam):
        harga = self.getBasePrice()
        return (harga * (1 + self.tax) * jumlah_malam)



class KamarStandard(KamarHotel):
    def __init__(self):
        super().__init__('Kamar Standard', 0, 500000)
        self.kapasitas = '2 Orang'
        self.tax = 0.05

    def tampilkan_detail(self):
        harga = self.getBasePrice()
        print(f'[STANDARD] Kamar Standard Superior | Kapasitas: {self.kapasitas}')
        print(f"Harga Dasar/Malam: Rp " + f"{harga:_.0f}".replace('_', '.') + " | Pajak(5%): Rp " + f"{(harga * self.tax):_.0f}".replace('_', '.') )

    def hitung_harga_total(self, jumlah_malam):
        harga = self.getBasePrice()
        return (harga * (1 + self.tax) * jumlah_malam)



def proses_transaksi(daftar_pesanan):
    print()
    print('--- STRUK PEMESANAN ---')
    totalInvoice = 0
    i = 0
    for order in daftar_pesanan:
        print(str(i+1) + '. ', end='')
        kamar = order['kamar']
        jumlah_malam = order['jumlah_malam']
        kamar.tampilkan_detail()
        subtotal = kamar.hitung_harga_total(jumlah_malam)
        totalInvoice += subtotal
        print(f'Menginap: {jumlah_malam} malam | Subtotal: Rp ' + f"{subtotal:_.0f}".replace('_', '.'))
        print()
        i += 1
    
    print('----------------------------------------')
    print('TOTAL TAGIHAN: Rp ' + f"{totalInvoice:_.0f}".replace('_', '.'))
    print('----------------------------------------')





print('--- SETUP DATA KAMAR ---')

kamarDeluxe = KamarDeluxe()
kamarStandard = KamarStandard()

kamarDeluxe.tambah_stok(10)
kamarStandard.tambah_stok(-5)
kamarStandard.tambah_stok(20)

daftarPesanan = [
    {
        "kamar": kamarDeluxe,
        "jumlah_malam": 2
    },
    {
        "kamar": kamarStandard,
        "jumlah_malam": 1
    }
]

proses_transaksi(daftarPesanan)