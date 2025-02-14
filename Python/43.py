# Variabla globale
konteksi = "Fillestar"
def ndrysho_konteksin():
    global konteksi
    konteksi = "I përparuar"
def printo_konteksin():
    print(f"Konteksi është: {konteksi}")
ndrysho_konteksin()
printo_konteksin()  # Rezultati: Konteksi është: I përparuar
