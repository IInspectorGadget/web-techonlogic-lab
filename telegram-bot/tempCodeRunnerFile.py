from telegram import Update 
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
import pika


button_help = "Помощь"

#обработчик кнопки
def button_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text = "Помощь",
        reply_markup=ReplyKeyboardRemove(),
    )

#обработчик текста
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_help:
        return button_help_handler(update = update, context = context)


    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body=text)
    connection.close()

    # настройка кнопок
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text = button_help)
            ],
        ],
        resize_keyboard=True,
    )

    #бот пишет сообщение
    update.message.reply_text(
        text = "Привет, нажми кнопку ниже!",
        reply_markup=reply_markup,
    )

def main():
    #подключаемся и ждём сообщений
    updater = Updater(
        token="2113039370:AAFaleJ-uHr-1Fhj_AEaDKyaEeHoDHoEKkM",
        use_context=True,
    )

    #ответ на сообщение
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    #что-то вроде бесконечного цикла
    updater.idle()


if __name__ == '__main__':
    main()


