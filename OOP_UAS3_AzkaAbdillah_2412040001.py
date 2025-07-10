import datetime

class Person:
    def __init__(self, person_id, first_name, last_name, date_of_birth, nationality):
        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.nationality = nationality

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Contract:
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
    def __init__(self, person_id, first_name, last_name, date_of_birth, nationality, 
                 jersey_number, market_value, position, status, team_id):
        super().__init__(person_id, first_name, last_name, date_of_birth, nationality)
        self.jersey_number = jersey_number
        self.market_value = market_value
        self.position = position
        self.status = status
        self.team_id = team_id
        self.contract = None

    def play_match(self):
        print(f"{self.get_full_name()} (No. {self.jersey_number}) sedang bermain di posisi {self.position}.")

class Coach(Person):
    def __init__(self, person_id, first_name, last_name, date_of_birth, nationality, 
                 license_level, role, team_id):
        super().__init__(person_id, first_name, last_name, date_of_birth, nationality)
        self.license_level = license_level
        self.role = role
        self.team_id = team_id
        self.contract = None

    def select_squad(self, player_list):
        print(f"{self.role} {self.get_full_name()} sedang memilih skuad dari {len(player_list)} pemain.")

class Staff(Person):
    def __init__(self, person_id, first_name, last_name, date_of_birth, nationality, 
                 department, role, club_id):
        super().__init__(person_id, first_name, last_name, date_of_birth, nationality)
        self.department = department
        self.role = role
        self.club_id = club_id
        self.contract = None

class Stadium:
    def __init__(self, stadium_id, name, capacity, address):
        self.stadium_id = stadium_id
        self.name = name
        self.capacity = capacity
        self.address = address

class Team:
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

# Implementasi Factory Method
class PersonFactory:
    @staticmethod
    def create_person(person_type, details):
        if person_type.lower() == 'player':
            return Player(**details)
        elif person_type.lower() == 'coach':
            return Coach(**details)
        elif person_type.lower() == 'staff':
            return Staff(**details)
        else:
            raise ValueError(f"Tipe person '{person_type}' tidak dikenal.")

class ContractFactory:
    @staticmethod
    def create_contract(person, club, details):
        details['person_id'] = person.person_id
        details['club_id'] = club.club_id
        return Contract(**details)


