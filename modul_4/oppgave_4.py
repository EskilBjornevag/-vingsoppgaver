#alder = 25
#er_student = True
#har_medlemskort = False

# jeg tror det blir False
#print(alder < 12 or alder > 67)

# Jeg tror True, fordi alderen er under 30
#print(er_student and alder < 30)

# Jeg tror not har_medlemskort blir True, fordi det snur om verdien.
#print(not har_medlemskort)

# Jeg tror det blir True, siden er_student er sann.
#print(er_student or har_medlemskort)

# Jeg tror det blir False, fordi er_student var True og 30 var høyere en 25
#print(not er_student or alder < 30)

# Del 2

alder = 21

er_student = input("Er du student? (ja/nei) ").lower() == "ja"
alder = int(input("Hvor gammel er du? "))

if alder < 12 or alder > 67:
    print(f"Prisen er gratis.")
elif er_student and alder < 30:
    print(f"Prisen er 50kr.")
else:
    print(f"prisen er 120kr.")
if not er_student:
    print(f"Studenter under 30 får rabatt.")

# 8 år, ikke student = Det står at prisen er gratis og studenter under 30 år får rabatt.
# 70 år, ikke student = Det står at prisen er gratis og studenter under 30 år får rabatt.
# 22 år, student = Det står prisen er 50kr.
# 35 år, sududent = Det står prisen er 120kr.
# 25 år, ikke student = Det står prisen er 120kr, og studenter under 30 år får rabatt.

# Jeg tror viss jeg skriver .lower() så vil den gjøre alle bokstavene i lowecase, slik at prisen blir 50kr.

# --- Refleksjon ---
# - and er riktig når begge sidene er riktig. Or er riktig når en av sidene er riktig.
# - 35-åringen som student fikk 120kr i pris fordi han ikke var under 30 år
# - "not" bytter om på True eller False. Jeg kunne ha skrevet "if er_student == False:", for å få det samme svaret.
# - Regelen om at alle under 12 og over 67 slår inn først, fordi det ligger øverst i koden, som vil si at 70-åringen får gratis ingang.