# Stock News Notifier

The Stock News Notifier is a Python script that fetches the latest stock price data and related news for a given company, and sends the information as an SMS message. It uses the Alpha Vantage API for stock data and the News API for news data, and sends SMS using the Twilio API.

## Features

- Fetches the latest stock price data for a specified company.
- Retrieves recent news articles related to the company.
- Sends an SMS message containing the stock price change and headlines of the latest news articles.

## How to use

1. The script is executed by running the command `python3 stock_news_notifier.py` (or `python stock_news_notifier.py` depending on your Python setup) in the terminal.
2. The script will fetch stock data and news for the company specified in the `get_news("TSLA")` function call at the bottom of the script.

## Dependencies

This project uses the following libraries and APIs:

- `requests`: a popular Python library used for making HTTP requests.
- Alpha Vantage API: to get stock price data.
- News API: to fetch the latest news articles.
- Twilio API: to send SMS messages.

## API Keys and Tokens

The script requires API keys for Alpha Vantage and News API, and the Account SID and Auth Token for your Twilio account. These should be added where the corresponding variables are defined in the script.

```python
api_key = "your_alpha_vantage_api_key"
news_api_key = "your_news_api_key"
twilio_account_sid = "your_twilio_account_sid"
twilio_auth_token = "your_twilio_auth_token"
```

## Disclaimer

This script is for educational purposes only. Always verify financial data from trusted sources before making investment decisions.

## Future Enhancements

- Parameterize the company symbol so it can be entered at runtime.
- Add exception handling for API calls.

