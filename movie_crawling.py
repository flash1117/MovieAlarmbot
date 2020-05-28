import requests
import telegram
from bs4 import BeautifulSoup

bot = telegram.Bot(token = 'token number')

url = 'http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200528'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

#title_list = soup.select('div.info-movie')
#for i in title_list:
#    print(i.select_one('a > strong').text.strip())

imax = soup.select_one('span.gold')
if(imax):
    imax = imax.find_parent('div', class_='col-times')
    title = imax.select_one('div.info-movie > a > strong').text.strip()
#   print(title + 'IMAX 예매가 열렸습니다.')
    bot.sendMessage(chat_id = 1141123839, text = title + 'IMAX 예매가 열렸습니다.')

else:
    bot.sendMessage(chat_id = 1141123839, text = 'IMAX 예매가 아직 열리지 않았습니다.')