# --- ENTRY POINT PROGRAM ---
if __name__ == "__main__":
    
    # Setup data awal
    fc_cakrawala = Club(
        club_id="FC-CKW", name="FC Cakrawala", founding_date=datetime.date(2024, 1, 1), 
        budget=5000000000, league="Liga 3"
    )
    tim_muda = Team(
        team_id="CKW-U23", name="FC Cakrawala Muda", league="U-23", 
        division="Jawa Barat", club_id=fc_cakrawala.club_id
    )
    fc_cakrawala.add_team(tim_muda)

    #  objek pelatih via factory
    coach_details_1 = {
        'person_id': "P-001", 'first_name': "Shin Tae", 'last_name': "Yong", 
        'date_of_birth': datetime.date(1970, 10, 11), 'nationality': "South Korea",
        'license_level': "AFC Pro", 'role': "Head Coach", 'team_id': tim_muda.team_id
    }
    head_coach = PersonFactory.create_person("coach", coach_details_1)
    
    #  kontrak via factory
    contract_details_1 = {
        'contract_id': "K-001", 'start_date': datetime.date(2024, 1, 1), 
        'end_date': datetime.date(2026, 12, 31), 'salary': 25000000, 'clauses': "Juara Liga 3"
    }
    kontrak_head_coach = ContractFactory.create_contract(head_coach, fc_cakrawala, contract_details_1)
    head_coach.contract = kontrak_head_coach
    tim_muda.add_coach(head_coach)

    coach_details_2 = {
        'person_id':"P-002", 'first_name':"Budiono", 'last_name':"Siregar", 
        'date_of_birth':datetime.date(1985, 8, 15), 'nationality':"Indonesia",
        'license_level':"Lisensi B", 'role':"Assistant Coach", 'team_id':tim_muda.team_id
    }
    asisten_coach = PersonFactory.create_person("coach", coach_details_2)
    contract_details_2 = {
        'contract_id':"K-002", 'start_date':datetime.date(2024, 1, 1), 
        'end_date':datetime.date(2025, 12, 31), 'salary':15000000, 'clauses':"Evaluasi tahunan"
    }
    kontrak_asisten = ContractFactory.create_contract(asisten_coach, fc_cakrawala, contract_details_2)
    asisten_coach.contract = kontrak_asisten
    tim_muda.add_coach(asisten_coach)

    posisi_pemain = ["Goalkeeper", "Left Wing Defender", "Central Back Defender", "Right Wing Defender", "Central Back Defender", "Central Midfielder", "Central Midfielder", "Defensive Midfielder", "Second Striker", "Right Wing Forward", "Left Wing Forward", "Attacking Forward", "Attacking Midfielder", "Left Wing Defender", "Goalkeeper"]
    nama_pemain_terkenal = [
        ("Diogo", "Costa"), ("Nuno", "Mendes"), ("Josko", "Gvardiol"), ("Jeremie", "Frimpong"), ("William", "Saliba"),
        ("Jude", "Bellingham"), ("Pedri", "González"), ("Eduardo", "Camavinga"), ("Joao", "Felix"), ("Bukayo", "Saka"),
        ("Vinícius", "Junior"), ("Julian", "Alvarez"), ("Jamal", "Musiala"), ("Alejandro", "Balde"), ("Gianluigi", "Donnarumma")
    ]
    
    for i in range(15):
        nama_depan, nama_belakang = nama_pemain_terkenal[i]
        player_details = {
            'person_id': f"P-{i+3:03d}", 'first_name': nama_depan, 'last_name': nama_belakang,
            'date_of_birth': datetime.date(2003, 1, 1), 'nationality': "International",
            'jersey_number': i + 1, 'position': posisi_pemain[i], 'market_value': 15000000,
            'status': "Active", 'team_id': tim_muda.team_id
        }
        pemain_baru = PersonFactory.create_person("player", player_details)

        contract_details = {
            'contract_id': f"K-{i+3:03d}", 'start_date': datetime.date(2024, 7, 1), 
            'end_date': datetime.date(2025, 6, 30), 'salary': 7000000, 'clauses': "Bonus per gol"
        }
        kontrak_pemain = ContractFactory.create_contract(pemain_baru, fc_cakrawala, contract_details)
        pemain_baru.contract = kontrak_pemain
        tim_muda.add_player(pemain_baru)

    print(f"Selamat Datang di Sistem Manajemen Klub {fc_cakrawala.name}!")
    
    # Login
    active_coach = None
    while not active_coach:
        print("\n--- Pilih Wewenang Anda ---")
        for idx, coach in enumerate(tim_muda.coaches):
            print(f"{idx + 1}. {coach.get_full_name()} ({coach.role})")
        
        try:
            pil_coach = int(input("Login sebagai (masukkan nomor): "))
            if 1 <= pil_coach <= len(tim_muda.coaches):
                active_coach = tim_muda.coaches[pil_coach - 1]
            else:
                print("Nomor tidak valid. Coba lagi.")
        except ValueError:
            print("Input salah!! Harap masukkan nomor.")
    
    print("\n" + "="*40)
    print(f"Login berhasil! Anda masuk sebagai:")
    print(f"   {active_coach.get_full_name()} ({active_coach.role})")
    print("="*40)

    # Menu Utama
    while True:
        print("\nMENU UTAMA:")
        print("1. Lihat Daftar Pemain")
        print("2. Pilih Pemain")
        print("3. Ubah Nama Pemain")
        print("4. Keluar")
        pilihan = input("pilih menu > ")

        if pilihan == '1':
            print("\n--- DAFTAR PEMAIN FC CAKRAWALA MUDA ---")
            print(f"{'No.':<5}{'Nama Pemain':<25}{'Posisi':<25}{'Status':<15}")
            print(f"{'-'*4:<5}{'-'*23:<25}{'-'*23:<25}{'-'*13:<15}")
            for p in tim_muda.players:
                print(f"{p.jersey_number:<5}{p.get_full_name():<25}{p.position:<25}{p.status:<15}")

        elif pilihan == '2':
            try:
                nomor_punggung_input = int(input("Masukkan nomor punggung: "))
                player_found = next((p for p in tim_muda.players if p.jersey_number == nomor_punggung_input), None)
                
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
                    active_coach.select_squad(tim_muda.players)
                    player_found.play_match()
                else:
                    print(f"ERROR: Pemain dgn no punggung {nomor_punggung_input} tidak ada.")
            except ValueError:
                print("ERROR: masukkan angka yang valid.")

        elif pilihan == '3':
            try:
                no_in = int(input("Nomor punggung pemain yg mau diubah: "))
                pemain_terpilih = next((p for p in tim_muda.players if p.jersey_number == no_in), None)
                
                if pemain_terpilih:
                    print(f"Nama saat ini: {pemain_terpilih.get_full_name()}")
                    nama_depan_baru = input("Nama depan baru: ").strip()
                    nama_belakang_baru = input("Nama belakang baru: ").strip()
                    
                    if nama_depan_baru and nama_belakang_baru:
                        pemain_terpilih.first_name = nama_depan_baru
                        pemain_terpilih.last_name = nama_belakang_baru
                        print(f"Nama pemain berhasil diubah jadi: {pemain_terpilih.get_full_name()}")
                    else:
                        print("Nama tidak boleh kosong.")
                else:
                    print(f"ERROR!! pemain dengan no punggung {no_in} tidak ditemukan.")
            except ValueError:
                 print("ERROR!! masukkan angka yang valid.")

        elif pilihan == '4':
            print("\nAnda telah logout. Terimakasih!")
            break
        else:
            print("Pilihan tidak valid!!")