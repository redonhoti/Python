# Variabla globale
vlera = 50

def ndrysho_vleren():
    vlera = 100  # Kjo është një variabël lokale
    print(f"Vlera brenda funksionit: {vlera}")

ndrysho_vleren()  # Rezultati: Vlera brenda funksionit: 100
print(f"Vlera jashtë funksionit: {vlera}")  # Rezultati: Vlera jashtë funksionit: 50
