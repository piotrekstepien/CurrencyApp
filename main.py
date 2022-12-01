from datetime import date
import PySimpleGUI as sg
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def get_date_list(url):  # returns period of time as a list of strings
    date_dict = get_exchange_rate(url)
    date_list = list(date_dict)
    return date_list


def get_exchange_rate(url):
    response = requests.get(url)
    dictionary_ = response.json()
    list_ = dictionary_["rates"]
    dict_ = {}
    date_ = []
    value_ = []
    for item in list_:
        date_.append(item["effectiveDate"])
        value_.append(item["mid"])
    for item in range(0, len(value_)):
        dict_[date_[item]] = value_[item]
    return dict_


def get_currency_as_list(
        url):  # reformats currency exchange rate from a dictionary to a list -> useful for current value of exchange reate
    currency_dict = get_exchange_rate(url)
    currency_list = list(currency_dict.values())
    return currency_list


def get_currency_ratio(currency_1, currency_2):  # returns ratio of any currencies as a list in specific time period
    ratio = []
    for i in range(0, len(currency_1)):
        ratio.append(round(currency_1[i] / currency_2[i], 4))
    return ratio


today = date.today()
url_usd = "http://api.nbp.pl/api/exchangerates/rates/A/USD/2022-01-01/" + f"{today}"
url_eur = "http://api.nbp.pl/api/exchangerates/rates/A/EUR/2022-01-01/" + f"{today}"
url_bgn = "http://api.nbp.pl/api/exchangerates/rates/A/BGN/2022-01-01/" + f"{today}"

usd_list = get_currency_as_list(url_usd)
eur_list = get_currency_as_list(url_eur)
bgn_list = get_currency_as_list(url_bgn)

usd_to_eur = get_currency_ratio(usd_list, eur_list)

#
# # Builds GUI:
# layout = [
#     [sg.Push(), sg.Text(today), sg.Text(font="Calibre 16", key="-TEXT-", enable_events=True), sg.Push()],
#     [sg.Push(), sg.Button("USD", key="-USD-"), sg.Button("EUR", key="-EUR-"), sg.Button("USD/EUR", key="-RATE-"),
#      sg.Push()]
# ]
# window = sg.Window("USDtoEUR V0.0.1", layout)
plt.plot(get_date_list(url_eur), usd_to_eur)
plt.show()
# while True:
#     event, values = window.read()
#     if event == sg.WINDOW_CLOSED:
#         break
#     if event == "-USD-":
#         window["-TEXT-"].update(usd)
#     if event == "-EUR-":
#         window["-TEXT-"].update(eur)
#     if event == "-RATE-":
#         window["-TEXT-"].update(rate)
# window.close()
