#Apualiohjelmia
#Tämä tyhejntyi ja on melkein jo turha






def return_to_menu():
    #vakiokysymys vaiheessa, jossa jonkun harjoituksen tietyn tason kysymykset on tehty 
    print("X: Lopetetaan harjoittelu ja palataan päävalikkoon")
    print("Mikä tahansa muu: jatka harjoittelua seuraavalla tasolla.")                
    ans = input("X/muu > ")
    return(ans.upper())
