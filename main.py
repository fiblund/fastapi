from typing import Optional
from fastapi import FastAPI, Request

import requests
import json

from pprint import pprint

import pytz
from datetime import datetime, timezone
from tzlocal import get_localzone

PST = pytz.timezone('US/Pacific')
EST = pytz.timezone('US/Eastern')
JST = pytz.timezone('Asia/Tokyo')
NZST = pytz.timezone("Pacific/Auckland")

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/astros")
def astross():
    people = requests.get('http://api.open-notify.org/astros.json')
    if people.status_code == 200:
        return json.loads(people.text)
    else:
        return {"status": "Error"}


@app.get("/iss-now")
def iss_now():
    iss_now = requests.get('http://api.open-notify.org/iss-now.json')
    if iss_now.status_code == 200:
        return json.loads(iss_now.text)
    else:
        return {"status": "Error"}


@app.get("/iss-pass")
def iss_pass():
    iss_pass = requests.get('http://api.open-notify.org/iss-pass.json')
    if iss_pass.status_code == 200:
        return json.loads(iss_pass.text)
    else:
        return {"status": "Error"}


@app.get("/myip")
def myip(request: Request):
    client_ip = request.client.host
    return {"client_ip": client_ip}


@app.get("/datetime-now")
def datetime_now():

    utc_dt = datetime.now(timezone.utc)

    nzst_dt = ("New Zealand time: {}".format(utc_dt.astimezone(NZST).isoformat()))
    return {nzst_dt}


@app.get("/items/{item_id}")
def read_item(item_id: int, query: Optional[str] = None):
    return {"item_id": item_id, "query": query}
