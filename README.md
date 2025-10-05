# Naloga_z_stroji

To je majhna programerska naloga, ki sem jo izvedel pri podjetju *AFlabs*. Spodaj so navodila za izvedbo in navodila za zagon v Dockerju.

## Zagon

Zaženeš z 'docker-compose build' in nato 'docker-compose up'. Potem v ukazni vrstici dobiš povezavo do spletnega strežnika (izbran je port 8000).


## Struktura

Imamo stroje z naslednjimi lastnostmi

- Stroj ima identifiktor (unikatna stevilka/string/...)
- Stroj je lahko prižgan ali ugasnjen
- Stroj ima temperaturo
- Stroj ima najvišjo toleranco temperature
- Stroj vsako sekundo 10x sporoči svojo temperaturo

## Konfiguracija

V neki obliki (npr json, yaml, ...) lahko zapišemo konfiguracijo strojev, ki poleg vseh lastnoti stroja vsebuje še podatek o tem kdaj je stroj prižgan in kdaj je ugasnjen (npr kot uro). Format naj podpira tudi možnost, da je stroj vedno prižgan ali pa vedno ugasnjen.

## Potek

Napiši program, ki bo simuliral poljubno število strojev z zgornjo strukturo v realnem casu (simuliraj npr s funkcijo time.sleep) po naslednjih pravilih:

- Stroj sproči temperaturo po naslednjem postopku če je prižgan:
  - 50% časa se temperatura poveča za 1
  - 40% časa se temperatura pomanjša za 1 ce je višja kot nek minimalni parameter (recimo 22)
  - 10% časa temperatura ostane enaka
- Če je stroj ugasnjen se vsako sekundo temperatura zniža za 1
- Če temperatura stroja presega toleranco se stroj ugasne
- Če temperatura stroja ne presega (tolerance - 10) se stroj prižge in upošteva konfiguracijo

Pripravi api streznik z uporabo knjiznice `fastapi`, ki ima naslednje poti

- GET /api/v0/konfiguracija - vse konfiguracije
- GET /api/v0/konfiguracija/id - konfiguracija za stroj z indikatorjem
- GET /api/v0/log/id - log za stroj z indikatorjem

## Program

Loči program na več vsebinskih delov, npr:

- Del s stroji
- Del ki prebere konfiguracijske datoteke in pripravi vse potrebno za simulacijo
- Del ki simulira zgornji program glede na neke vhodne podatke

Pripravi konfiguracijo za vsaj 5 strojev, ki uporabi vse možnosti, ki jih podpira izbran format za konfiguracijo.

## Pakiranje aplikacije

Napisi `Dockerfile`, ki zapakira aplikacijo in `docker-compose.yaml`, ki bo omogocal:

- Branje konfiguracijskih datotek iz izvornega sistema
- Dostop do api streznika na nekem lokalnem portu
- Uporaba dodanega Dockerfila za grajenje docker slike, ki se uporabi za poganjanje sistema




Zaženeš z 'docker-compose build' in nato 'docker-compose up'.
