import json

vokabellisten = {}
    

def speichern():
    with open("vokabeln.json", "w", encoding="utf-8") as datei:
        json.dump(vokabellisten, datei, indent=4, ensure_ascii=False)

def laden():
    global vokabellisten
    try:
        with open("vokabeln.json", "r", encoding="utf-8") as datei:
            vokabellisten = json.load(datei)
    except:
        vokabellisten = {}

def liste_erstellen():
    name = input("Name der Liste:").strip()

    if name == "":
        print("Darf nicht Leer sein.")
        return
    
    if name in vokabellisten:
        print("Liste existiert bereits.")
        return
    
    vokabellisten[name] = []
    print("Liste wurde erstellt.")

    while len(vokabellisten[name]) < 10:

        thai = input("Thai(Schrift): ").strip()

        if thai == "":
            break

        lautschrift = input("Lautschrift: ").strip()

        while True:
            deutsch = input("Deutsch: ").strip()

            if deutsch == "":
                print("Deutsch darf nicht leer sein.")
            else:
                break

        kommentar = input("Kommentar (optional): ").strip()

        vokabel = {
            "thai": thai,
            "lautschrift": lautschrift,
            "deutsch": deutsch,
            "kommentar": kommentar
        }
       
        vokabellisten[name].append(vokabel)

        print("Vokabel hinzugefügt.")

        speichern()

def listen_anzeigen():
    if not vokabellisten:
        print("Keine liste vorhanden")
        return
    
    namen = list(vokabellisten.keys())
    
    print("\nVorhandene Listen:")
    for nummer, name in enumerate(namen, start=1):
        print(f"{nummer}) {name}")

    auswahl = input("Welche Liste möchtest du anzeigen? ").strip()

    if not auswahl.isdigit():
        print("Bitte eine Zahl eingeben.")
        return

    auswahl = int(auswahl)

    if auswahl < 1 or auswahl > len(namen):
        print("Ungültige Auswahl.")
        return

    listenname = namen[auswahl - 1]

    print(f"\nListe: {listenname}")

    if not vokabellisten[listenname]:
        print("Diese Liste ist leer.")
        return

    for nummer, vokabel in enumerate(vokabellisten[listenname], start=1):
        print(f"\n{nummer}. Vokabel")
        print(f"Thai: {vokabel['thai']}")
        print(f"Lautschrift: {vokabel['lautschrift']}")
        print(f"Deutsch: {vokabel['deutsch']}")

        if vokabel["kommentar"] != "":
            print(f"Kommentar: {vokabel['kommentar']}")



def menue_anzeigen():
    print("\nVokabel-App")
    print("1) Liste erstellen")
    print("2) Liste Anzeigen")
    print("3) Quiz starten")
    print("4) Beenden")

laden()

while True:
    menue_anzeigen()

    auswahl = input("Bitte wähle eine Option (1-4): ").strip()

    if auswahl == "1":
        liste_erstellen()
    elif auswahl == "2":
        listen_anzeigen()
    elif auswahl == "3":
        print("Quiz anzeigen kommt Später")
    elif auswahl == "4":
        print("Programm beenden")
        break
    else:
        print("Bitte eine gültige Option wählen.")
    