poeng = int(input("Hvor mange poeng fikk du? "))

if poeng >= 90:
    print("A")
elif poeng >= 80:
    print("B")
elif poeng >= 60:
    print("C")
elif poeng >= 50:
    print("D")
elif poeng >= 40:
    print("E")
else:
    print("F")

# 95: Jeg forventer en A fordi >= er over 90.
# 72: Jeg forventer en C fordi >= er over 60.
# 40: Jeg forventer en E fordi >= er teller også med 40.
# 12: Jeg forventer en F fordi poeng under 40 blir en F.

if poeng >= 40:
    print("E")
if poeng >= 50:
    print("D")
if poeng >= 60:
    print("C")
if poeng >= 80:
    print("B")
if poeng >= 90:
    print("A")
else:
    print("F")

# Jeg tror det blir E

# --- Refleksjon ---
# - Den fikk E siden poengsummen var over 40, som vil si at den ikke trengte å gå videre til elif.
# - Jeg fikk alle karakterene untatt F. "if" skriver verdien om det den stemmer. elif stopper ved den siste verdien som stemmer.
# - Vi trenger ikke å sjekke poengene under 90, fordi vi har en poeng >= 90, som stenger ut poeng >= 80.
# - "else" kjører når ingen av poengene stemmer med "if" eller "elif".
#