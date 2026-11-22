navn = input("Hva heter du? ")
print("Hei,", navn)

print(f"Hei, {navn}")

alder = int(input("Hvor gammel er du? "))
print(type(alder))
print(alder + 1)

print(type(alder))
print(f"Alder til neste år, {alder + 1}")

høyde = float(input("Hvor høy er du? "))

# --- Refleksjon ---
# Det svarte at jeg brukte en string, fordi input kanskje automatisk blir en string først slik at brukeren kan skrive.
# Den klaget på at den ikke kunne konventere str til int.
# Jeg syns ("Hei,", navn) er lettest å lese nå, men kanskje det blir lettere å lese f-strengen når det blir mer kode. det er mellomrom for å ha avstand fra komma i begge variantene.