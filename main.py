import requests
from bs4 import BeautifulSoup
import smtplib
header = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Defined"
}


my_email='test@gmail.com'
password='test'
practice_url = "https://appbrewery.github.io/instant_pot/"
amazon_url='https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=asc_df_B08N5W4NNB/?tag=googleshopdes-21&linkCode=df0&hvadid=709855510254&hvpos=&hvnetw=g&hvrand=10706717538611143725&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9182014&hvtargid=pla-1136686879362&mcid=9ad65b98b6723b2c8aaca1185061d230&gad_source=1&th=1'
response=requests.get(amazon_url,headers=header)
website_html=response.text
print(website_html)
soup=BeautifulSoup(website_html,'html.parser')

price = soup.find(class_="a-offscreen").get_text()
print(price)
price_without_currency = price.split("₹")[1]
price_in_digits = price_without_currency.replace(",", "")
print(price_in_digits)
float_currency = float(price_in_digits)
print(float_currency)

if float_currency<50000:
    print('email alert')
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()  # tls enables for security
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email,
                        msg=f'Amazon Price drop alert \n\nHi, MacBook Air is below 50k')
    connection.close()
else:
    print('price same')
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()  # tls enables for security
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email,
                        msg=f'Subject:Amazon Price Today \n\nHi, MacBook Air is {float_currency}')
    connection.close()

