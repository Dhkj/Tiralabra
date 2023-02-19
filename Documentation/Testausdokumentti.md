# Testausdokumentti

## Testikattavuusraportti

[![codecov](https://codecov.io/gh/Dhkj/Tiralabra/branch/main/graph/badge.svg?token=GGQ60FH4C3)](https://codecov.io/gh/Dhkj/Tiralabra)

## Testatut osa-alueet

- Testattu kauttaaltaan jokaista ohjelman sovelluslogiikan metodia useilla sekä hylkäyksen että hyväksynnän antavilla syötteillä.
- Kutakin metodia ja testitapausta testattu useilla eri ja eri suuruisilla syötteillä.
- Testattu ohjelmaa kauttaaltaan sen kokoisilla luvuilla, joilla sovelluksessa operoidaan (500 - 4500 bittiä).
- Lisäksi testattu 1000 unicode-merkin enkryptaus/dekryptaus.
- Testattu myös sadan satunnaisesti generoidun kymmenen merkin merkkijonon enkryptauksen/dekryptauksen toimivuus.
- Testattu salaus ja purku satunnaisilla täysimittaisilla merkkijonoilla (alle 1024 bittiä = 40 Unicode-merkkiä).

## Testien ajaminen

Ohjelman testit voidaan suorittaa komennolla:

```poetry run pytest src/index.py```

Ohjelman haarautumakattavuus voidaan testata komennolla:

```poetry run coverage run -branch -m pytest src```

Ohjelman testikattavuusraportti voidaan luoda komennolla:

```poetry run coverage report -m```

## Koodin laadun seuranta

Ohjelman laatutarkastukset voidaan suorittaa komennolla:

```poetry run pylint src```
