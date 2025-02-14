# Variabla globale
numri = 10
def ndrysho_numrin():
    global numri  # Përdorimi i fjalës "global" për të ndryshuar vlerën
    numri = 20
    print(f"Numri brenda funksionit: {numri}")
ndrysho_numrin()  # Rezultati: Numri brenda funksionit: 20
print(f"Numri jashtë funksionit: {numri}")  # Rezultati: Numri jashtë funksionit: 20
