import threading
import uvicorn

from simulacija import simuliraj, nalozi_stroje_iz_json

from spletni_vmesnik import app
import spletni_vmesnik


# Naliži stroje
stroji = nalozi_stroje_iz_json("zacetno_stanje.json")
spletni_vmesnik.stroji = stroji

#Zaženi simulacijo
paralelni_proces = threading.Thread(target=simuliraj, args=(stroji,), daemon=True)
paralelni_proces.start()

#Zaženi spletni vmesnik
uvicorn.run(app, host="0.0.0.0", port=8000)

