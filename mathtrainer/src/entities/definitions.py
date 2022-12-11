# tähän lisätään harjoituskokonaisuuksien nimiä
DESCRIPTION = {

    1: "Kirjoitettujen lukujen ilmaiseminen numeroilla",
    2: "Peruslaskutoimitusten harjoittelua kirjoitetuin numeroin",
    3: "Sanallisia peruslaskuharjoituksia (pari esimerkkiä)",
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
    3: 2,
    4: 6
}
