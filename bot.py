import os 
from telegram.ext import Updater, CommandHandler


def start(update, context):

    update.message.reply_text('Hola, humano')

if __name__ == '__main__':
    updater = Updater(token='2093019819:AAHg5Ws8BaW4SsXTbYRK2YOe2lRFs4Hir6E', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))


    updater.start_polling()
    updater.idle()