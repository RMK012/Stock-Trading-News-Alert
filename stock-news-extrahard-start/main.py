
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

import requests

from twilio.rest import Client

def get_news(ticker):
    # Step 1: Get the stock price change
    api_key = "TRFCJRX5JPEJ4B42"
    stock_url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={api_key}"
    response = requests.get(stock_url)
    stock_data = response.json()
    print(stock_data)
    yesterday_price = float(stock_data["Global Quote"]["03. high"])
    day_before_yesterday_price = float(stock_data["Global Quote"]["04. low"])
    change_percent = ((yesterday_price - day_before_yesterday_price) / day_before_yesterday_price) * 100
    print(change_percent)

    # Step 2: Get the first 3 news articles for the company
    news_api_key = "f475fbd6db174b5abfbea6f2e0cf00b6"
    news_url = f"https://newsapi.org/v2/everything?q={ticker}&apiKey={news_api_key}"
    news_response = requests.get(news_url)
    news_data = news_response.json()
    articles = news_data["articles"][:3]

    # Step 3: Send SMS with the news and stock change
    twilio_account_sid = "AC7883e82b30ed24bcc4fd36b3b4a09ba1"
    twilio_auth_token = "cc2a3db3b9a2ecfcfa5e3f48c284d3dc"
    client = Client(twilio_account_sid, twilio_auth_token)
    message = f"{ticker}: "
    if change_percent > 0:
        message += "🔺"
    else:
        message += "🔻"
    message += f"{change_percent:.2f}%\n"
    for article in articles:
        message += f"Headline: {article['title']}\nBrief: {article['description']}\n"
    client.messages.create(to="+972542072785", from_="+13512473948", body=message)

get_news("TSLA")
