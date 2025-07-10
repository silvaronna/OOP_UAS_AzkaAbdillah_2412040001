import datetime


class Person:
    """Kelas dasar untuk semua individu dalam klub."""
    def __init__(self, person_id, first_name, last_name, date_of_birth, nationality):
        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.nationality = nationality

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Contract:
    """Mewakili kontrak untuk seorang Person."""
    def __init__(self, contract_id, start_date, end_date, salary, clauses, person_id, club_id):
        self.contract_id = contract_id
        self.start_date = start_date
        self.end_date = end_date
        self.salary = salary
        self.clauses = clauses
        self.person_id = person_id
        self.club_id = club_id

    def __str__(self):
        return f"Kontrak hingga {self.end_date.year} dengan gaji Rp{self.salary:,.0f}"

class Player(Person):
    """Mewakili seorang pemain."""
    def __init__(self, person_id, first_name, last_name, date_of_birth, nationality, 
                 jersey_number, market_value, position, status, team_id):
        super().__init__(person_id, first_name, last_name, date_of_birth, nationality)
        self.jersey_number = jersey_number
        self.market_value = market_value
        self.position = position
        self.status = status
        self.team_id = team_id
        self.contract = None

    def assign_contract(self, contract):
        self.contract = contract

    def play_match(self):
        print(f"{self.get_full_name()} (No. {self.jersey_number}) sedang bermain di posisi {self.position}.")

class Coach(Person):
    """Mewakili seorang pelatih."""
    def __init__(self, person_id, first_name, last_name, date_of_birth, nationality, 
                 license_level, role, team_id):
        super().__init__(person_id, first_name, last_name, date_of_birth, nationality)
        self.license_level = license_level
        self.role = role
        self.team_id = team_id
        self.contract = None

    def assign_contract(self, contract):
        self.contract = contract

    def select_squad(self, player_list):
        print(f"{self.role} {self.get_full_name()} sedang memilih skuad dari {len(player_list)} pemain.")

class Staff(Person):
    """Mewakili staf klub."""
    def __init__(self, person_id, first_name, last_name, date_of_birth, nationality, 
                 department, role, club_id):
        super().__init__(person_id, first_name, last_name, date_of_birth, nationality)
        self.department = department
        self.role = role
        self.club_id = club_id
        self.contract = None

    def assign_contract(self, contract):
        self.contract = contract

class Stadium:
    """Mewakili stadion klub."""
    def __init__(self, stadium_id, name, capacity, address):
        self.stadium_id = stadium_id
        self.name = name
        self.capacity = capacity
        self.address = address

class Team:
    """Mewakili sebuah tim dalam klub."""
    def __init__(self, team_id, name, league, division, club_id):
        self.team_id = team_id
        self.name = name
        self.league = league
        self.division = division
        self.club_id = club_id
        self.players = []
        self.coaches = []

    def add_player(self, player):
        self.players.append(player)
    
    def add_coach(self, coach):
        self.coaches.append(coach)

class Club:
    """Kelas utama yang mewakili klub sepak bola."""
    def __init__(self, club_id, name, founding_date, budget, league):
        self.club_id = club_id
        self.name = name
        self.founding_date = founding_date
        self.budget = budget
        self.league = league
        self.teams = []
        self.stadium = None

    def add_team(self, team):
        self.teams.append(team)
    
    def assign_stadium(self, stadium):
        self.stadium = stadium


def show_player_list(team):
    """Menampilkan daftar pemain dalam tim."""
    print("\n--- DAFTAR PEMAIN FC CAKRAWALA MUDA ---")
    print(f"{'No.':<5}{'Nama Pemain':<25}{'Posisi':<25}{'Status':<15}")
    print(f"{'-'*4:<5}{'-'*23:<25}{'-'*23:<25}{'-'*13:<15}")
    for p in team.players:
        print(f"{p.jersey_number:<5}{p.get_full_name():<25}{p.position:<25}{p.status:<15}")

