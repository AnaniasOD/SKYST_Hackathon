from fastapi import FastAPI, File, UploadFile, Request, Query, Form
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import uvicorn

app = FastAPI()

@app.post('/upload')
async def upload(file: UploadFile = File(...)):
    df_bro = pd.read_csv('cal_bro.csv')
    df_dad = pd.read_csv('cal_dad.csv')
    df_mom = pd.read_csv('cal_mom.csv')

    if file.filename.endswith('.csv'):
        empty_day = []
        df = pd.read_csv(file.file)
        for i in range(len(df)):
            if df_bro["일정"][i] == 'x' & df_dad["일정"][i] == 'x' & df_mom["일정"][i] == 'x' & df["일정"][i] == 'x':
                empty_day.append(df["날짜"][i])
            else:
                continue
        print(empty_day[:3])
        global empty
        empty = empty_day[:3]
        return empty_day[:3]

html_list = []

@app.post("/submit_radio")
async def submit_radio(choice: str = Form(...)):
    html_list.append(choice)
    available_days = [3,2,3]
    
    for i in range(3):
        if available_days[i] == 3:
            date = str(empty[i])
            if date in html_list:
                final_day = [int(date[:4]),int(date[4:6]),int(date[6:8])]
            else:
                continue
        else:
            continue

    return final_day

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*", "http://localhost:5500"],
)

