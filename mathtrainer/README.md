# Mathtrainer

Sovelluksen avulla käyttäjät voivat harjoitella peruskoulun matemaattisia tehtäviä. 

Pääpaino on sanallissa matemaattisissa peruslaskutoimituksia sisältävissä tehtävissä. Suomea vieraana kieltä puhuville on suomenkielisten matemaattisten ilmausten ymmärtämistä harjoittavia tehtäviä. Ennen varsinaisia sanallisia tehtäviä harjoitellaan lausekkeiden arvojen määrittämistä ja alkeellisia yhtälön ratkaisutehtäviä.

## Python-versio

Sovellus on tehty käyttämällä Python-versiota 3.9., mutta testattu Python-versiolla 3.8.

## Dokumentaatio

* [käyttöohje](https://github.com/arskav/ot-harjoitustyo/blob/main/mathtrainer/dokumentaatio/kayttoohje.md)

* [Vaativuusmäärittely](https://github.com/arskav/ot-harjoitustyo/blob/main/mathtrainer/dokumentaatio/vaativuusmaarittely.md)

* [Arkkitehtuurikuvaus](https://github.com/arskav/ot-harjoitustyo/blob/main/mathtrainer/dokumentaatio/arkkitehtuuri.md)

* [Testausdokumentti (tällä hetkellä vain testauskattavuus)](https://github.com/arskav/ot-harjoitustyo/blob/main/mathtrainer/dokumentaatio/testaus.md)

* [Työaikakirjanpito](https://github.com/arskav/ot-harjoitustyo/blob/main/mathtrainer/dokumentaatio/tuntikirjanpito.md)

* [Changelog](https://github.com/arskav/ot-harjoitustyo/blob/main/mathtrainer/dokumentaatio/changelog.md)

## Releas

[Viimeisin release](https://github.com/arskav/ot-harjoitustyo/releases/tag/loppupalautus)

## Asennus

Asenna riippuvuudet komennolla

> poetry install

Suorita tietokantojen alustustoimenpiteen komennolla

> poetry run invoke build

Käynnistä ohjelma komennolla

> poetry run invoke start


## Komentorivitoiminnot

### Ohjelman suorittaminen

> poetry run invoke start

### Testaus

> poetry run invoke test

### Testikattavuus

> poetry run invoke coverage-report

Raportti generoituu _htmlcov_-hakemistoon.


### Pylint

Tiedoston [.pylintrc](https://github.com/arskav/ot-harjoitustyo/blob/main/mathtrainer/.pylintrc) mukaiset tarkistukset

> poetry run invoke lint

