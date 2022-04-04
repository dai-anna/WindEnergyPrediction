import requests
from fastapi import FastAPI, Request
import uvicorn
import json

application = FastAPI()


@application.get("/")
def root(req: Request):
    query_params = dict(req.query_params)
    location = query_params["location"]
    days = query_params["days"]
    r = requests.get(
        "https://api.weatherapi.com/v1/forecast.json?key=7ba8aae77c1847bdb34232330220304&q={}&days={}&aqi=no&alerts=no".format(
            location, days
        )
    )
    f_data = r.json()['forecast']['forecastday'][0]['hour']
    lst = []
    for i in range(24):
        lst.append((i,f_data[i]['wind_mph']))
    
    return json.dumps({"wind_mph":lst})


if __name__ == "__main__":
    uvicorn.run(application, port=8080, host="0.0.0.0")
