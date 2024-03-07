class NPC:
    def __init__(self, nama, jenis_kelamin, tindakan):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.tindakan = tindakan

    def memberikan_misi(self, karakter, misi):
        print(f"{self.nama} memberikan misi kepada {karakter.nama}: {misi.deskripsi}")

    def memberikan_informasi(self, informasi):
        print(f"{self.nama} memberikan informasi penting: {informasi}")

    def menjual_barang(self, barang):
        print(f"{self.nama} menjual barang: {barang}")

    def membeli_barang(self, barang):
        print(f"{self.nama} membeli barang: {barang}")
