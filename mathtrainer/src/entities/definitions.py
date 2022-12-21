"""Kun sovellukseen lisätään uusi harjoitus, tähän pitää
päivittää vakioon DESCRIPTION, lisätä harjoitus päävalikon
komentoihin COMMANDS ja lisätä harjoitus ja sen tasojen lukumäärä
vakioon MAXLEVELS."""


DESCRIPTION = {

    1: "Kirjoitettujen lukujen ilmaiseminen numeroilla",
    2: "Peruslaskutoimitusten harjoittelua kirjoitetuin numeroin",
    3: "Sanallisia peruslaskuharjoituksia (pari esimerkkiä)",
    4: "Yhtälön ratkaisun alkeita"
}
"""Harjoitusten nimet päävalikossa"""

COMMANDS = {
    "O": "Ohje (O-kirjain)",
    "X": "Lopetus",
    "Y": "Ylläpito (vaatii salasanan)",
    "1": DESCRIPTION[1],
    "2": DESCRIPTION[2],
    "3": DESCRIPTION[3],
    "4": DESCRIPTION[4]
}
"""Päävalikon valinnat, DESCRIPTION sisältää harjoitusten nimet."""

MAXLEVELS = {
    1: 6,  # harjoituksessa 1 tasoja 6
    2: 6,
    3: 2,
    4: 6
}
"""Harjoituksessa olevien tasojen eli osaharjoitusten lukumäärä."""

COMMANDS_ADMIN = {
    "0":   "paluu päävalikkoon",
    "1":   "kaikki käyttäjänimet",
    "2":   "kaikki käyttäjät harjoitustietoineen",
    "3":   "kaikki suoritukset",
    "4":   "kaikki annetun käyttäjän suoritukset",
    "5":   "kaikki annetun harjoituksen suoritukset",
    "6":   "tilasto annetun harjoituksen onnistumisprosenteista",
    "7":   "käyttäjätunnuksen poistaminen"
}
