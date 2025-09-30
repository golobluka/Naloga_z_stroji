import time
import random
from datetime import datetime, time as dt_time

class Stroj:
    identifikator: str
    je_prizgan: bool
    temperatura: float
    najvisja_toleranca_temperature: float
    urnik: str | list  # String je v primeru za: 'vedno_prizgan' ali 'vedno_ugasnjen', sicer pa je seznam slovajev s ključema 'začetek' in 'konec'. 
    min_temperatura: float
    log: list  # Seznam z trojicami, ki se pomikajo skozi čas (cas, temperatura, stanje)

    def __init__(self,identifikator: str, 
                 najvisja_toleranca_temperature: float,
                 urnik: str | list,
                 zacetna_temperatura: float = 0.0,
                 min_temperatura: float = 22.0):
        self.identifikator = identifikator
        self.je_prizgan = False
        self.temperatura = zacetna_temperatura
        self.najvisja_toleranca_temperature = najvisja_toleranca_temperature
        self.urnik = urnik
        self.min_temperatura = min_temperatura
        self.log = []  # Inicializiraj prazen log
        self.prekurjen = False
        
        self.rocno_stikalo()

    def rocno_stikalo(self):
        trenutni_cas: dt_time = datetime.now().time() #Vrne čas v sekundah
        

        if self.urnik == "vedno_prizgan":
            self.je_prizgan = True
        elif self.urnik == "vedno_ugasnjen":
            self.je_prizgan = False
        elif isinstance(self.urnik, list):
            self.je_prizgan = False
            for interval in self.urnik:
                zacetek = datetime.strptime(interval["zacetek"], "%H:%M").time() #Vrne čas v sekundah
                konec = datetime.strptime(interval["konec"], "%H:%M").time()
                if zacetek <= trenutni_cas <= konec:
                    self.je_prizgan = True
                    break
        else:
            raise ValueError(f"Neznan format urnika: {self.urnik}")


    def posodobi_temperaturo_in_stanje(self): #To se bo zgodilo v vsaki desetinki sekunde.
        if not self.prekurjen:
            self.rocno_stikalo() 

        if self.je_prizgan:
            rand = random.random() 
            if rand < 0.5:
                self.temperatura += 1
            elif rand < 0.9:
                if self.temperatura > self.min_temperatura:
                    self.temperatura -= 1
            else:
                pass #Temperatura ostane enaka
        else:
            if self.temperatura > self.min_temperatura: #Ni napisano, ali tudi tukaj upoštevamo minimalno temperaturo??
                self.temperatura -= 0.1 #Mogoče malo prilagojeno, vsako sekundo se mora zmanjšati za ena.

        if self.temperatura > self.najvisja_toleranca_temperature:
            self.je_prizgan = False
            self.prekurjen = True

        if self.temperatura < (self.najvisja_toleranca_temperature - 10):
            self.prekurjen = False



        #Posodobimo zgodovino
        self.log.append({
            "cas": datetime.now().strftime('%Y:%m:%d:%H:%M'),
            "temperatura": self.temperatura,
            "je_prizgan": self.je_prizgan
        })