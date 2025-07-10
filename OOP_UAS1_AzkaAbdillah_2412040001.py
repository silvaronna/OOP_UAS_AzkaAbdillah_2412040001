import datetime

class Person:
    def __init__(self, id, nama_depan, nama_belakang, tgl_lahir, kebangsaan):
        self.person_id = id
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.tgl_lahir = tgl_lahir
        self.kebangsaan = kebangsaan

    def get_full_name(self):
        return f"{self.nama_depan} {self.nama_belakang}"

class Contract:
    def __init__(self, id, tgl_mulai, tgl_selesai, gaji):
        self.contract_id = id
        self.tgl_mulai = tgl_mulai
        self.tgl_selesai = tgl_selesai
        self.gaji = gaji

    def __str__(self):
        return f"Kontrak hingga {self.tgl_selesai.year} dengan gaji Rp{self.gaji:,.0f}"

class Player(Person):
    def __init__(self, id, nama_depan, nama_belakang, tgl_lahir, kebangsaan, no_punggung, posisi, kontrak):
        super().__init__(id, nama_depan, nama_belakang, tgl_lahir, kebangsaan)
        self.no_punggung = no_punggung
        self.posisi = posisi
        self.kontrak = kontrak

    def play_match(self):
        print(f"{self.get_full_name()} (No. {self.no_punggung}) sedang bermain di posisi {self.posisi}.")

class Coach(Person):
    def __init__(self, id, nama_depan, nama_belakang, tgl_lahir, kebangsaan, lisensi, peran, kontrak):
        super().__init__(id, nama_depan, nama_belakang, tgl_lahir, kebangsaan)
        self.lisensi = lisensi
        self.peran = peran
        self.kontrak = kontrak
    def select_squad(self, daftar_pemain):
        print(f"{self.peran} {self.get_full_name()} sedang memilih skuad dari {len(daftar_pemain)} pemain.")

class Staff(Person):
    def __init__(self, id, nama_depan, nama_belakang, tgl_lahir, kebangsaan, departemen, peran, kontrak):
        super().__init__(id, nama_depan, nama_belakang, tgl_lahir, kebangsaan)
        self.departemen = departemen
        self.peran = peran
        self.kontrak = kontrak

class Stadium:
    def __init__(self, id, nama, kapasitas, lokasi):
        self.stadium_id=id
        self.nama=nama
        self.kapasitas=kapasitas
        self.lokasi=lokasi

class Team:
    # team class
    def __init__(self, id, nama, divisi):
        self.team_id = id
        self.nama = nama
        self.divisi = divisi
        self.daftar_pemain = []
        self.daftar_pelatih = []
    def tambah_pemain(self, pemain):
        self.daftar_pemain.append(pemain)
    def tambah_pelatih(self, pelatih):
        self.daftar_pelatih.append(pelatih)

class Club:
    # main class
    def __init__(self, id, nama, thn_berdiri):
        self.club_id = id
        self.nama = nama
        self.thn_berdiri = thn_berdiri
        self.daftar_tim = []
        self.stadion = None
    def tambah_tim(self, tim):
        self.daftar_tim.append(tim)

