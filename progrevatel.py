import telebot
from telebot import types

token=''
bot=telebot.TeleBot(token)
#подключил бота

#cписки фраз
privet = ["здравствуйте", "привет", "добрый день", "здравствуйтеб майор иванов", "здравствуйте, слушаю", "слушаю", "говорите", "что случилось?"]

#тут я генерирую кнопки отображаемые в интефейсе на вход подается мессадж, название 2х кнопок, и текст выдаваемый пользователю
def button_gen (message, button_name1,button_name2,message_text):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(button_name1)
    item2 = types.KeyboardButton(button_name2)
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, text=message_text, reply_markup=markup)


#приветсвенное собщение
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Проверьте себя, сможете ли вы распознать мошенника! ВНИМАНИЕ! Не вводите личных данных и банковские реквизиты. веддите слово "прогрев" если готовы начать')

# Получение сообщений от пользователя
@bot.message_handler(content_types=["text"])
#def handle_text(message):
def func(message):
    if message.text.lower() == ("прогрев"): #lower() превод в нижний регистр
        button_gen(message, "Майор Иванов", "Служба безопасности","Выберите номер сценария")
    elif message.text.lower() == ("майор иванов"):
        button_gen(message, "Здравствуйте, слушаю", "Ой телефон мужа он уехал на работу и забыл его дома", "Здравствуйте вас беспокоит Майор Иванов из Восточнго ГУ МП УГТ по 'Кировскому району' г. Москва. \n Хочу обсудить с вами вопрос связанный с вашим коллегой, \n разговор прошу оставить между нами")
    elif message.text.lower() in privet:
        button_gen(message,"первый раз слышу", "я там не работаю", "У меня буквально несколько вопросов касательно вчерашнего инциндента, с утечкой зарплатных данных")
    elif message.text.lower() == ("ой телефон мужа он уехал на работу и забыл его дома"):
        bot.send_message(message.chat.id, text="хорошая тактика продолжайте в том же духе, всегда давайте неопределенные туманные расплывчатые ответы. \n уклоняйтесь от ответа что бы взять время на подумать")




#постоянный опрос сервера бота
#bot.infinity_poling()
bot.polling(none_stop=True, interval=0)