def select_player(team, coach):
    """Memilih dan menampilkan detail seorang pemain."""
    try:
        nomor_punggung_input = int(input("Masukkan nomor punggung: "))
        player_found = None
        for pemain in team.players:
            if pemain.jersey_number == nomor_punggung_input:
                player_found = pemain
                break
        
        if player_found:
            print("\n--- Detail Pemain ---")
            print(f"  Nama         : {player_found.get_full_name()}")
            print(f"  No Punggung  : {player_found.jersey_number}")
            print(f"  Posisi       : {player_found.position}")
            print(f"  Status       : {player_found.status}")
            print(f"  Market Value : Rp{player_found.market_value:,.0f}")
            if player_found.contract:
                print(f"  Info Kontrak : {player_found.contract}")
            else:
                print("  Info Kontrak : Belum ada kontrak.")
            
            print("\n--- Simulasi Aksi ---")
            coach.select_squad(team.players)
            player_found.play_match()
        else:
            print(f"ERROR: Pemain dgn no punggung {nomor_punggung_input} tidak ada.")
    except ValueError:
        print("ERROR: masukkan angka yang valid.")

def change_player_name(team):
    """Mengubah nama seorang pemain."""
    try:
        no_in = int(input("Nomor punggung pemain yg mau diubah: "))
        pemain_terpilih = None
        for pemain in team.players:
            if pemain.no_punggung == no_in:
                pemain_terpilih = pemain
                break
        
        if pemain_terpilih:
            print(f"Nama saat ini: {pemain_terpilih.get_full_name()}")
            nama_depan_baru = input("Nama depan baru: ").strip()
            nama_belakang_baru = input("Nama belakang baru: ").strip()
            
            if nama_depan_baru and nama_belakang_baru:
                pemain_terpilih.first_name = nama_depan_baru
                pemain_terpilih.last_name = nama_belakang_baru
                print(f"Nama pemain berhasil diubah jadi: {pemain_terpilih.get_full_name()}")
            else:
                print("Tidak boleh kosong.")
        else:
            print(f"ERROR!! pemain dengan no punggung {no_in} tidak ditemukan.")
    except ValueError:
        print("ERROR!! masukkan angka yang valid.")


