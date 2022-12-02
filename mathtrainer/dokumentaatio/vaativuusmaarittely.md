# Vaatimuusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät voivat harjoitella peruskoulun matemaattisia tehtäviä. 

Pääpaino on sanallissa matemaattisissa peruslaskutoimituksia sisältävissä tehtävissä. Suomea vieraana kieltä puhuville on suomenkielisten matemaattisten ilmausten ymmärtämistä harjoittavia tehtäviä. Ennen varsinaisia sanallisia tehtäviä harjoitellaan lausekkeiden arvojen määrittämistä ja alkeellisia yhtälön ratkaisutehtäviä.


## Käyttäjät

_Normaali käyttäjä_ pystyy kirjautumaan järjestelmään tarvittaessa luoden uuden tunnuksen. _Tehty._


_Pääkäyttäjä_ pystyy tulostamaan yhteenvetoja kaikkien käyttäjien harjoitteluista. Pääkäyttäjä-toiminta lisätään vasta sitten, kun käyttäjien tiedot tallennetaan tietokantaan.

## Käyttöliittymäluonnos

Ohjelmaa aloitettaessa kysytään tunnusta. Jos tunnusta ei vielä ole, se luodaan tässä vaiheessa. _Tehty._

Tämän jälkeen avautuu valikko, jossa on valittavissa eri harjoituksia. _Tehty._
Jokaiselle harjoitukselle on oma käyttöliittymä, jossa huomioitu tehtävien luonne.

## Perusversio

Tavoitteena on luoda ohjelmarunko, johon on helppo lisätä erilaisia harjoituskokonaisuuksia.

Kun käyttäjä kirjautuu järjestelmään vanhalla tunnuksella, hän näkee tilastotietoa harjoitteluistaan: alkuvaiheessa harjoituskokonaisuudet, mitkä hän aloittanut ja mitkä tehnyt loppuun, sekä kuinka monta yksittäistä tehtävää hän on yrittänyt tehdä ja kuinka moni on mennyt oikein. _Tehty._

Harjoituskokonaisuudessa on tasoja. Käyttäjä aloittaa helpoimmista tehtävistä. Harjoituskokonaisuudessa on asetettu ehdot sille, miten siirrytään tasolta ylemmäs. Ehdot voivat vaihdella eri tasoilla. _Tehty kaksi harjoituskokonaisuutta valmiiksi._

Harjoituskokonaisuuden yhteydessä pidetään kirjaa siitä, miten tehtävät etenevät ja reaaliaikainen tilanne näytetään käyttäjälle. __Tehty osittain, mutta harjoitusta koskevat tiedot nollautuvat aloitettaessa uudelleen. Niitä ei vielä viedä tietokantaan._

Käyttäjä voi keskeyttää harjoittelukokonaisuuden tekemisen. Tällöin harjoituksen tila tallennetaan. Kun käyttäjä palaa harjoitukseen, jatketaan siltä tasolta, mihin hän on päässyt. _Tehty._

Kun käyttäjä on tehnyt kaikki vaativamman tason tehtävät, harjoituskokonaisuus on tehty, eikä käyttäjä voi enää samalla tunnuksella siihen palata. Käyttäjä voi kuitenkin tehdä uuden tunnuksen ja palata jo tekemiinsä harjoituksiin. _Tehty._

Tämän opintojakson yhteydessä tavoitteena on toteuttaa ainakin harjoittelukokonaisuus muuttujista ja yhtälöiden ratkaisemisesta. 

## Jatkokehittelyä

Kun järjestelmään on saatu lisättyä alussa mainitut kolme harjoituskokonaisuutta, on tarkoitus testata harjoitusten toimivuutta testikäyttäjillä. Tarkoitus on luoda erityisesti sellaisia tehtävämuotoja, jotka eroavat Moodlen tarjoamista. (Tosin lausekkeita ja yhtälöitä käsittävässä harjoituskokonaisuudessa tuskin merkittävästi poiketaan Moodlessa olevista tehtävätyypeistä.)

Kun on löydetty toimivia harjoittelumuotoja, on
ajatuksena toteuttaa lisää harjoittelukokonaisuuksia kirjoittamani oppimateriaalin [Matematiikan perustiedot](https://homepages.tuni.fi/ari.virtanen/peruskoulumatikkaa.pdf) mukaisesti.

Jos tämä etenee suotuisasti, niin ohjelmasta on tarkoitus tehdä web-sovellus (harrastuksena tai ehkä jonkun toisen opintojakson yhteydessä). Välitavoitteena on tehdä ohjelmasta versio, joka toimii Windows-koneissa.





