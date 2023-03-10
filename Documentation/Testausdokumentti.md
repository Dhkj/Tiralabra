# Testausdokumentti

## Testikattavuusraportti

[![codecov](https://codecov.io/gh/Dhkj/Tiralabra/branch/main/graph/badge.svg?token=GGQ60FH4C3)](https://codecov.io/gh/Dhkj/Tiralabra)

## Testatut osa-alueet

- Testattu kauttaaltaan jokaista ohjelman sovelluslogiikan metodia useilla sekä hylkäyksen että hyväksynnän antavilla syötteillä.
- Kutakin metodia ja testitapausta testattu useilla eri ja eri suuruisilla syötteillä.
- Testattu ohjelmaa kauttaaltaan sen kokoisilla luvuilla, joilla sovelluksessa operoidaan (500 - 4500 bittiä).
- Käytetty testauksessa Mersennen alkulukuja sekä suuria tunnettuja alkulukuja välillä 300 - 1000 desimaalia.
- Lisäksi testattu 1000 unicode-merkin enkryptaus/dekryptaus.
- Testattu myös sadan satunnaisesti generoidun kymmenen merkin merkkijonon enkryptauksen/dekryptauksen toimivuus.
- Testattu salaus ja purku satunnaisilla täysimittaisilla merkkijonoilla (alle 1024 bittiä = 40 Unicode-merkkiä).
- Testattu salaus ja purku sadalla satunnaisella täysimittaisella merkkijonolla käyttäen kahta eri testiä ja testaustapaa.
- Testattu salaus ja purku käyttäen sataa satunnaisesti generoitua avainparia ja testattu kutakin avainparia sadalla satunnaisella täysimittaisella merkkijonolla.

## Suorituskykytestit

- Testattu salaus ja purku käyttäen sataa satunnaisesti generoitua avainparia ja testattu kutakin avainparia sadalla satunnaisella täysimittaisella merkkijonolla.
- Yhteensä sadan avainparin generointi ja 100*100 = 10 000 täysimittaisen merkkijonon testi.
- Kokonaissuoritusaika noin 65 - 70s.
- Yhden täysimittaisen merkkijonon enkryptaukseen/dekryptaukseen kuluva aika: 6,5 - 7,0ms (sisältäen osittain avaimen generoinnin).

## Testien ajaminen

Ohjelman testit voidaan suorittaa komennolla:

```poetry run pytest src```

Ohjelman haarautumakattavuus voidaan testata komennolla:

```poetry run coverage run --branch -m pytest src```

Ohjelman testikattavuusraportti voidaan luoda komennolla:

```poetry run coverage report -m```

## Koodin laadun seuranta

Ohjelman laatutarkastukset voidaan suorittaa komennolla:

```poetry run pylint src```

## Lähteet

Testauksessa käytettyjä tunnettuja alkulukuja
```https://primes.utm.edu/lists/small/small3.html#300```
```https://primes.utm.edu/curios/index.php?start=301&stop=1000```
