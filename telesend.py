import requests
def botmsg(bot_message):
    bot_token = '5033997656:AAHcGq2QaeKPclqzNhP2msPxYVpaJiXgvx8'
    bot_chatID = '2025063834'#LEGEND
    #bot_chatID1 = '1688134885'#rio
    #bot_chatID1 = '548521105'#siva
    #314516752
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    #send_text1='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID1 + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    # response1 = requests.get(send_text1)
    return response.json()

