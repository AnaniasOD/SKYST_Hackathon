from fastapi import FastAPI, File, UploadFile, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import uvicorn

app = FastAPI()
#class Item(BaseModel):
#    data: str

@app.post('/upload')
async def upload(file: UploadFile = File(...)):
    if file.filename.endswith('.csv'):
        empty_day = []
        df = pd.read_csv(file.file)
        for i in range(len(df)):
            if df["일정"][i] == "x":
                empty_day.append(df["날짜"][i])
            else:
                continue
        print(empty_day[:3])
        return empty_day[:3]

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*", "http://localhost:5500"],
)
'''
db = []

class City(BaseModel):
    name: str
    timezone: str

@app.get("/cities")
def get_cities():
    results = []
    for city in db:
        strs = f"https://worldtimeapi.org/timezone/{city['timezone']}"
        r = requests.get(strs)
        cur_time = r.json()['datetime']
        results.append({'name':city['name'], 'timezone':city['timezone'], 'current_time':cur_time })

    return results

@app.get('/cities/{city_id}')
def get_city(city_id: int):
    city = db[city_id-1]
    strs = f"https://worldtimeapi.org/timezone/{city['timezone']}"
    r = requests.get(strs)
    cur_time = r.json()['datetime']

    return {'name':city['name'], 'timezone':city['timezone'], 'current_time':cur_time}

@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())

    return db[-1]

@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
'''

