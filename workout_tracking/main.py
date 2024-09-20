import requests
import os
from datetime import datetime

date_now = datetime.now().strftime("%d/%m/%y")
time_now = datetime.now().strftime("%X")

APP_ID ="0254972d"
API_KEY = "ead537eeb5b6a501051bd98322469e1d"
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_GET = "https://api.sheety.co/alishirzad444@gmail.com/workoutTrucking/sheet1"
SHEETY_POST = "https://api.sheety.co/dcb6ae0b86991adf285021859f2b13fa/workoutTrucking/sheet1"
MY_TOKEN = "Bearer sadhljhasdlkh233423§1§lhhlad(()=??()//T(=?=`JHshkd2575"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}

body = {
    "query": input("Tell me which exercises you did: ").lower(),
    "gender": "Male",
    "weight_kg": "78",
    "height_cm": "178",
    "age": "24",

}

response = requests.post(url=ENDPOINT, json=body, headers=headers)
result = response.json()
print(result)
headers = {
    "Authorization": MY_TOKEN,
}
for excercise in result["exercises"]:
    parameters = {
        "sheet1":{
         "date": date_now,
         "time": time_now,
         "exercise": excercise["name"].title(),
         "duration": int(excercise["duration_min"]),
         "calories": int(excercise["nf_calories"])

        }
    }

    send = requests.post(url=SHEETY_POST, json=parameters, headers=headers)
    print (send.text)


#
