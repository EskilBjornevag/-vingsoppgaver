brus = 24.90
smørbrød = 45
banan = 8.50

print("Totalpris:",brus + smørbrød + banan)
print("Totalsum med 25% mva:", (brus + smørbrød + banan) * 1.25)
print("Pris per person:", (brus + smørbrød + banan) * 1.25 / 4)
print("prisforskjellen:", (smørbrød - banan))

# --- Refleksjon ---
# Smørbrød + brus ble en float siden det er et desimaltall.
# Datatypen ble en float, men jeg ble ikke overasket.
# Det er mye mer oversiktlig og raskere å bruke variabler, fordi en kan endre verdien på prisen ved å endre på en variabel.