def setup_data():
    """create entry point data such as (klub, tim, pemain, pelatih)."""
    fc_cakrawala = Club(
        club_id="FC-CKW", name="FC Cakrawala", founding_date=datetime.date(2024, 1, 1), 
        budget=5000000000, league="Liga 3"
    )
    
    tim_muda = Team(
        team_id="CKW-U23", name="FC Cakrawala Muda", league="U-23", 
        division="Jawa Barat", club_id=fc_cakrawala.club_id
    )
    fc_cakrawala.add_team(tim_muda)

    head_coach = Coach("P-001", "Shin Tae", "Yong", datetime.date(1970, 10, 11), "South Korea", 
                       "AFC Pro", "Head Coach", team_id=tim_muda.team_id)
    kontrak_head_coach = Contract("K-001", datetime.date(2024, 1, 1), datetime.date(2026, 12, 31), 
                                  25000000, "Juara Liga 3", head_coach.person_id, fc_cakrawala.club_id)
    head_coach.assign_contract(kontrak_head_coach)
    tim_muda.add_coach(head_coach)

    asisten_coach = Coach("P-002", "Budiono", "Siregar", datetime.date(1985, 8, 15), "Indonesia", 
                          "Lisensi B", "Assistant Coach", team_id=tim_muda.team_id)
    kontrak_asisten = Contract("K-002", datetime.date(2024, 1, 1), datetime.date(2025, 12, 31), 
                               15000000, "Evaluasi tahunan", asisten_coach.person_id, fc_cakrawala.club_id)
    asisten_coach.assign_contract(kontrak_asisten)
    tim_muda.add_coach(asisten_coach)

    posisi_pemain = ["Goalkeeper", "Left Wing Defender", "Central Back Defender", "Right Wing Defender", "Central Back Defender", "Central Midfielder", "Central Midfielder", "Defensive Midfielder", "Second Striker", "Right Wing Forward", "Left Wing Forward", "Attacking Forward", "Attacking Midfielder", "Left Wing Defender", "Goalkeeper"]
    nama_pemain_terkenal = [
        ("Diogo", "Costa"), ("Nuno", "Mendes"), ("Josko", "Gvardiol"), ("Jeremie", "Frimpong"), ("William", "Saliba"),
        ("Jude", "Bellingham"), ("Pedri", "González"), ("Eduardo", "Camavinga"), ("Joao", "Felix"), ("Bukayo", "Saka"),
        ("Vinícius", "Junior"), ("Julian", "Alvarez"), ("Jamal", "Musiala"), ("Alejandro", "Balde"), ("Gianluigi", "Donnarumma")
    ]
    
    for i in range(15):
        nama_depan, nama_belakang = nama_pemain_terkenal[i]
        pemain_baru = Player(
            person_id=f"P-{i+3:03d}", first_name=nama_depan, last_name=nama_belakang,
            date_of_birth=datetime.date(2003, 1, 1), nationality="International",
            jersey_number=i + 1, position=posisi_pemain[i], market_value=15000000,
            status="Active", team_id=tim_muda.team_id
        )
        kontrak_pemain = Contract(
            contract_id=f"K-{i+3:03d}", start_date=datetime.date(2024, 7, 1), end_date=datetime.date(2025, 6, 30),
            salary=7000000, clauses="Bonus per gol", person_id=pemain_baru.person_id, club_id=fc_cakrawala.club_id
        )
        pemain_baru.assign_contract(kontrak_pemain)
        tim_muda.add_player(pemain_baru)

    return fc_cakrawala, tim_muda

def login_menu(team):
    """Menangani logika login untuk memilih pelatih."""
    active_coach = None
    while not active_coach:
        print("\n--- Pilih Wewenang Anda ---")
        for idx, coach in enumerate(team.coaches):
            print(f"{idx + 1}. {coach.get_full_name()} ({coach.role})")
        
        try:
            pil_coach = int(input("Login sebagai (masukkan nomor): "))
            if 1 <= pil_coach <= len(team.coaches):
                active_coach = team.coaches[pil_coach - 1]
            else:
                print("Nomor tidak valid. Coba lagi.")
        except ValueError:
            print("Input salah!! Harap masukkan nomor.")
    
    print("\n" + "="*40)
    print(f"Login berhasil! Anda masuk sebagai:")
    print(f"   {active_coach.get_full_name()} ({active_coach.role})")
    print("="*40)
    return active_coach

def main_menu(team, coach):
    """Menampilkan menu utama dan menangani input pengguna."""
    while True:
        print("\nMENU UTAMA:")
        print("1. Lihat Daftar Pemain")
        print("2. Pilih Pemain")
        print("3. Ubah Nama Pemain")
        print("4. Keluar")
        pilihan = input("pilih menu > ")

        if pilihan == '1':
            show_player_list(team)
        elif pilihan == '2':
            select_player(team, coach)
        elif pilihan == '3':
            print("Fitur 'Ubah Nama Pemain' belum diimplementasikan dalam fungsi terpisah.")
        elif pilihan == '4':
            print("\nAnda telah logout. terimakasih!")
            break
        else:
            print("Pilihan tidak valid!!")

def main():
    """Fungsi utama untuk menjalankan seluruh aplikasi."""
    club, team = setup_data()
    print(f"Selamat Datang di Sistem Manajemen Klub {club.name}!")
    
    active_coach = login_menu(team)
    if active_coach:
        main_menu(team, active_coach)

if __name__ == "__main__":
    main()