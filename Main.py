import json
import random

# Hier werden alle Vokabellisten gespeichert
vokabellisten = {}import json
import random

# Hier werden alle Vokabellisten gespeichert
vokabellisten = {}


# Speichert alle Vokabeln in einer JSON-Datei
def speichern():
    with open("vokabeln.json", "w", encoding="utf-8") as datei:
        json.dump(vokabellisten, datei, indent=4, ensure_ascii=False)


# Lädt die gespeicherten Vokabeln beim Start
def laden():
    global vokabellisten
    try:
        with open("vokabeln.json", "r", encoding="utf-8") as datei:
            vokabellisten = json.load(datei)
    except:
        # Falls noch keine Datei existiert
        vokabellisten = {}


# Erstellt eine neue Vokabelliste und fügt Vokabeln hinzu
def liste_erstellen():
    name = input("Name der Liste: ").strip()

    if name == "":
        print("Darf nicht leer sein.")
        return

    # Verhindert doppelte Listen
    if name in vokabellisten:
        print("Liste existiert bereits.")
        return

    vokabellisten[name] = []
    print("Liste wurde erstellt.")

    # Maximal 10 Vokabeln pro Liste
    while len(vokabellisten[name]) < 10:
        thai = input("Thai (Schrift): ").strip()

        # Leere Eingabe beendet die Eingabe
        if thai == "":
            break

        lautschrift = input("Lautschrift: ").strip()

        # Deutsch darf nicht leer bleiben
        while True:
            deutsch = input("Deutsch: ").strip()

            if deutsch == "":
                print("Deutsch darf nicht leer sein.")
            else:
                break

        kommentar = input("Kommentar (optional): ").strip()

        # Eine einzelne Vokabel
        vokabel = {
            "thai": thai,
            "lautschrift": lautschrift,
            "deutsch": deutsch,
            "kommentar": kommentar
        }

        vokabellisten[name].append(vokabel)

        print("Vokabel hinzugefügt.")

        # Direkt speichern, damit nichts verloren geht
        speichern()


# Zeigt vorhandene Listen und deren Vokabeln an
def listen_anzeigen():
    if not vokabellisten:
        print("Keine Liste vorhanden.")
        return

    namen = list(vokabellisten.keys())

    print("\nVorhandene Listen:")

    # Listen nummeriert anzeigen
    for nummer, name in enumerate(namen, start=1):
        print(f"{nummer}) {name}")

    auswahl = input("Welche Liste möchtest du anzeigen? ").strip()

    # Prüft, ob eine Zahl eingegeben wurde
    if not auswahl.isdigit():
        print("Bitte eine Zahl eingeben.")
        return

    auswahl = int(auswahl)

    # Prüft, ob die Auswahl gültig ist
    if auswahl < 1 or auswahl > len(namen):
        print("Ungültige Auswahl.")
        return

    listenname = namen[auswahl - 1]

    print(f"\nListe: {listenname}")

    if not vokabellisten[listenname]:
        print("Diese Liste ist leer.")
        return

    # Alle Vokabeln der gewählten Liste anzeigen
    for nummer, vokabel in enumerate(vokabellisten[listenname], start=1):
        print(f"\n{nummer}. Vokabel")
        print(f"Thai: {vokabel['thai']}")
        print(f"Lautschrift: {vokabel['lautschrift']}")
        print(f"Deutsch: {vokabel['deutsch']}")

        # Kommentar nur anzeigen, wenn einer eingetragen wurde
        if vokabel["kommentar"] != "":
            print(f"Kommentar: {vokabel['kommentar']}")


