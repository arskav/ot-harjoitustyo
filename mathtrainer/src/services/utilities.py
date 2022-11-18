#Apualiohjelmia


#Harjoituksiin liittyen

def update_total(trainee, session):
    #Päivitetään kokonaistilanne
    trainee._correct_total += session._correct_at_level
    trainee._tries_total += session._tries_at_level    


def return_to_menu():
    #vakiokysymys vaiheessa, jossa jonkun harjoituksen tietyn tason kysymykset on tehty 
    print("X: Lopetetaan harjoittelu ja palataan päävalikkoon")
    print("Mikä tahansa muu: jatka harjoittelua seuraavalla tasolla.")                
    ans = input("X/muu > ")
    return(ans.upper())
