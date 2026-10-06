import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://quotes.toscrape.com/' 
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

quotes = []
for item in soup.find_all('span', class_='text'):
    quotes.append(item.text)

df = pd.DataFrame({'Quotes': quotes})
df.to_csv('my_quotes.csv', index=False)

print("സക്സസ്! ഡാറ്റ സേവ് ആയിട്ടുണ്ട്.")
