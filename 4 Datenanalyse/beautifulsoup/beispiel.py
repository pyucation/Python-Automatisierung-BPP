import requests
from bs4 import BeautifulSoup


with open('4 Datenanalyse/website.html', 'r', encoding='utf-8') as file:
    content = file.read()

# HTML parsen
soup = BeautifulSoup(content, 'html.parser')
script = soup.find_all('script')[0].string

print("JavaScript-Code gefunden:")
print(script)
