
def skriv_meny():
    skriv_skillelinje()
    print("--- Meny ---")
    print("1. Pannekaker")
    print("2. Vaffler")
    print("3. Lapper")
    skriv_skillelinje()

def skriv_velkomst():
    print("Velkommen!")
    print("Under finner du menyen.")

def skriv_skillelinje():
    print("-" * 20)


skriv_velkomst()
skriv_meny()
skriv_meny()
skriv_meny()

# --- Refleksjon ---
# Ingen ting blir skrevet ut, på grunn av at jeg ikke kaller prosedyren
# definere en prosedyre er å lage den og innholdet, men å kalle en prosedyre er å bruke den til å skrive noe ut.
# Jeg fikk error fordi jeg prøvde å kalle på prosedyren før den var definert, siden den var over hvor jeg definerte prosedyren. Python leser kode fra toppen og ned.
# Det er mye raskere å skrive en prosedyre, istedenfor å skrive samme kode flere ganger.