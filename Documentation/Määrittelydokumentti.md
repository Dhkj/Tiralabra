# Määrittelydokumentti

## Kurssin hallinnointi
- Opinto-ohjelma: TKT

## Käytetty kieli
- Dokumentaatio: suomi
- Koodi ja kommentit: englanti

## Ohjelmointikielet

- Käytetty ohjelmointikieli: Python
- Muut hallitut kielet: Java

## Ohjelman tarkoitus ja ratkaistava ongelma

1. 1024-bittisen RSA-avainparin generointi.
2. Käyttäjän antamien syötteiden enkryptaaminen sekä dekryptaaminen.

## Ohjelman toteuttamat algoritmit:

1. Miller–Rabin primality test
  - Käytetään satunnaisten suurien alkulukujen generoimiseen.
  - Algoritmi on probabilistinen ja tuottaa virheellisen arvion parametrina annetun luvun alkulukuisuudesta korkeintaan todennäköisyydellä 1/2.
  - Suorittamalla algoritmi lukuisia kertoja peräkkäin voidaan siten todennäköisyys virheellisen suuren alkuluvun generoimiselle saada häviävän pieneksi.
      ((Lähde, kaava))
      
2. Laajennettu Euklideen algoritmi
  - Algoritmi tuottaa annettujen parametrien suurimman yhteisen tekijän sekä toisena annetun parametrin modulaarisen tulonkäänteisluvun.

3. Carmichael's totient functionin arvon ja least common multiplen laskennassa hyödynnetään laajennettua Euklideen algoritmia.

4. Neliöönkorotusalgoritmi
  - Suurten modulaarieksponenttien laskeminen.
  - Hyödynnetty pythonin valmista funktiota pow().


## Ohjelman toiminta

### RSA-avainparin generointi

1. Ohjelma generoi kaksi suurta alkulukua
  - Metodi generoi satunnaisen suuren parittoman kokonaisluvun annetulla toivottua avaimen pituutta vastaavalla välillä.
  - Metodi testaa kokonaisluvun alkulukuisuutta Miller–Rabinin alkulukutestillä.
  - Mikäli kokonaisluku ei ole alkuluku, kasvatetaan kokonaislukua kahdella tuottaen aina uuden parittoman kokonaisluvun, jonka alkulukuisuutta jälleen testataan.
  - Metodin suoritus on erittäin tehokas ja vaatii keskimäärin 200 yritystä (lähde, kaava).

2. Ohjelma laskee generoitujen kahden suuren alkuluvun tulon n = p * q, jonka pituus on käytetyn avaimen pituus.

3. lambda_n

4. e

5. d

### Enkryptaus ja dekryptaus
- Ohjelma saa käyttäjältä syötteitä, joita käyttäjä voi enkryptata ja dekryptata.

### Lähteet

