from bs4 import BeautifulSoup
import urllib.request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint



#1


url = "https://www.doviz.com/bitcoin"
url_oku = urllib.request.urlopen(url)
soup = BeautifulSoup(url_oku, 'html.parser')

#Burada "span" ve "color-red" kısımı sitedeki verinin yerini belirtiyor.
vericek = soup.find_all('span',attrs={'class':'color-red'})





#2

scope = ['https://spreadsheets.google.com/feeds']
#Burada ise google drive api ile oluşturduğumuz ve indirdiğimiz dosyanın adını yazıyoruz (ben adını değiştirdim !)
creds = ServiceAccountCredentials.from_json_keyfile_name('pythonornek.json', scope)
client = gspread.authorize(creds)

#Burada google drive da oluşturduğumuz dökümanın adını yazıyoruz.
sheet = client.open("veriler").sheet1


#3

pp=pprint.PrettyPrinter()

#hücreye gidiyoruz ve içini yazdırıyoruz
result = sheet.cell(1, 1).value
pp.pprint(result)


#4

#cektigimiz veri ile hücreyi degistirelim

sheet.update_cell(1,1, vericek[0].text)
