from bs4 import BeautifulSoup 
import requests 
import fake_useragent 
 
user = fake_useragent.FakeUserAgent().random 
 
headers = { 
 
    'user-agent' : user 
} 
prompt = 'what+is+hse+university'
pages = 1

link = f'https://yandex.ru/search/?text={prompt}' 
    
response = requests.get(link, headers= headers) 
    
soup = BeautifulSoup(response.text, 'lxml') 
formated_html = soup.prettify() 
    
links = soup.find_all('a', class_ = 'Link Link_theme_normal OrganicTitle-Link organic__url link') 
    
for item in links: 
    link = item.get('href') 
    print(link) 
     
