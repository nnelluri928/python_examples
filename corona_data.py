import requests
import bs4 
import pandas as pd
url =' https://www.worldometers.info/coronavirus/country/india/'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text,'lxml')
cases = soup.find_all('div', class_ = 'maincounter-number')
data = []
for i in cases:
    span = i.find('span')
    data.append(span.string)
#create a dataframe
df = pd.DataFrame({'CoronaData': data})
#naming the columns
df.index = ['TotalCases', 'Deaths', 'Recovered']
df.to_csv('Corona_Data.csv')