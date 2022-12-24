# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät voivat harjoitella peruskoulun matemaattisia tehtäviä peruslaskutoimituksista yhtälöiden ratkaisemiseen.

Pääpaino on sanallisissa matemaattisissa peruslaskutoimituksia sisältävissä tehtävissä. Suomea vieraana kieltä puhuville on suomenkielisten matemaattisten ilmausten ymmärtämistä harjoittavia tehtäviä.


## Käyttäjät

_Normaali käyttäjä_ pystyy kirjautumaan järjestelmään tarvittaessa luoden uuden tunnuksen.


_Pääkäyttäjä_ pystyy tulostamaan erilaisia yhteenvetoja ja tilastoja käyttäjien harjoitteluista. Pääkäyttäjä pystyy myös poistamaan käyttäjätunnuksen ja siihen liittyvät tiedot harjoittelusta.

## Käyttöliittymä

Ohjelmaa aloitettaessa kysytään tunnusta. Jos tunnusta ei vielä ole, se luodaan tässä vaiheessa.

Tämän jälkeen avautuu valikko, jossa on valittavissa eri harjoituksia. Valikosta voi avat myös pääkäyttäjälle tarkoitetun ylläpitotoimintojen valikon. Jokaiselle harjoitukselle on oma käyttöliittymä, jossa huomioitu tehtävien luonne.

## Perusversio

Ohjelmarunkoon on helppo lisätä erilaisia harjoituskokonaisuuksia ja kasvattaa harjoituskokonaisuuden tehtävien lukumäärää. Perusversiossa on suomea vieraana kielenä puhuville tarkoitettu harjoitus, jossa suomeksi kirjoitettua lukuja ilmaistaan numeroina, ja toinen harjoitus, jossa esitetään yhteen-, vähennys-, kerto- ja jakolaskutehtäviä sanallisesti. Kolmas harjoitus on esimerkki parista sanallisesta matematiikan tehtävästä. Neljäs harjoitus johdattaa yksinkertaisten yhtälöiden ratkaisemiseen.

Kun käyttäjä kirjautuu järjestelmään vanhalla tunnuksella, hän näkee tilastotietoa harjoitteluistaan: alkuvaiheessa harjoituskokonaisuudet, mitkä hän aloittanut ja mitkä tehnyt loppuun, sekä kuinka monta yksittäistä tehtävää hän on yrittänyt tehdä ja kuinka moni on mennyt oikein.

Harjoituskokonaisuudessa on tasoja. Käyttäjä aloittaa helpoimmista tehtävistä. Harjoituskokonaisuudessa on asetettu ehdot sille, miten siirrytään tasolta ylemmäs. Ehdot voivat vaihdella eri tasoilla.

Harjoituskokonaisuuden yhteydessä pidetään kirjaa siitä, miten tehtävät etenevät ja reaaliaikainen tilanne näytetään käyttäjälle. Kun harjoittelu lopetetaan, tiedot tallennetaan tietokantaan ja käyttäjän kirjautuessa sovellukseen vanhana käyttäjänä hänen tietonsa haetaan tietokannasta.

Kun käyttäjä on tehnyt kaikki vaativamman tason tehtävät, harjoituskokonaisuus on tehty, eikä käyttäjä voi enää samalla tunnuksella siihen palata. Käyttäjä voi kuitenkin tehdä uuden tunnuksen ja palata jo tekemiinsä harjoituksiin.


## Jatkokehittelyä

Ensimmäinen jatkotavoite on toteuttaa ohjelman pääkäyttöliitymä ja yksittäisten harjoitusten käyttöliittymä graafisena käyttöliittymänä. Toinen välitön jatkotavoite on yhdenmukaistaa harjoitusten koodaustapaa niin, että se vastaa nykyisen harjoituksen 3 tapaa.

Tämän jälkeen on tarkoitus luoda erityisesti sellaisia tehtävämuotoja, jotka eroavat Moodlen tarjoamista ja testata niiden toimivuutta (oikeastaan kiinnostavuutta) sopivalla kohderyhmällä. Kun on löydetty toimivia harjoittelumuotoja, on ajatuksena toteuttaa lisää harjoittelukokonaisuuksia kirjoittamani oppimateriaalin [Matematiikan perustiedot](https://homepages.tuni.fi/ari.virtanen/peruskoulumatikkaa.pdf) mukaisesti.

Jos tämä etenee suotuisasti, niin ohjelmasta on tarkoitus tehdä web-sovellus (harrastuksena tai ehkä jonkun toisen opintojakson yhteydessä). Välitavoitteena on tehdä ohjelmasta versio, joka toimii Windows-koneissa ns. standalone sovelluksena. Tarkoitus on myös kehittää pääkäyttäjälle apuohjelmia, jotka osittain automatisoivat uusien harjoitustehtävien lisäämistä.






