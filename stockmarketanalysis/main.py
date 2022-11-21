# By: Ryan Alumkal and Christian F.

import requests
from bs4 import BeautifulSoup

# maybe create a graph? or create a GUI that updates live?

URL = [
"https://www.google.com/finance/quote/TSLA:NASDAQ?hl=en", 
"https://www.google.com/finance/quote/AAPL:NASDAQ?hl=en",
"https://www.google.com/finance/quote/NFLX:NASDAQ?hl=en",
"https://www.google.com/finance/quote/GOOGL:NASDAQ?hl=en",
"https://www.google.com/finance/quote/SHOP:NYSE?hl=en",
"https://www.google.com/finance/quote/FAZE:NASDAQ?hl=en",
"https://www.google.com/finance/quote/BTC-USD?hl=en" # does not work, fix 
]

def main():
    try:
        soup = BeautifulSoup(page.text, "html.parser")
        
        company = soup.find('div',{'class': 'zzDege'}).text

        ticker = soup.find('div', {'class': 'PdOqHc'}).text.split(' ')[0].replace('Home', '').split('•')[0] # Get company from Home > COMPANY • PLATFORM

        platform = soup.find('div', {'class': 'PdOqHc'}).text.split(' ')[2].split('•')[0] # Get platform from Home > COMPANY • PLATFORM
        
        price = soup.find('div', {'class': 'YMlKec fxKbKc'} ).text

        after_hours_down = soup.find('span', {'class': 'JwB6zf'}).text # after hours percentage, 
        
        ytd_soup = BeautifulSoup(requests.get(URL[i] + '&window=YTD').text, "html.parser")

       # Prices
        YTD = ytd_soup.find('div', {'class': 'JwB6zf'}).text

        after_hours_down = soup.find('span', {'class': 'JwB6zf'}).text # after hours percentage, change to current percentage
        print(f"\nCompany: {company}")
        print(f"Ticker: {ticker}, trading on {platform}")
        print(f"Price: {price}")
        print(f"After Hours:{after_hours_down}")
        print(f"Year To Date: {YTD}")

    except:
        print(f"Error with {URL[i]}")

if __name__ == '__main__':
    for i in range(len(URL)):
        page = requests.get(URL[i])
        main()
