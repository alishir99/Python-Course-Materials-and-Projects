import requests
from twilio.rest import Client
import datetime as dt
today=dt.datetime.today()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MY_API_KEY = "N79ID5UVJ0N90W7R"
URL = "https://www.alphavantage.co/query"
account_sid ="AC5376766960e1e6d93cd4862503bdf524"
auth_token ="d6fcd6c0d26033f99c81b07cb6a3ad98"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameteter = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey":MY_API_KEY,
}
response = requests.get(URL, params=parameteter)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
today_close_price =float( data_list[0]["4. close"])
yesterday_close_price =float(data_list[1]["4. close"])
stock_diff = (today_close_price/yesterday_close_price)

percentage = round((stock_diff-1)*100,2)
print(percentage)

def up_or_down(n):
    if n>0:
        return f"🔺{n}%"
    else:
        return f"🔻{n}%"

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
MY_NEWS_API_KEY = "364f86f182eb4bff9fc97995d3e60e8f"
parameteters = {
    "q": COMPANY_NAME,
    "sortBy":"popularity",
    "category":"business",
    "apiKey":MY_NEWS_API_KEY,
    "country":"us",
}

response = requests.get("https://newsapi.org/v2/top-headlines", params=parameteters)
response.raise_for_status()
news_data= response.json()
if percentage <=-2 or percentage>=2:
    news_list = news_data["articles"]
    three_articles = news_list[:3]


    message_to_send = [f'TSLA: {up_or_down(percentage)}'
                       f'\nHeadline: {i["title"]}'
                       f'\n link: {i["url"]}'
                       for i in three_articles]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

    client = Client(account_sid, auth_token)
    for to_send in message_to_send:
        message = client.messages \
        .create(
            body=f'TSLA: {to_send}',
            from_ = "+17088093573",
            to= "+46793323636"
        )
        print(message.status)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

