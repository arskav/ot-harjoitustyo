# Arkkitehtuurikuvaus

![Pakkausrakenne](./kuvat/viikko4.png)


Tapahtumat, kun kirjautunut asiakas: MathTrainerUser on valinnut päävalikosta harjoitukset harj, jota asiakas ei ole tehnyt loppuun, mutta on aloittanut. 

```mermaid
    sequenceDiagram
    participant UI
    participant mathtraineruser
    participant harjoitussessio   
    UI ->> asiakas: begin_practising(asiakas, harj)
    asiakas -->> UI: practise_finished(harj) False
    asiakas -->> UI: practise_started(harj) True
    UI ->> session_repositio: find_session_of_user(asiakas, harj)
    session_repositio -->> UI: asiakkaan harjoituksen viimeisimmän session tiedot 
    UI ->> harjoitussessio: MathTrainerSession(asiakas, harjoituksen tiedot)
    UI ->> harjoitussessio: begin_practise(asiakas)
    harjoitussessio ->> harj: harj.question
    harj -->> harjoitussessio: is_correct, is_cancelled, is_finish
```
Kun on tehty yksi harjoituksen harj kysymyksistä, jatko määräytyy sen mukaan, onko vastaus oikein, keskeytettiinkö harjoituksen tekeminen ja (kun vastaus on oikein) tehtiinkö harjoituksen taso loppuun.

    

