import telebot
from telebot import types

token = "7272016644:AAFl6J_u0zlwbUXS7LVNFCFkZ6e-5m-Dh0w"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.chat.id,
        'Здравствуйте! Это бот с информацией по всем ЖК компании Setl Group в Красносельском районе города Санкт-Петербург. \n\nЧтобы посмотреть информацию по вашему ЖК нажмите\n"/check"',
    )


@bot.message_handler(commands=["check"])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Солнечный город. Резиденции")
    markup.add(item1)
    item2 = types.KeyboardButton("Солнечный город")
    markup.add(item2)
    item3 = types.KeyboardButton("Дворцовый фасад")
    markup.add(item3)
    bot.send_message(message.chat.id, "Выберите ваш ЖК", reply_markup=markup)


@bot.message_handler(content_types="text")
def message_reply(message):
    if message.text == "Солнечный город. Резиденции":
        bot.send_message(
            message.chat.id,
            "https://setlgroup.ru/projects/solnechnyi-gorod-rezidentsiya",
        )
    if message.text == "Солнечный город":
        bot.send_message(
            message.chat.id, "https://setlgroup.ru/projects/solnechnyi-gorod"
        )
    if message.text == "Дворцовый фасад":
        bot.send_message(
            message.chat.id, "https://setlgroup.ru/projects/dvortsovyi-fasad"
        )


bot.infinity_polling()
