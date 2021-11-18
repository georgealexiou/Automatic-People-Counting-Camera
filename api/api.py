from fastapi import FastAPI
import uvicorn
from datetime import datetime

from data import get_date_data


app = FastAPI(title='RP API')

@app.get('/')
async def root():
    return '<h1>Hello</h1>'

@app.get('/data/today/')
async def get_today():
    return get_date_data(datetime.now().strftime('%d_%m_%Y'))

@app.get('/data/date/{date}')
async def get_spec_day(date: str, needy: str):
    if date.matches("\\d{2}_\\d{2}_d{4}"):
        return get_date_data(date)
    else:
        return 'Invalid date format. Must be dd-mm-yyyy'

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port='5000')