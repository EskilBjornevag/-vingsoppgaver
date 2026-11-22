def hilsen(navn, alder, by="Oslo"):
    print(f"Hei, {navn}! Du er {alder} år og bor i {by}.")

brukerens_navn = input("Hva heter du? ")
brukerens_alder = int(input("Hvor gammel er du? "))

hilsen(brukerens_navn, brukerens_alder)

# Jeg tror det fortsatt fugerer, men det endra rekkefølge
# Jeg tror det kommer en feilmelding.

# --- Refleksjon ---
# - Parameter er plassen der argumentene skal være. "navn, alder og by" er parameter.
#   Argumenter er det som blir plassert inne i parameterene. Oslo, brukerens_navn og brukerens_alder er argumenter.
# - Steg 4 ga ikke en feilmelding, fordi variablene var riktig uansett.
# - Ja, det fungerte med forskjellig navn på variabelen og parameteren.
# - Jeg tror 
