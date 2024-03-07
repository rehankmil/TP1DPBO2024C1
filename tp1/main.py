from karakter import Karakter
from senjata import Senjata
from npc import NPC
from misi import Misi

if __name__ == "__main__":
    # Membuat senjata
    panah = Senjata("Panah", 10)
    pedang = Senjata("Pedang", 15)
    tombak = Senjata("Tombak", 12)
    tongkat_sihir = Senjata("Tongkat Sihir", 18)
    kapak = Senjata("Kapak", 5)

    # Membuat karakter
    fauzan = Karakter("Fauzan", "Laki-laki", panah, 100, 20, "DPS", [])
    yasin = Karakter("Yasin", "Laki-laki", pedang, 120, 25, "Tank", [])
    bintang = Karakter("Bintang", "Laki-laki", tombak, 110, 22, "CC", [])
    mia = Karakter("Mia", "Perempuan", tongkat_sihir, 90, 18, "Healer", [])
    monster = Karakter("Monster Hutan", "???", kapak, 50, 10, "Musuh", [])

    # Membuat NPC
    adrian = NPC("Adrian", "Laki-laki", "Memberikan misi")
    lyra = NPC("Lyra", "Perempuan", "Memberikan informasi")

    # Membuat misi
    misi1 = Misi("Misi Penyelamatan", "Menyelamatkan desa dari serangan monster", "Pedang legendaris")
    misi2 = Misi("Misi Pengintaian", "Mengintai gerakan musuh di hutan terlarang", "Harta karun")
    
    print("SELAMAT DATANG DI GAME PETUALANGAN!!!")

    # Menampilkan statistik karakter
    print("\nLihat Karaktermu!")
    print(f"{fauzan.nama} ({fauzan.status_lain}) :")
    print(f"- HP      = {fauzan.HP}")
    print(f"- ATK     = {fauzan.ATK}")
    print(f"- Senjata = {fauzan.senjata.jenis}")
    print(f"{yasin.nama} ({yasin.status_lain}) :")
    print(f"- HP      = {yasin.HP}")
    print(f"- ATK     = {yasin.ATK}")
    print(f"- Senjata = {yasin.senjata.jenis}")
    print(f"{bintang.nama} ({bintang.status_lain}) :")
    print(f"- HP      = {bintang.HP}")
    print(f"- ATK     = {bintang.ATK}")
    print(f"- Senjata = {bintang.senjata.jenis}")
    print(f"{mia.nama} ({mia.status_lain}) :")
    print(f"- HP      = {mia.HP}")
    print(f"- ATK     = {mia.ATK}")
    print(f"- Senjata = {mia.senjata.jenis}")

    # Interaksi dalam game
    print("\nSelamat datang Pemain!")
    print(f"{fauzan.nama} siap untuk petualangan!")
    adrian.memberikan_misi(fauzan, misi1)
    fauzan.melakukan_misi(misi1)
    print("\nDeskripsi Misi!")
    print(f"{misi1.deskripsi}")
    print(f"{misi1.tujuan}")
    print(f"Hadiah : {misi1.hadiah}")

    # Informasi tambahan dari NPC
    print(f"\nBantuan dari {adrian.nama} dan {lyra.nama}!")
    lyra.memberikan_informasi("Hati-hati dengan kekuatan musuh di hutan terlarang!")
    adrian.menjual_barang("Potion")

    # Melawan monster
    print("\nMuncul Monster dalam hutan!")
    print(f"{monster.nama} ({monster.status_lain}) :")
    print(f"{monster.status_lain}")
    print(f"- HP      = {monster.HP}")
    print(f"- ATK     = {monster.ATK}")
    print(f"- Senjata = {monster.senjata.jenis}")

    print("\nBunuh Monster!")
    fauzan.menyerang(monster)
    bintang.menyerang(monster)
    yasin.menyerang(monster)
    mia.menyerang(monster)

    # Menyelesaikan misi lain
    print("\nMisi baru ditemukan!")
    lyra.memberikan_misi(yasin, misi2)
    yasin.melakukan_misi(misi2)
    print("\nDeskripsi Misi!")
    print(f"{misi2.deskripsi}")
    print(f"{misi2.tujuan}")
    print(f"Hadiah : {misi2.hadiah}")