from os import path, remove, listdir

# 1. Failist lugemine järjendisse
def loe_failist(failinimi: str) -> list:
    with open(failinimi, 'r', encoding="utf-8-sig") as f:
        return [rida.strip() for rida in f]

# 2. Järjendi kirjutamine faili
def kirjuta_failisse(failinimi: str, andmed: list):
    with open(failinimi, 'w', encoding="utf-8-sig") as f:
        for rida in andmed:
            f.write(rida + '\n')

# 3. Faili olemasolu kontroll ja kustutamine
if path.isfile("TextFile1.txt"):
    remove("TextFile1.txt")
    print("Fail kustutati.")
else:
    print("Faili ei leitud, loome uue.")

# 4. Loome ja kirjutame andmed faili
nimed = ["Ann", "Kati", "Mari"]
kirjuta_failisse("TextFile1.txt", nimed)

# 5. Faili lugemine tervikuna .read() abil
with open("TextFile1.txt", "r", encoding="utf-8-sig") as f:
    sisu = f.read()
print("Faili sisu (read):")
print(sisu)

# 6. Ühe rea lugemine readline() abil
with open("TextFile1.txt", "r", encoding="utf-8-sig") as f:
    print("Esimene rida (readline):", f.readline().strip())

# 7. Kõigi ridade lugemine readlines() abil
with open("TextFile1.txt", "r", encoding="utf-8-sig") as f:
    readlines_tulemus = f.readlines()
    print("Ridade loend (readlines):", [r.strip() for r in readlines_tulemus])

# 8. Faili ridade läbimine tsükliga
print("Faili sisu ridade kaupa:")
with open("TextFile1.txt", "r", encoding="utf-8-sig") as f:
    for rida in f:
        print(rida.strip())

# 9. MP3-failide otsimine kaustast
mp3_leidub = False
kaust = "C:\\Users\\Public\\Music"  # Muuda vajadusel oma kausta teeks

try:
    failinimed = listdir(kaust)
    for fail in failinimed:
        if fail.endswith(".mp3"):
            mp3_leidub = True
            break
except FileNotFoundError:
    print("Kausta ei leitud:", kaust)

print("MP3 leiti:", mp3_leidub)
