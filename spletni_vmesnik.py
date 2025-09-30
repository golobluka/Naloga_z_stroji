from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import RedirectResponse


stroji = None #Ta globalna spremenljivka bo kasneje spremenjena iz 'main.py'.

#Oblike podatkov na spletnem vmesniku.
class Konfiguracija(BaseModel):
    identifikator: str
    najvisja_toleranca_temperature: float
    urnik: str | list
    temperatura: float
    min_temperatura: float
    je_prizgan: bool

class LogOblika(BaseModel):
    cas: str
    temperatura: float
    je_prizgan: bool

    

app = FastAPI()


#Spletne strani, kot so opisane v navodilih.
@app.get("/api/v0/konfiguracija", response_model=list[Konfiguracija])
async def get_vse_konfiguracije():
    return [Konfiguracija(
        identifikator=s.identifikator,
        najvisja_toleranca_temperature=s.najvisja_toleranca_temperature,
        urnik=s.urnik,
        temperatura=s.temperatura, 
        min_temperatura=s.min_temperatura,
        je_prizgan=s.je_prizgan) for s in stroji]

@app.get("/api/v0/konfiguracija/{identifikator}", response_model=Konfiguracija)
async def get_konfiguracija_po_id(identifikator: str):
    imena_strojev = [stroj.identifikator for stroj in stroji]
    stroji_dict = {stroj.identifikator: stroj for stroj in stroji}

    s = stroji_dict[identifikator]
    return Konfiguracija(
        identifikator=s.identifikator,
        najvisja_toleranca_temperature=s.najvisja_toleranca_temperature,
        urnik=s.urnik,
        temperatura=s.temperatura,
        min_temperatura=s.min_temperatura,
        je_prizgan = s.je_prizgan
    )

@app.get("/api/v0/log/{identifikator}", response_model=list[LogOblika])
async def get_log_po_id(identifikator: str):

    stroji_dict = {stroj.identifikator: stroj for stroj in stroji}

    return [LogOblika(**vnos) for vnos in stroji_dict[identifikator].log]

@app.get("/")  # Za lažjo uporabo takoj preusmerimo na konfiguracije.
async def redirect_to_konfiguracija():
    return RedirectResponse(url="/api/v0/konfiguracija")

