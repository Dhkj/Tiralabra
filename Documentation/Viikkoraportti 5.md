# Tällä viikolla olen:

- Opiskellut lisää aihealueeseen liittyen.

- Havaittu virhe modulaarisen tulon käänteisluvun määrittämisen toteuttavassa metodissa.
- Algoritmi toimii pienillä luvuilla, mutta aiheuttaa toisinaan virheen isoilla luvuilla, jolloin palautettu luku ei ole modulaarinen tulon käänteisluku.
- Implementoitu ja kokeiltu toteutusta vaihtoehtoista algoritmia hyödyntäen, mutta virhe säilyy.
- Lisätty siten avainparin generoivaan metodiin tarkistus, että kyseessä on todella modulaarinen tulon käänteisluku, ja mikäli ei, arvotaan uusi avainpari.
- Toteutus lienee ok.

- Lisätty testejä viikon 4 palautteen ohjeistuksen mukaan:
  1) Lisätty kaikkiin testeihin testitapaukset ja testattu ohjelmaa kauttaaltaan sen kokoisilla luvuilla, joilla sovelluksessa operoidaan.
  2) Testattu salaus ja purku satunnaisilla täysimittaisilla merkkijonoilla (siis vajaat 1024 bittiä), että palautuu alkuperäiseen.
- Pythonin dokumentaation mukaan Unicode-merkistö olisi koodattu käyttäen 24 bittiä, jolloin täysimittainen alle 1024-bitin merkkijono muodostuisi enintään 42 merkistä.
- Toteutettu testit käyttäen 40 unicode-merkin pituisia merkkijonoja.
- Toteutus lienee ok.


- Toteutettu ensimmäinen vertaisarvio.

- Päivitetty dokumentaatiota.


# Mitä opin tällä viikolla:

- Opin lisää aihealueeseen liittyvästä teoriasta, matematiikasta sekä algoritmeista.



# Mitä teen seuraavaksi:

- Nyt ohjelma olisi kokonaisuudessaan valmis ja toimii virheettömästi.
- Ohjelma generoi 1024-bittisen rsa-avainparin ja pystyy enkryptamaan ja dekryptaamaan kaikkia unicode-merkistön viestejä.


# Kysymyksiä ja huomioita:

1) Todellinen avaimen pituus käytetyllä menetelmällä on 1023-1024 bittiä. Tämä on luultavasti ok.

2) Viestin enkrypraus ja dekryptaus on toteutettu enkryptaamalla ja dekryptaamalla viesti merkki kerrallaan. Tämä toteutus lienee ok.

3) Toteutettu viikon 4 palautteessa ohjeistetut testit. Testit lienevät nyt ok.


- Kiitos kaikista mahdollisista lisähuomioistasi, kommenteistasi ja mahdollisesta jatko-ohjeistuksesta!


# Käytetty työaika:

10h. (Käytetty myös ylimääräistä aikaa aihealueen tutkimiseen.)
