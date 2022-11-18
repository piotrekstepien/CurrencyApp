from datetime import date
import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
import requests
from  datetime import date

url = "https://dskbank.bg"
session = requests.Session()
session.headers[
    "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) 107.0.5304.87 Safari/537.36"
html = session.get(url)

tabela = bs(html.text, "html.parser")
data = tabela.find("div", class_ = "currency-box__inner"). find_all("td")
today = date.today()
# for td in data:
#     print(td.text)
usd = round((float(data[1].text)+ float(data[2].text))/2, 4)

eur = (float(data[10].text)+ float(data[11].text))/2

rate = round((usd/eur),4)
#print(rate)


layout = [
    [sg.Push(), sg.Text(font= "Calibre 16", key = "-TEXT-", enable_events= True),sg.Push()],
[sg.Multiline("HERE WILL BE GRAPH \n Press any button", size=(50,20), no_scrollbar= True, justification="center")],
    [sg.Push(), sg.Button("USD", key = "-USD-"), sg.Button("EUR", key = "-EUR-"), sg.Button("USD/EUR", key = "-RATE-"), sg.Push()]
]
window = sg.Window("USDtoEUR V0.0.1", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "-USD-":
        window["-TEXT-"].update(usd)
    if event == "-EUR-":
        window["-TEXT-"].update(eur)
    if event == "-RATE-":
        window["-TEXT-"].update(rate)
window.close()
