import requests
import itertools
import smtplib
import html
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NUMBER_OF_TOP_NEWS = 3
My_EMAIL = ""  # -----------> * you should insert your email address here
MY_PASSWORD = ""    # -----------> * you should insert your app email password here
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Message details
from_addr = My_EMAIL
to_addr = My_EMAIL


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_top_news():
    api_key_news = "005ec26c70704951ac3c34d3c7706581"
    end_point_news = "https://newsapi.org/v2/everything"
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": api_key_news,
    }
    responses_news = requests.get(end_point_news, params=news_parameters)
    responses_news.raise_for_status()
    news_list = [({"title": responses_news.json()["articles"][num]["title"]},
                  {"content": responses_news.json()["articles"][num]["description"]})
                 for num in range(NUMBER_OF_TOP_NEWS)]
    return news_list


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

api_key = "GFVH72GR0O2PETJO"
end_point_api = "https://www.alphavantage.co/query?"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key,
}
response = requests.get(end_point_api, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
two_days = dict(itertools.islice(data.items(), 2))
data_dic = [[key, float(two_days[key]["4. close"])] for key in two_days]
difference_percentage = ((data_dic[1][1] - data_dic[0][1]) / data_dic[1][1]) * 100
print(difference_percentage)
if abs(difference_percentage) > 1:
    print(get_top_news())

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


connection = smtplib.SMTP(host="smtp.gmail.com")
connection.starttls()
if difference_percentage > 0:
    arrow = "🔺"
else:
    arrow = "🔻"
email_text = get_top_news()
print(email_text)
subject = "Stock news"
body = f"TESLA: {arrow} {'{:.2f}'.format(difference_percentage)}%\n"
for num in range(NUMBER_OF_TOP_NEWS):
    body = body + f"Headline:{email_text[num][0]['title']}\nBrief:{email_text[num][1]['content']}\n\n"

message_text = html.unescape(body)
print(body)
# Create a multipart message
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
try:
    # Set up the SMTP server
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        # Log in to your email account
        server.login(My_EMAIL, MY_PASSWORD)
        # Send the email
        server.sendmail(from_addr, to_addr, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print("Error sending email:", str(e))
