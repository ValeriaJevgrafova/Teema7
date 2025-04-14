from random import *

def failist_to_dict(f:str):
    riik_pealinn = {}
    pealinn_riik = {}
    riigid = []
    file = open(f, 'r', encoding="utf-8-sig")
    for line in file:
        k, v = line.strip().split('-')
        riik_pealinn[k] = v
        pealinn_riik[v] = k
        riigid.append(k)
    file.close()
    return riik_pealinn, pealinn_riik, riigid

riik_pealinn, pealinn_riik, riigid = failist_to_dict("riigid_pealinnad.txt")

def kuva_pealinn(riik_nimi):
    """Kuva riigi pealinn vastavalt riigi nimele."""
    return riik_pealinn.get(riik_nimi, "Riiki ei leitud sõnastikus.")

def kuva_riik(pealinn_nimi):
    """Kuva riik vastavalt pealinna nimele."""
    return pealinn_riik.get(pealinn_nimi, "Pealinna ei leitud sõnastikus.")

def lisa_sonastikku(riik, pealinn):
    """Lisa riik ja pealinn mõlemasse sõnastikku."""
    riik_pealinn[riik] = pealinn
    pealinn_riik[pealinn] = riik

def paranda_sonastikku(riik, uus_pealinn):
    """Paranda riigi pealinn sõnastikus."""
    vana_pealinn = riik_pealinn.get(riik)
    if vana_pealinn:
        pealinn_riik.pop(vana_pealinn)
        riik_pealinn[riik] = uus_pealinn
        pealinn_riik[uus_pealinn] = riik
    else:
        print(f"Riik {riik} ei leitud.")

def kontrolli_tea():
    """Kontrolli kasutaja teadmisi riikide ja pealinnade kohta."""
    õiged_vastused = 0
    kogus = 5
    
    for _ in range(kogus):
        # Sõltuvalt juhuslikult valitakse, kas küsitakse riiki või pealinna
        kysimuse_tyyp = choice(['riik', 'pealinn'])

        if kysimuse_tyyp == 'riik':
            riik = choice(riigid)
            pealinn = riik_pealinn[riik]
            kasutaja_vastus = input(f"Mis on {riik} pealinn? ")

            if kasutaja_vastus.lower() == pealinn.lower():
                print("Õige vastus!")
                õiged_vastused += 1
            else:
                print(f"Vale vastus. Õige vastus on: {pealinn}")

        elif kysimuse_tyyp == 'pealinn':
            pealinn = choice(list(pealinn_riik.keys()))
            riik = pealinn_riik[pealinn]
            kasutaja_vastus = input(f"Mis riik on pealinna {pealinn} koduks? ")

            if kasutaja_vastus.lower() == riik.lower():
                print("Õige vastus!")
                õiged_vastused += 1
            else:
                print(f"Vale vastus. Õige vastus on: {riik}")
    
    print(f"Teie tulemus: {õiged_vastused}/{kogus} ({(õiged_vastused / kogus) * 100:.2f}%)")

def pea():
    while True:
        print("\nMenüü:")
        print("1. Kuva pealinn riigi nime järgi")
        print("2. Kuva riik pealinna nime järgi")
        print("3. Lisa uus riik ja pealinn")
        print("4. Paranda pealinn")
        print("5. Kontrolli teadmisi")
        print("6. Välju")

        valik = input("Valige tegevus (1-6): ")

        if valik == '1':
            riik = input("Sisestage riigi nimi: ")
            print(kuva_pealinn(riik))

        elif valik == '2':
            pealinn = input("Sisestage pealinna nimi: ")
            print(kuva_riik(pealinn))

        elif valik == '3':
            riik = input("Sisestage riigi nimi: ")
            pealinn = input("Sisestage pealinna nimi: ")
            lisa_sonastikku(riik, pealinn)
            print(f"Riik {riik} koos pealinna {pealinn} on lisatud.")

        elif valik == '4':
            riik = input("Sisestage riik, mille pealinna soovite parandada: ")
            uus_pealinn = input("Sisestage uus pealinn: ")
            paranda_sonastikku(riik, uus_pealinn)

        elif valik == '5':
            kontrolli_tea()

        elif valik == '6':
            print("Väljumine programmilt.")
            break

        else:
            print("Vale valik. Proovige uuesti.")

if __name__ == "__main__":
    pea()
