from fastapi import FastAPI
import uvicorn
from datetime import datetime
import re
from data import get_date_data

app = FastAPI(title='RP API')

def validate(date_text):
    try:
        datetime.strptime(date_text, '%d_%m_%Y')
        print (date_text)
        return(True)
    except ValueError:
        return(False)

@app.get('/')
async def root():
    return 'Use /data/today or /data/date/04_01_2022'

@app.get('/data/today/')
async def get_today():
    return get_date_data(datetime.now().strftime('%d_%m_%Y'))

@app.get('/data/date/{date}')
async def get_spec_day(date: str):
    if validate(date):
        return get_date_data(date)
    else:
        return 'Invalid date format. Must be dd-mm-yyyy'

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port='5000')