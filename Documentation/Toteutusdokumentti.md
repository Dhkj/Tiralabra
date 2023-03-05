# Toteutusdokumentti

## Ohjelman yleisrakenne

### Ohjelma koostuu:
1. Käyttöliittymästä.
2. Avainten generoimisesta vastaavasta luokasta.
3. Syötteiden enkryptauksesta ja dekryptauksesta vastaavasta luokasta.
4. Algoritmeista vastaavasta luokasta.

## Ohjelman käyttäminen ja toiminta:

### Käynnistys

- Ohjelma generoi 1024-bittisen RSA-avainparin ohjelman käynnistyksen yhteydessä.
- Ohjelma tulostaa generoidun RSA-avainparin ohjelman suorituksen alussa.

### Käyttäminen
1. Käyttäjä voi käyttöliittymän valikosta generoida uusia RSA-avainpareja, jotka myös tulostetaan käyttäjälle.
2. Käyttäjä voi valita annetun syötteen enkryptaamisen tai dekryptaamisen.
    - Enkryptatut ja dekryptatut syötteet tulostetaan käyttäjälle.
3. Käyttäjä voi sulkea ohjelman.

### Muuta
- Käyttäjän antamien virheellisten syötteiden mahdollisuus on estetty.

## Teoriaa:

### Ohjelman toiminta perustuu seuraaviin algoritmeihin:

I) RSA-avainparin generointi (Lähde 1):
  1. Select a value of e from (3, 5, 17, 257,) 65537
  2. repeat
  3.    p ← genprime(k/2)
  4. until (p mod e) ≠ 1
  5. repeat
  6.    q ← genprime(k - k/2)
  7. until (q mod e) ≠ 1
  8. N ← pq
  9. L ← (p-1)(q-1)
  10. d ← modinv(e, L)
  11. return (N, e, d)

II) Satunnaisten alkulukujen generoiminen hyödyntää Miller-Rabinin algoritmia satunnaisten lukujen alkulukuisuuden testaamiseen. (Lähde 2)

III) Modulaarisen tulon käänteisluvun määrittämiseen on hyödynnetty laajennettua Euklideen algoritmia.

### Lähteet

#### (Lähde 1:) RSA key pair generation algorithm
```https://www.di-mgt.com.au/rsa_alg.html```

#### (Lähde 2:) Miller-Rabin primality test algorithm
```https://gist.github.com/Ayrx/5884790```

#### (Lähde 3:) Testauksessa käytettyjä tunnettuja alkulukuja
```https://primes.utm.edu/lists/small/small3.html#300```
```https://primes.utm.edu/curios/index.php?start=301&stop=1000```
