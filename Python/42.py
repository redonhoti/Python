# Variabla globale
lista = [1, 2, 3]

def shto_element():
    lista.append(4)  # Ndryshim direkt pa përdorimin e "global"
    print(f"Lista brenda funksionit: {lista}")

shto_element()  # Rezultati: Lista brenda funksionit: [1, 2, 3, 4]
print(f"Lista jashtë funksionit: {lista}")  # Rezultati: Lista jashtë funksionit: [1, 2, 3, 4]
