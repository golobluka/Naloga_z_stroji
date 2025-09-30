import time
import json


from stroji import Stroj


def nalozi_stroje_iz_json(pot_do_datoteke: str):
    with open(pot_do_datoteke, 'r', encoding='utf-8') as f:
        konfiguracija = json.load(f)
    return [Stroj(**stroj) for stroj in konfiguracija]


def simuliraj(stroji):
    while True:
        for stroj in stroji:
            stroj.posodobi_temperaturo_in_stanje()
            time.sleep(0.1) 
