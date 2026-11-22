riktig_brukernavn = "michael"
riktig_passord = "python123"

alder = int(input("Hvor gammel er du? "))

if alder < 13:
    print("Du er for ung til å logge inn")
else:
    brukernavn = input("Skriv inn brukernavnet ditt: ")
    passord = input("Skriv inn passordet ditt: ")

    if brukernavn == riktig_brukernavn and passord == riktig_passord:
        print(f"Velkommen, {riktig_brukernavn}!")
    elif brukernavn == riktig_brukernavn:
        print("riktig brukernavn, feil passord.")
    else:
        print("Ukjent bruker.")

# riktig brukernavn, riktig passord: Jeg tror det står "Velkommen, micheal!"
# riktig brukernavn, feil passord: Jeg tror det står "Riktig brukernavn, feil passord."
# feil brukernavn, riktig passord: Jeg tror det står "Ukjent bruker."
# feil brukernavn, feil passord Jeg trpr det står "Ukjent bruker."


# --- Refleksjon ---
# - Jeg bruke and for å sjekke at brukernavnet og passordet var riktige samtidig.
# - "if" må stå først for å sjekke alderen.
# - Jeg tror nettsider ikke sier hvem av dem som er feil for å gjøre det vanskligere å gjette seg frem.
# - Det er lurt å teste alle kombinasjonene, for å sikre seg at det håndterer riktig og feil svar.
