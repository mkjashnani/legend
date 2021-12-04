import requests

URL = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}"
def botmsg(bot_message):
    bot_token = '5064671174:AAFTdDwyLtGK55K2k0wIJsioJsV5pzfcUPE'
    bot_chatID = '2025063834'#LEGEND
    #bot_chatID1 = '1688134885'#rio
    #bot_chatID1 = '548521105'#siva
    #314516752
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    #send_text1='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID1 + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    #response1 = requests.get(send_text1)
    return response.json()
def get_price(coin,currency):
    try:
        response = requests.get(URL.format(coin,currency)).json()
        return response
    except:
        return False
while True:
    # date_time = datetime.strftime("%d/%m/%Y %H:%M:%S")
    _current_price = get_price("eth","USD")
    _current_price_1 = get_price("btc", "USD")
    _current_price_2 = get_price("doge", "USD")

    current_price = _current_price['USD']
    current_price_1 =  _current_price_1['USD']
    current_price_2 =  _current_price_2['USD']

    botmsg("Ethereum Price is "+str(current_price)+", Bitcoin Price is "+str(current_price_1)+", Dogecoin Price is "+str(current_price_2))
