import os
from entities.definitions import DESCRIPTION
#Harjoitusten kuvaukset

from services.utilities import return_to_menu
#vakiokysymys vaiheessa, jossa jonkun harjoituksen tietyn tason kysymykset on tehty 

import practises.practises1
import practises.practises2
#Näitä lisätään sitä mukaa kun tulee lisää harjoituskokonaisuuksia

class MathTrainerSession:
    def __init__(self, username, practise, max, level=1, correct=0, tries=0,  correct_level=0, tries_level=0, cancelled = False): 
        self._user = username
        self._practise = practise
        self._correct = correct
        self._tries = tries
        self._level = level
        self._maxlevel = max
        self._correct_at_level = correct_level
        self._tries_at_level = tries_level
        self._cancelled = cancelled


    def __str__(self):

        string = self._user 
        string += " harjoitus " + str(self._practise) 
        string += "\n" + "Yrityksiä tässä harjoituksessa " + str(self._tries) + ", joista "
        string += "oikeita vastauksia " + str(self._correct)        
        string += "\nTaso " + str(self._level) + "/" + str(self._maxlevel) + ", tällä tasolla yrityksiä " + str(self._tries_at_level) + ", joista " 
        string += "oikeita vastauksia " + str(self._correct_at_level)        
                
        return(string)

    def _begin_practise(self, drill, trainee):
        
        os.system('clear')
        print(DESCRIPTION[drill])    
        print("Nyt ei kuitenkaan vielä varsinaisia tehtäviä")
        #Tässä voisi olla myös enemmänkin tehtäväkokonaisuuden esittelyä              
        
        #lisätään tieto, että harjoitus drill aloitettu
        #tässä vaiheessa ohjelmaa tämä aina aloituskerta, koska tietoja ei tallenneta vielä
        #Jatkossa haetaan vanhat tiedot tietokannasta.
        if drill not in trainee._practise_started:
            trainee._practise_started.append(drill) 
        
        self._do_practise(drill,trainee)        
   
   
    def _do_practise(self, drill, trainee):
        #trainee on harjoituksen tekijä, drill harjoituksen nro ja self harjoituksen suoritustiedot       

        training = True
        

        while training and self._level <= self._maxlevel:
             
            if drill == 1:
                practises.practises1.do_practise(self, trainee)
                #Tehdään harjoitus 1 tasolla level, 
                #session: harjoituskerran tiedot,
                #trainee: käyttäjän harjoittelua koskevat tiedot


            if drill == 2:
                practises.practises2.do_practise(self, trainee)
                #vrt. yllä

            #HARJOITUKSEN LISÄÄMINEN
            # jos esim. numero 100
            # if drill == 100:
            #       practises100.do_practise(session, trainee)
            #tiedostossa paractises100 funktio do_practise, joka sisältää harjoituksen.

            

            if self._level - 1 == self._maxlevel:            
                print(f"Olet tehnyt kaikki tehtävät harjoituksissa {drill}." )     
                print("Jos haluat tehdä tämän harjoituksen tehtäviä uudelleen, valitse uusi käyttäjätunnus.")                
                print("TODO tallennetaan tilastointia varten harjoituskerran tiedot tietokantaan.")
                print("taso on nyt max taso + 1 sen merkiksi, että harjoitus tehty loppuun")
                #print(self) tarkistusta varten
                #Tähän voisi lisätä yhteenvedon harjoitusten sujumisesta
                input("Enter paluu päävalikkoon.")
            
                #päivitetään tieto tästä käyttäjän tietoihin                
                trainee._practise_finished.append(drill)                
                break            
       
                        
            if self._cancelled or (return_to_menu() == 'X'):                                  
                    print(self)
                    print("TODO tallennetaan harjoituskerran tiedot tietokantaan")
                    input("Jatka ")
                    break
        
    def _new_attempt(self):
        #uusi yritys, kasvatetaan yritysten sekä harjoitus- että tasokohtaista lukumäärää yhdellä
        self._tries += 1
        self._tries_at_level += 1  

    def _level_up(self):
        #siirrytään seuraavalle tasolle
        #Tulostetaan tilanne        
        print(self)
        print("Siirrytään seuraavalle tasolle")
        input("Jatka ")

        self._level += 1
        #nollataan tason yritysten ja oikeiden vastausten lkm
        self._tries_at_level = 0
        self._correct_at_level = 0


    def _correct_up(self):
        #oikea vastaus, kasvatetaan oikeiden vastausten sekä harjoitus- että tasokohtaista lukumäärää yhdellä      
        #tähän voi lisätä muutakin toimintaa kuin vain oikeiden vastausten lukumäärän kasvattaminen
        self._correct += 1
        self._correct_at_level += 1

        
    