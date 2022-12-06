# tähän lisätään harjoituskokonaisuuksien nimiä
DESCRIPTION = {

    1: "Kirjoitettujen lukujen ilmaiseminen numeroilla",
    2: "Peruslaskutoimitusten harjoittelua kirjoitetuin numeroin",
    3: "TODO Sanallisesta peruslaskuharjoituksia (ei valittavissa)",
    4: "Yhtälön ratkaisun alkeita"
}


# Päämenun valinnat, tähän lisätään valintamahdollisuuksia
COMMANDS = {
    "O": "Ohje (O-kirjain)",
    "X": "Lopetus",
    "Y": "Ylläpito (vaatii salasanan)",
    "1": DESCRIPTION[1],
    "2": DESCRIPTION[2],
    "3": DESCRIPTION[3],
    "4": DESCRIPTION[4],


}
# Harjoituksessa olevien tasojen eli osaharjoitusten lukumäärä.
# Jokaiselle uudelle harjoituskokonaisuudelle lisäys.
MAXLEVELS = {
    1: 6,  # harjoituksessa 1 tasoja 6
    2: 6,
    3: 1,
    4: 6
}


"""Harjoituksen lisäämisen päivitysohje:
   kun lisäät harjoituksen, vaikkapa numero 100,
   joka on koodattu tiedostoon  practises.practises100.py
   lisää session.py rivi

   if drill == 100:
            practises.practises100.do_practise(session, trainee)

   Päivitä ohjelma definitions.py lisäämällä

   DESCRIPTION = {
    ...
    100: "Harjoitusten 100 lyhyt kuvaus",
    }

   COMMANDS = {
        ...
        "100" : DESCRIPTION[100]
        }

    MAXLEVELS = {
    100: 10,   #harjoituksessa 100 tasoja (esim) 10
    }
"""
