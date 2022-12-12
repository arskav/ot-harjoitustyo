# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/arskav/ot-harjoitustyo/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source


## Ohjelman käynnistäminen

Asenna ensin riippuvuudet komennolla

> poetry install

Suorita alustustoimenpiteet komennolla

> poetry run invoke build

Ohjelman voi tämän jälkeen käynnistää komennolla

> poetry run invoke start

## Kirjautuminen

Sovellus käynnistyy kirjautumisnäkymään

> Anna käyttäjätunnus (vähintään viisi merkkiä)

Sovellus ei kysy salasanaa. Jos annat käyttäjätunnuksen, joka on jo käytössä, sovellus toteaa, että jos et itse ole rekisteröinyt tunnusta, kirjaudu uudelleen eri tunnuksella.

Kirjautumisen jälkeen avautuu valikko, jonka yläreunassa ilmoitetaan käyttäjätunnuksen harjoituksissa tekemät vastausyritykset ja oikeiden vastausten lukumäärä ja mahdolliset aloitetut ja loppuun asti tehdyt harjoitukset. Valikossa voi valita seuraavat toimenpiteet

> O : Ohje (O-kirjain) 
> X : Lopetus  
> Y : Ylläpito (vaatii salasanan)  
> 1 : Kirjoitettujen lukujen ilmaiseminen numeroilla  
> 2 : Peruslaskutoimitusten harjoittelua kirjoitetuin numeroin  
> 3 : Sanallisia peruslaskuharjoituksia (pari esimerkkiä)  
> 4 : Yhtälön ratkaisun alkeita

Valintojen 'O', 'Y' ja 'X', joka lopettaa ohjelman suorittamisen, yhteydessä ei erotella isoja ja pieniä kirjaimia. Valinnan 'O' tuottamat ohjeet ovat vielä varsin suppeat.

Valinta 'Y' ei toistaiseksi vaadi salasanaa. Se antaa valikon, jolla voi tulostaa erilaista tilastotietoa sovelluksen käytöstä:

> 1:   kaikki käyttäjänimet  
> 2:   kaikki käyttäjät harjoitustietoineen  
> 3:   kaikki suoritukset  
> 4:   kaikki annetun käyttäjän suoritukset  
> 5:   kaikki annetun harjoituksen suoritukset

Suoraviivaisin näistä on 3, joka tulostaa kaikki sovelluksen käyttäjät ja heidän tekemänsä harjoitustensa eri tasojen tulokset.

Varsinainen harjoitus valitaaan päävalikosta numeroilla 1, 2, 3 tai 4. Näkymä vaihtelee harjoituksittain, mutta yleisesti esitellään tehtävä ja pyydetään siihen vastausta. 

Jos vastaa oikein,
sovellus kysyy harjoituksen meneillä olevan tason seuraavan kysymyksen tai jos peräkkäisiä oikeita vastauksia on tarpeeksi (testauksen nopeuttamiseksi vaatimukseksi on asetettu nyt 2 peräkkäistä oikeaa vastausta), mahdollistetaan harjoituksen lopetus kirjaimella 'X' (tai 'x'). 

Jos vastaa väärin, sovellus kertoo oikean vastauksen ja joissakin harjoituksissa antaa lisäksi ohjeet, miten oikea vastaus lasketaan. Tämän jälkeen kysytään uusi kysymys.

Jos haluaa keskeyttää harjoituksen kysymyksen yhteydessä, tämä onnistuu vastaamalla jotain muuta kuin mitä tehtävässä ohjeistetaan antamaan vastaukseksi. Esimerkiksi pelkkä rivinsiirto (Enter) keskeyttää harjoituksen tekemisen.

Joissakin harjoituksissa on käytössä 'laskin' eli vastaukseksi voi syöttää merkillä '=' alkavan laskutoimituksia +, -, * ja / sisältävän lausekkeen ja sovellus laskee (syntaktisesti oikein muodostetun) lausekkeen arvon. Esimerkiksi Esimerkiksi =2*(3+4) tai = (4 - 2) / -2.


Kun keskeyttää tai lopettaa harjoituksen tai siirtyy harjoituksen seuraavalla tasolle, harjoituksen meneillään olevaa tasoa vastaavat tiedot (kuinka monta yritystä, kuinka moni oikein) tallennetaan tietokantaan. Aloitettaessa harjoituksen tekeminen uudelleen tiedot haetaan tietokannasta ja harjoitusta voi jatkaa tasolta, minne pääsi.

Aloitetut harjoitukset tallennetaan myös tietokantaan ja samoin käyttäjän loppuun asti (eli kaikki tasot) tekemät harjoitukset. Loppuun asti tehtyä harjoitusta ei voi tehdä enää samalla käyttäjätunnuksella uudelleen. Myöskään paluu harjoituksen aikaisemmille tasoille ei ole mahdollista samaa käyttäjätunnusta käytettäessä.












