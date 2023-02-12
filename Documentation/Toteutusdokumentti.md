# Toteutusdokumentti

## Ohjelman yleisrakenne

### Ohjelma koostuu:
1. Käyttöliittymästä.
2. Avainten generoimisesta vastaavasta luokasta.
3. Syötteiden enkryptauksesta ja dekryptauksesta vastaavasta luokasta.
4. Algoritmeista vastaavasta luokasta.

### Ohjelman käyttäminen ja toiminta:

#### Käynnistys

- Ohjelma generoi 1024-bittisen RSA-avainparin ohjelman käynnistyksen yhteydessä.
- Ohjelma tulostaa generoidun RSA-avainparin ohjelman suorituksen alussa.

#### Käyttäminen
1. Käyttäjä voi käyttöliittymän valikosta generoida uusia RSA-avainpareja, jotka myös tulostetaan käyttäjälle.
2. Käyttäjä voi valita annetun syötteen enkryptaamisen tai dekryptaamisen.
    - Enkryptatut ja dekryptatut syötteet tulostetaan käyttäjälle.
3. Käyttäjä voi sulkea ohjelman.

### Muuta
- Käyttäjän antamien virheellisten syötteiden mahdollisuus on estetty.

### Lähteet

#### RSA key pair generation algorithm
```https://www.di-mgt.com.au/rsa_alg.html```

#### Miller-Rabin primality test algorithm
```https://gist.github.com/Ayrx/5884790```



