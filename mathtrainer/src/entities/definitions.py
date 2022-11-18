#tähän lisätään harjoituskokonaisuuksien nimiä
DESCRIPTION = {
    1: "Leikkikysymyksiä TODO Peruslaskutoimitusten harjoittelua (erityisesti jos suomi ei äidinkieli)",
    2: "Leikkikysymyksiä TODO Alkeita muuttujista ja yhtälöistä"
}
    

#Päämenun valinnat, tähän lisätään valintamahdollisuuksia
COMMANDS = {
        "O" : "Ohje (O-kirjain)",
        "X" : "Lopetus",      
        "Y" : "Ylläpito (vaatii salasanan)",
        "1" : DESCRIPTION[1],
        "2" : DESCRIPTION[2]   
        }

#Harjoituksessa olevien tasojen eli osaharjoitusten lukumäärä. Jokaiselle uudelle harjoituskokonaisuudelle lisäys.
MAXLEVELS = {
    1: 2,   #harjoituksessa 1 tasoja 2
    2: 3,   #harjoituksessa 2 tasoja 3 
}



"""Harjoituksen lisäämisen päivitysohje:

   kun lisäät harjoituksen, vaikkapa numero 100, joka on koodattu tiedostoon  practises.practises100.py   
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