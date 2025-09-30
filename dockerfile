
FROM python:3.10

WORKDIR /naloga_z_stroji

COPY main.py simulacija.py spletni_vmesnik.py stroji.py requirements.txt zacetno_stanje.json /naloga_z_stroji/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]