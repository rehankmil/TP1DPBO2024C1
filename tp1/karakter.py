class Karakter:
    def __init__(self, nama, jenis_kelamin, senjata, HP, ATK, status_lain, barang_di_simpan):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.senjata = senjata
        self.HP = HP
        self.ATK = ATK
        self.status_lain = status_lain
        self.barang_di_simpan = barang_di_simpan

    def melakukan_misi(self, misi):
        print(f"{self.nama} sedang menyelesaikan misi: {misi.deskripsi}")

    def menyerang(self, target):
        print(f"{self.nama} menyerang {target.nama} dengan {self.senjata.jenis}!")
        # Logika serangan

    def menggunakan_skill(self):
        print(f"{self.nama} menggunakan skill khusus!")
        # Logika penggunaan skill

    def meningkatkan_kekuatan(self):
        print(f"{self.nama} meningkatkan kekuatan!")
        # Logika peningkatan kekuatan
