import requests   ## requests is used to open or get directed to urls
from bs4 import BeautifulSoup
import smtplib
URL = 'Product URL' ##INSERT YOUR PRODUCT URL

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'}  ##User-Agent gives us some information about the browser we are using.

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')  ##This will give complete info about the url page we gave

    title = soup.find(id="productTitle").get_text() ##provides us with product name available
    price = soup.find(id="priceblock_ourprice").get_text() ##provides us with product price available
    converted_price = float(price[0:5]) 

    if(converted_price < 50.99):
        send_mail()

    print(converted_price)
    print(title.strip())  

    if(converted_price < 50.99):
        send_mail()

    def send_mail():
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('Your Mail-ID','PASSWORD')

        subject = 'Price Fell Down!'
        body = 'Check the amazon link '

        msg = f"Subject:{subject}\n\n{body}"

        server.sendmail(
            'MAIL-1(From)',
            'MAIL-2(To)',
            msg
        )
        print('HEY EMAIL HAS BEEN SENT!')

        server.quit()

while(True):
    check_price()
    time.sleep(60)       
