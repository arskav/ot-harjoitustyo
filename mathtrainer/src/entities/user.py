class MathTrainerUser:   
            
    def __init__(self, username, started, finished, correct, tries): 
        self._user = username
        self._practise_started = started
        self._practise_finished = finished
        self._correct_total = correct
        self._tries_total = tries
       

    def __str__(self):
        #Tulostus ainakin päävalikon yhteydessä
        string = "Käyttäjätunnus: " + self._user 
        string += "\n" + "Yrityksiä kaikissa harjoituksissa " + str(self._tries_total) + ", joista "
        string += "oikeita vastauksia " + str(self._correct_total) + "\n"
        if self._practise_started != []:
            string += "Aloitettu harjoitukset "
            for i in self._practise_started:
                string += str(i) + ", "     
            if self._practise_finished != []:
                string += "tehty loppuun harjoitukset "
                #pilkutuksen vuoksi mutkikkaampi kuin yllä
                for i in range(len(self._practise_finished)):
                    string += str(self._practise_finished[i])
                    if i < len(self._practise_finished) - 1:
                        string += ", "    
            else:
                string += "ei loppuun tehtyjä harjoituksia. "                       
        else:
            string += "Ei aloitettuja harjoituksia."            
            
        return string
