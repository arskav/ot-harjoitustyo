import os

from entities.definitions import DESCRIPTION, COMMANDS, MAXLEVELS
#Vakiot, joita käytetään päävalikon esittämiseen, ja harjoituskokonaisuuksien tasojen lukumäärä
#tiedostoa päivitetään aina lisättäessä uusi harjoituskokonaisuus

from entities.user import MathTrainerUser
#yksittäistä käyttäjää kuvaava luokka

from entities.session import MathTrainerSession
#meneillään olevaa harjoitusta kuvaava luokka

#Pääohjelmaa vastaava luokka
class MathTrainer:   
    #Käyttöliittymää vastaava luokka
    def mainmenu(self):
        
        trainee = self._login()
        #kirjaudutaan järjestelmään uuten atai vanhana käyttäjänä
        #harjoituksen tekijan tiedot luokan MathTrainerUse mukaisesti

        while True:       
            self._show_main_menu(trainee)
            #Näytetään valikko

            choice = input("Valinta: ").upper()
            if not choice in COMMANDS:
                #Tarkistetaan, tunnistetaanko annettu komento
                os.system('clear')
                print(choice, "on virheellinen komento")
                print("Valitse uudelleen")
            elif choice == "X":   
                self._shutdown(trainee)
                #Lopetetaan istunto.
                break
            elif choice == "Y":
                self._maintenance()
                #TODO ylläpito
            else:
                self._action(trainee, choice)       
                #Valitaan jokin harjoituksista tai tulostetaan ohjeet     
    
    def _show_main_menu(self, trainee):
        #Päävalikko    
        print(trainee)              
        #Näytetään käyttäjän tiedot
            
        for command in COMMANDS:
            print(command, ":", COMMANDS[command])

    def _maintenance(self):

        print("TODO Kysytään salasanaa")
        print("Avataan valikko, missä toimenpidemahdollisuuksia.")
        print("Lähinnä tilastotietoa suorituksista.")
        input("Enter paluu päävalikkoon.")


    def _action(self, trainee, choice):
        #Ohjeet tai jokin harjoituksista
        if choice == "O":
            #Ohjeita
            self._help()        
        else:
            self._begin_practising(int(choice), trainee)
            #Aloitetaan harjoitus

                    
    def _begin_practising(self, drill, trainee):
        #drill aloitettavan harjoituksen numero, trainee käyttäjä

        if drill not in trainee._practise_finished:   
            #Käyttäjä ei ole tehnyt harjoitusta loppuun
            if drill in trainee._practise_started:
                print("Harjoitus aloitettu")
                print("TODO tiedot haetaan tietokannasta")
                print("Nyt kuitenkin aloitetaan alusta")
                input(" Jatka ")
                session = MathTrainerSession(trainee._user, practise = drill, max =  MAXLEVELS[drill])
            else:                    
                #1. harjoituskerta
                #harjoitussessioon liittyvä tiedot luokan MathTrainerSessi mukaisesti
                session = MathTrainerSession(trainee._user, practise = drill, max =  MAXLEVELS[drill])
            
            session._begin_practise(drill, trainee)    
            #Aloitetaan tai jatketaan harjoitusta
            
                
        else:
                #Käytetyllä käyttäjätunnuksella on jo tehty kaikki harjoituksen tehtävät
                self._all_done(drill) 

    def _all_done(self, drill):
        print(f"Olet tehnyt kaikki tehtävät harjoituksissa {drill}." )     
        print("Jos haluat tehdä tämän harjoituksen tehtäviä uudelleen, valitse uusi käyttäjätunnus.")
        input("Enter paluu päävalikkoon.")


    def _shutdown(self, trainee):
        print("Lopetetaan ohjelman suoritus.")
        print("TODO tallennetaan käyttäjän tiedot tietokantaan")
        print("Käyttäjän tiedot:")
        print(trainee)
        input(" Jatka ")
        return

    def _help(self):
        os.system('clear')
        print("Valintasi: O")
        print("TODO tarvittavia ohjeita")

    def _login(self):
        os.system('clear')
        username = input("Anna käyttäjätunnus ")   
        #Tässä vaiheessa oletetaan, että aina uusi käyttäjätunnus
        #TODO jatkokehittelyssä tarkistetaan, onko tunnus jo tietokannassa
        #jos on, haetaan tiedot sieltä        
        trainee = MathTrainerUser(username, [], [], 0, 0)
        #TODO jos uusi käyttäjätunnus, tallennetaan se tietokantaan

        return(trainee)                       
           
    
