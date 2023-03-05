# Käyttöohje
## Asennus

1) Lataa ohjelman zip-tiedosto ja pura zip-tiedosto valittuun hakemistoon.
2) Avaa ohjelman juurihakemisto (hakemisto, jossa sijaitsee mm. kansio src) komentoriviltä.
3) Asenna ohjelman riippuvuudet suorittamalla ohjelman juurihakemistossa komento (olettaen, että poetry on asennettuna):

     ```poetry install```

## Käynnistys

Ohjelma voidaan käynnistää ohjelman juurihakemistossa komennolla:

```poetry run python src/index.py```
tai
```poetry run python3 src/index.py```

## Valikko

Ohjelman valikosta käyttäjä voi valita:
1) Uuden 1024-bittisen RSA-avainparin generointi.
   - Ohjelma tulostaa generoidun avainparin: julkinen avain (n,e) + yksityinen avain (d).
2) Käyttäjän viestin enkryptaus. (Maksimipituus 40 merkkiä.)
   - Käyttäjä voi kirjoittaa syötteen.
   - Ohjelma tulostaa enkryptatun käyttäjän syötteen.
3) Enkryptatun viestin dekryptaus.
   - Käyttäjä voi syöttää enkryptatun viestin (= suuri kokonaisluku).
   - Ohjelma tulostaa dekryptatun viestin.
4) Käyttäjä voi sulkea ohjelman.

## Esimerkki ohjelman käyttämisestä

1) Käyttäjä voi käynnistää ohjelman ylläolevalla komentorivikomennolla.
2) Ohjelma generoi ohjelman käynnistyessä avainparin.
   - Käyttäjä voi halutessaan generoida myös uuden avainparin.
3) Generoitu avainpari tallentuu ohjelmaan.
4) Käyttäjä voi valita ohjelman valikosta viestin enkryptauksen, jolloin ohjelma kysyy käyttäjän viestiä.
5) Käyttäjä voi syöttää valitsemansa viestin ohjelmalle.
6) Ohjelma tulostaa käyttäjän syöttämän syötteen enkryptattuna (= suuri kokonaisluku).
7) Käyttäjä voi testata ohjelman toiminnallisuuden esimerkiksi kopioimalla tulostetun enkryptatun viestin, valitsemalla valikosta dekryptauksen ja syöttämällä kopioidun enkryptatun viestin.
8) Ohjelma tulostaa käyttäjän alkuperäisen viestin dekryptattuna.

## Testaus

Ohjelman testit voidaan suorittaa komennolla:

```poetry run pytest src```

Ohjelman haarautumakattavuus voidaan testata komennolla:

```poetry run coverage run -branch -m pytest src```

Ohjelman testikattavuusraportti voidaan luoda komennolla:

```poetry run coverage report -m```

## Laatutarkastukset

Ohjelman laatutarkastukset voidaan suorittaa komennolla:

```poetry run pylint src```

