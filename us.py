from bs4 import BeautifulSoup
import requests
import time

url = "https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sca_esv=80879160ea65325f&sca_upv=1&sxsrf=ADLYWIJ-_LQ5cIDjpY2NQR82tUK4i5z9Zg%3A1716368054780&ei=trJNZvKhL4zCwPAP9Y2JwAQ&udm=&oq=dolar&gs_lp=Egxnd3Mtd2l6LXNlcnAiBWRvbGFyKgIIADIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzINEAAYgAQYsAMYQxiKBTINEAAYgAQYsAMYQxiKBUiGDFAAWABwAXgBkAEAmAEAoAEAqgEAuAEByAEAmAIBoAISmAMAiAYBkAYKkgcBMaAHAA&sclient=gws-wiz-serp"
headers = {
    'User-Agent': 'Your user agent'}


page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
convert = soup.find_all('span', {"class": "DFlfde SwHCTb", "data-precision": 2})
usd = convert[0].text
usd1 = '1 $ = '
print(convert[0].text)

