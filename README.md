# Tiralabra

[![workflow](https://github.com/Dhkj/Tiralabra/actions/workflows/main.yml/badge.svg)](https://github.com/Dhkj/Tiralabra/actions)
[![codecov](https://codecov.io/gh/Dhkj/Tiralabra/branch/main/graph/badge.svg?token=GGQ60FH4C3)](https://codecov.io/gh/Dhkj/Tiralabra)

## Dokumentaatio
### Ohjelman dokumentaatio:

[Määrittelydokumentti](https://github.com/Dhkj/Tiralabra/blob/main/Documentation/M%C3%A4%C3%A4rittelydokumentti.md)

[Toteutusdokumentti](https://github.com/Dhkj/Tiralabra/blob/main/Documentation/Toteutusdokumentti.md)

[Testausdokumentti](https://github.com/Dhkj/Tiralabra/blob/main/Documentation/Testausdokumentti.md)

### Viikkoraportit:

[Viikkoraportti 1](https://github.com/Dhkj/Tiralabra/blob/main/Documentation/Viikkoraportti%201.md)

[Viikkoraportti 2](https://github.com/Dhkj/Tiralabra/blob/main/Documentation/Viikkoraportti%202.md)

[Viikkoraportti 3](https://github.com/Dhkj/Tiralabra/blob/main/Documentation/Viikkoraportti%203.md)

## Käyttöohje
### Asennus

Asenna ohjelman riippuvuudet komennolla:

```poetry install```

### Käynnistys

Ohjelma voidaan käynnistää komennolla:

```poetry run python src/index.py```
tai
```poetry run python3 src/index.py```

### Testaus

Ohjelman testit voidaan suorittaa komennolla:

```poetry run pytest src/index.py```

Ohjelman haarautumakattavuus voidaan testata komennolla:

```poetry run coverage run -branch -m pytest src```

Ohjelman testikattavuusraportti voidaan luoda komennolla:

```poetry run coverage report -m```

### Laatutarkastukset

Ohjelman laatutarkastukset voidaan suorittaa komennolla:

```poetry run pylint src```