# main program
if __name__ == "__main__":
    fc_cakrawala = Club(id="FC-CKW", nama="FC Cakrawala", thn_berdiri=2024)
    tim_muda = Team(id="CKW-U23", nama="FC Cakrawala Muda", divisi="U-23")
    fc_cakrawala.tambah_tim(tim_muda)
    # data pelatih
    kontrak_head_coach = Contract("K-001", datetime.date(2024, 1, 1), datetime.date(2026, 12, 31), 25000000)
    head_coach = Coach("P-001", "Shin Tae", "Yong", datetime.date(1970, 10, 11), "South Korea", "AFC Pro", "Head Coach", kontrak_head_coach)
    kontrak_asisten = Contract("K-002", datetime.date(2024, 1, 1), datetime.date(2025, 12, 31), 15000000)
    asisten_coach = Coach("P-002", "Budiono", "Siregar", datetime.date(1985, 8, 15), "Indonesia", "Lisensi B", "Assistant Coach", kontrak_asisten)
    tim_muda.tambah_pelatih(head_coach)
    tim_muda.tambah_pelatih(asisten_coach)

    posisi_pemain = ["Goalkeeper", "Left Wing Defender", "Central Back Defender", "Right Wing Defender", "Central Back Defender", "Central Midfielder", "Central Midfielder", "Defensive Midfielder", "Second Striker", "Right Wing Forward", "Left Wing Forward", "Attacking Forward", "Attacking Midfielder", "Left Wing Defender", "Goalkeeper"]
    nama_pemain_terkenal = [
        ("Diogo", "Costa"), ("Nuno", "Mendes"), ("Josko", "Gvardiol"), ("Jeremie", "Frimpong"), ("William", "Saliba"),
        ("Jude", "Bellingham"), ("Pedri", "González"), ("Eduardo", "Camavinga"), ("Joao", "Felix"), ("Bukayo", "Saka"),
        ("Vinícius", "Junior"), ("Julian", "Alvarez"), ("Jamal", "Musiala"), ("Alejandro", "Balde"), ("Gianluigi", "Donnarumma")
    ]
    # data pemain
    for i in range(15):
        kontrak_pemain = Contract(f"K-{i+3:03d}", datetime.date(2024, 7, 1), datetime.date(2025, 6, 30), 7000000) # Gaji sedikit disesuaikan
        nama_depan, nama_belakang = nama_pemain_terkenal[i]
        pemain_baru = Player(f"P-{i+3:03d}", nama_depan, nama_belakang, datetime.date(2003, 1, 1), "International", i + 1, posisi_pemain[i], kontrak_pemain)
        tim_muda.tambah_pemain(pemain_baru)

    print(f"Selamat Datang di Sistem Manajemen Klub {fc_cakrawala.nama}!")
    coach_aktif = None
    while not coach_aktif:
        print("\n--- Pilih Wewenang Anda ---")
        for idx, coach in enumerate(tim_muda.daftar_pelatih):
            print(f"{idx + 1}. {coach.get_full_name()} ({coach.peran})")
        try:
            pil_coach = int(input("Login sebagai (masukkan nomor): "))
            if 1 <= pil_coach <= len(tim_muda.daftar_pelatih):
                coach_aktif = tim_muda.daftar_pelatih[pil_coach - 1]
            else:
                print("Nomor tidak valid. Coba lagi.")
        except ValueError:
            print("Input salah!! Harap masukkan nomor.")
    print("\n" + "="*40)
    print(f"Login berhasil! Anda masuk sebagai:")
    print(f"   {coach_aktif.get_full_name()} ({coach_aktif.peran})")
    print("="*40)

    while True:
        print("\nMENU UTAMA:")
        print("1. Lihat Daftar Pemain")
        print("2. Pilih Pemain")
        print("3. Ubah Nama Pemain")
        print("4. Keluar")
        pilihan = input("pilih menu > ")

        if pilihan == '1':
            print("\n--- DAFTAR PEMAIN FC CAKRAWALA MUDA ---")
            print(f"{'No.':<5}{'Nama Pemain':<25}{'Posisi':<25}")
            print(f"{'-'*4:<5}{'-'*23:<25}{'-'*23:<25}")
            for p in tim_muda.daftar_pemain:
                print(f"{p.no_punggung:<5}{p.get_full_name():<25}{p.posisi:<25}")

        elif pilihan == '2':
            try:
                nomor_punggung_input = int(input("Masukkan nomor punggung: "))
                player_found = None
                for pemain in tim_muda.daftar_pemain:
                    if pemain.no_punggung == nomor_punggung_input:
                        player_found = pemain
                        break
                if player_found:
                    print("\n--- Detail Pemain ---")
                    print(f"  Nama         : {player_found.get_full_name()}")
                    print(f"  No Punggung  : {player_found.no_punggung}")
                    print(f"  Posisi       : {player_found.posisi}")
                    print(f"  Info Kontrak : {player_found.kontrak}")
                    print("\n--- Simulasi Aksi ---")
                    coach_aktif.select_squad(tim_muda.daftar_pemain)
                    player_found.play_match()
                else:
                    print(f"ERROR: Pemain dgn no punggung {nomor_punggung_input} tidak ada.")
            except ValueError:
                print("ERROR: masukkan angka yang valid.")
        
        elif pilihan == '3':
            try:
                no_in = int(input("Nomor punggung pemain yg mau diubah: "))
                pemain_terpilih = None
                for pemain in tim_muda.daftar_pemain:
                    if pemain.no_punggung == no_in:
                        pemain_terpilih = pemain
                        break
                if pemain_terpilih:
                    print(f"Nama saat ini: {pemain_terpilih.get_full_name()}")
                    nama_depan_baru = input("Nama depan baru: ").strip()
                    nama_belakang_baru = input("Nama belakang baru: ").strip()
                    if nama_depan_baru and nama_belakang_baru:
                        pemain_terpilih.nama_depan = nama_depan_baru
                        pemain_terpilih.nama_belakang = nama_belakang_baru
                        print(f"Nama pemain berhasil diubah jadi: {pemain_terpilih.get_full_name()}")
                    else:
                        print("Tidak boleh kosong.")
                else:
                    print(f"ERROR!! pemain dengan no punggung {no_in} tidak ditemukan.")
            except ValueError:
                 print("ERROR!! masukkan angka yang valid.")

        elif pilihan == '4':
            print("\nAnda telah logout. terimakasih!")
            break
        else:
            print("Pilihan tidak valid!!")