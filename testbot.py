import datetime
import requests

url = 'https://api.telegram.org/bot516691485:AAEoJSlhnpjNTAUMSU7l5ZQBh7Mcj0DTElc/'



#Поиск последнего сообщения из массива чата с пользователем Telegram.
def lastUpdate (dataEnd):
    res = dataEnd['result']
    totalUpdates = len(res) - 1
    return res[totalUpdates]

#Получение идентификатора чата Telegram
def getChatID (update):
    chatID = update['message']['chat']['id']
    return chatID

#отправка запроса sendMessage боту
def sendResp (chat, value):
    settings = {'chat_id':chat, 'text':value}
    resp = requests.post(url + 'sendMessage', data = settings)
    return resp

#Get-запрос на обновление информации к боту. Результат – строка json. Метод .json

def getUpdatesJson (request):
    settings = {'timeout': 100, 'offset': None}
    responce = requests.get(request + 'getUpdates', data = settings)
    return responce.json()


def main ():
    chatID = getChatID(lastUpdate(getUpdatesJson(url)))
    sendResp(chatID, 'Ваше сообщение')
    updateID = lastUpdate(getUpdatesJson(url))['update_id']

    while True:
        if updateID == lastUpdate(getUpdatesJson(url))['update_id']:
            sendResp(getChatID(lastUpdate(getUpdatesJson(url))),'Nice try')
            updateID +=1


if __name__ == '__main__':
    main()
