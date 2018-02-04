# Please note that this isn't 100% accurate
# Not liable for any delays or incorrect prices

import json
import urllib.request as ul
import ctypes
import time


BTC_MIN = 10000  # lowerbound to check against in CAD
BTC_MAX = 11000  # upperbound to check against in CAD
TIME_DELAY = 60  # how often prices should be checked in seconds


def get_btc_price():
    square = 'https://coinsquare.io/?method=book&ticker=CAD&base=BTC'  # change this for different currencies
    square_data = json.load(ul.urlopen(square))
    square_last = square_data['book'][0]['prc']
    cad_ubtc = 0.000001 * float(square_last)/100
    btc_cad = (1/cad_ubtc)
    return btc_cad  # this returns the CAD equivalent of 1 BTC


def displayMessage(msg, value):
    if msg=='max':
        message = "It's time to sell out. \n BTC Price: " + str(value)
        ctypes.windll.user32.MessageBoxW(0, message, "BTC Spiked", 1)
    else:
        message = "It's time to sell out. \n BTC Price: " + str(value)
        ctypes.windll.user32.MessageBoxW(0, message, "BTC Crashed", 1)


while(True):
    curr_btc_price = get_btc_price()
    print("Current BTC: " + str(curr_btc_price) + " CAD")
    if curr_btc_price >= BTC_MAX:
        displayMessage('max', curr_btc_price)
        break

    elif curr_btc_price <= BTC_MIN:
        displayMessage('min', curr_btc_price)
        break
    else:
        time.sleep(TIME_DELAY)