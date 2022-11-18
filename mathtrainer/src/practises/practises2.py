import os
from services.utilities import update_total

#Tämä on kopio harjoituksesta 1 testausta varten


FINISH = 2
#Kuinka monen peräkkäisen oikean vastauksen jälkeen siirrytään seuraavalle tasolle.
#Siirtymisehto voi olla valmiissa harjoituksessa joku muukin.

def do_practise(session, trainee):
    
            level = session._level
            #Harjoituksen taso

            successive_correct = 0
            #Kun peräkkäisiä oikeita vastauksia on (tässä) 2, siirrytään seuraavalle tasolle.
            #Jatkossa siirtymisehtoa voi mutkistaa ja se voi vaihdella eri tasoilla ja harjoituksissa
            
            #Tämä on vain ohjelmarungon testausta, joten kaikilla tasoilla sama testikysymyssarja  
            #jatkokehittelyssä tässä kutsutaan harjoitusten drill tason level kysymysten esittämistä
            
            
            while successive_correct < FINISH and not(session._cancelled):
                
                (correctQ, interruptQ, finishQ) = fake_question(level, session, successive_correct)
                #successive_correct viittaa nyt lopetusehtoon, mutta aidossa harjoituksessa voi olla muukin lopetusehto kuin 
                #peräkkäisten vastausten lukumäärä.

                session._new_attempt()
                #Ainakin yritetty vastata
                
                #Näitä muutetaan meneillä olevan harjoituksen mukaisesti
                if interruptQ:
                    print("keskeytys")
                    input("Enter jatka")
                    session._cancelled = True
                else: 
                    if not(correctQ): 
                        print("Väärin")                                    
                    else:
                        print("Oikein") 
                        #correct(session)
                        session._correct_up()  
                        successive_correct += 1 
                    if finishQ:                                       
                        #Lopetusehdon toteutuessa siirrytään seuraavalle tasolle
                        #Tässä testauksessa riittää vastata kaksi kertaa 1, joka tulkitaan oikeaksi vastaukseksi

                        update_total(trainee, session) #tämä ehkä syytä vaihtaa metodiksi   
                
                        #siirrytään seuravalla tasolle
                        #session_level_up(session)
                        session._level_up()
                
            if session._cancelled:
                update_total(trainee, session)     #tämä ehkä syytä vaihtaa metodiksi   

#TODO varsinaisen harjoituksen koodaaminen    

def fake_question(level, session, successive_correct):
    os.system('clear')    
    print("Nämä eivät ole todellisia tehtäviä, vaan leikkikysymyksiä ohjelmarungon testaamiseksi.")
    print(f"Harjoitus 2, taso {level} ")
    print("---------------------------------------")
    print(session)
    print("Peräkkäisiä oikeita", successive_correct)
    print("Vastaamalla muuta kuin 0 tai 1 keskeytät harjoituksen tekemisen")

    answer = input(" testi, vastaa 0 tai 1 : 0 väärin, 1 oikein, muu keskeytys > ")     

    correctQ = (answer == str(1))
    interruptQ = (answer not in [str(0),str(1)])           
    finishQ = correctQ and successive_correct == FINISH - 1
    #Nämä todellisessa tilanteessa määräytyvät meneillä olevasta harjoituksesta ja kysymyksestä
    return(correctQ, interruptQ, finishQ)
