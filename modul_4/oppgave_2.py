aldersgrense = 18
alder = 18

if alder > aldersgrense:
    print(f"Du er {alder} år, og gammel nok.")
else:
    print(f"Du er {alder} år, og ikke gammel nok.")

print("Takk for at du sjekket!")

# 17 år, jeg forventer at jeg ikke er gammel nok.
# 18 år, jeg forventer at jeg er gammel nok.
# 19 år, jeg forventer at jeg er gammel nok.

# --- Refleksjon ---
# - I steg 5 forventet Python en indented block, som er innrykket.  I steg 6 er det invalid syntax, som betyr at Python ikke forstår hvordan koden er skrevet.
# - Fordi det står print uten if/else over.
# - alder >= aldersgrense betyr True om alderen er lik eller høyere aldersgrensen, viss alderen er under går det videre til else.
# - >= er riktig for en aldersgrense på 18 år, fordi da er man gammel nok om man er 18. Om en bruker bare > er man ikke gammel nok som 18 år.