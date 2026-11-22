alder = 31
aldersgrense = 18
navn = "Michael"
antall_studenter = 30

# Jeg tror det blir True, fordi alderen er høyere enn aldersgensen.
print(alder > aldersgrense)

# Jeg tror alder sjekker om det er sant at alder er 31. så det blir True.
print(alder == 31)

# Jeg tror != aldersgrense sjekker om alder ikke er lik aldersgrense, så det blir True.
print(alder != aldersgrense)

# Jeg tror <= sjekker om alder er mindre enn eller lik aldersgrense, så det blir False.
print(alder <= aldersgrense)

# Jeg tror sjekker om navnet er lik "Michael", så det blir True.
print(navn == "Michael")

# Jeg tror det sjekker om navnet er lik "Michael", men nå er det liten bokstav, så det blir False.
print(navn == "micahel")

# Jeg tror det sjekker om antall_studenter er lik eller over 30, så det blir True.
print(antall_studenter >= 30)

# Jeg tror det sjekker om alder + 5 år er over antall studenter, så det blir true
print(alder + 5 > antall_studenter)

# --- Refleksjon ---
# 5 og 6 ga forksjellige svar, fordi Michael er riktig i henold til variabelen.
# = Er et sybol for å vise at noe har samme verdi, mens == viser 