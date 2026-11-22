riktig_svar = "Oslo"

svar = input("Hva er hovedstaden i Norge? ")

if svar == riktig_svar:
    print("Riktig!")
else:
    print("Feil, svaret var", riktig_svar)

alder = int(input("Hvor gammel er du? "))

if alder == 18:
    print("Du er akkurat myndig!")
elif alder > 18:
    print("Du er myndig!")
else:
    print("Du er ikke 18.")

    # --- Refleksjon ---
# - Feielene var en manglende = tegn og det var et manglene kolon.
# - Siste feilen var at den sa jeg ikke var myndig om jeg var over 18 år. 
#   Jeg oppdaget den ved å svare på alderen i terminalen. 
#   Jeg tror ikke Python klaget, fordi koden fungerte helt fint, selv om skriften som står ikke gir mening.
# - Syntakstfeil er når koden er skrevet feil, og en logisk feil er når koden fungerer, men den er ikke logisk i den virkelige verden.
#.  Jeg tror logisk feil er farligest i den ekte verden, fordi det kan muligens gi feil svar, som kan skape store konsekvenser. 
# - Det er lurt å teste ulik alder, for å se om de stemmer.