# Startet ein kleines Quiz mit zufälligen Vokabeln
def quiz_starten():
    if not vokabellisten:
        print("Keine Listen vorhanden.")
        return

    namen = list(vokabellisten.keys())

    print("\nVorhandene Listen:")

    for nummer, name in enumerate(namen, start=1):
        print(f"{nummer}) {name}")

    auswahl = input("Mit welcher Liste möchtest du üben? ").strip()

    if not auswahl.isdigit():
        print("Bitte eine Zahl eingeben.")
        return

    auswahl = int(auswahl)

    if auswahl < 1 or auswahl > len(namen):
        print("Ungültige Auswahl.")
        return

    listenname = namen[auswahl - 1]

    if not vokabellisten[listenname]:
        print("Diese Liste ist leer.")
        return

    # Maximal 10 Fragen oder weniger, wenn die Liste kleiner ist
    anzahl_fragen = min(10, len(vokabellisten[listenname]))
    punkte = 0

    for i in range(anzahl_fragen):
        # Zufällige Vokabel auswählen
        vokabel = random.choice(vokabellisten[listenname])

        print(f"\nFrage {i + 1}:")
        print(f"Thai: {vokabel['thai']}")
        print(f"Lautschrift: {vokabel['lautschrift']}")

        antwort = input("Deutsch: ").strip()

        # Groß- und Kleinschreibung wird ignoriert
        if antwort.lower() == vokabel["deutsch"].lower():
            print("Richtig!")
            punkte += 1
        else:
            print("Falsch.")
            print(f"Richtig wäre: {vokabel['deutsch']}")

    print(f"\nQuiz beendet. Ergebnis: {punkte} von {anzahl_fragen} richtig.")

    # Kurze Pause, damit man das Ergebnis lesen kann
    input("\nDrücke Enter, um ins Menü zurückzukehren...")


# Zeigt das Hauptmenü
def menue_anzeigen():
    print("\nVokabel-App")
    print("1) Liste erstellen")
    print("2) Liste anzeigen")
    print("3) Quiz starten")
    print("4) Beenden")


# Beim Start werden gespeicherte Daten geladen
laden()

# Hauptschleife der App
while True:
    menue_anzeigen()

    auswahl = input("Bitte wähle eine Option (1-4): ").strip()

    if auswahl == "1":
        liste_erstellen()
    elif auswahl == "2":
        listen_anzeigen()
    elif auswahl == "3":
        quiz_starten()
    elif auswahl == "4":
        print("Programm beendet.")
        break
    else:
        print("Bitte eine gültige Option wählen.")
    
# Speichert alle Vokabeln in einer JSON-Datei
def speichern():
    with open("vokabeln.json", "w", encoding="utf-8") as datei:
        json.dump(vokabellisten, datei, indent=4, ensure_ascii=False)

# Lädt die gespeicherten Vokabeln beim Start
def laden():
    global vokabellisten
    try:
        with open("vokabeln.json", "r", encoding="utf-8") as datei:
            vokabellisten = json.load(datei)
    except:
        vokabellisten = {}

# Erstellt eine neue Vokabelliste und fügt Vokabeln hinzu
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

def quiz_starten():
    if not vokabellisten:
        print("Keine Listen vorhanden.")
        return
    
    namen = list(vokabellisten.keys())
    
    print("\nVorhandene Listen:")
    for nummer, name in enumerate(namen, start=1):
        print(f"{nummer}) {name}")
    
    auswahl = input("Mit welcher Liste möchtest du üben? ").strip()

    if not auswahl.isdigit():
        print("Bitte eine Zahl eingeben.")
        return
    
    auswahl = int(auswahl)
    
    if auswahl < 1 or auswahl > len(namen):
        print("Ungültige Auswahl.")
        return
    
    listenname = namen[auswahl - 1]

    if not vokabellisten[listenname]:
        print("Diese Liste ist leer.")
        return

    anzahl_fragen = min(10, len(vokabellisten[listenname]))
    punkte = 0

    for i in range(anzahl_fragen):

        vokabel = random.choice(vokabellisten[listenname])

        print(f"\nFrage {i+1}:")
        print(f"Thai: {vokabel['thai']}")
        print(f"Lautschrift: {vokabel['lautschrift']}")

        antwort = input("Deutsch: ").strip()

        if antwort.lower() == vokabel["deutsch"].lower():
            print("Richtig!")
            punkte += 1
        else:
            print("Falsch.")
            print(f"Richtig wäre: {vokabel['deutsch']}")
    
    print(f"\nQuiz beendet. Ergebnis: {punkte} von {anzahl_fragen} richtig.") 

    input("\nDrücke Enter, um ins Menü zurückzukehren...")

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
        quiz_starten()
    elif auswahl == "4":
        print("Programm beenden")
        break
    else:
        print("Bitte eine gültige Option wählen.")
    