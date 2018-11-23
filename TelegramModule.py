from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Response_Handler import m_response as get_response

updater = Updater(token='692946616:AAFE7gzrDbkuup0kcZADz-MFmhvMJ70eDho')  # Токен API к Telegram
dispatcher = updater.dispatcher

saved_message = ''


def textMessage(bot, update):
    texting = update.message.text
    response = get_response(texting)
    bot.send_message(chat_id=update.message.chat_id, text=response)


# Хендлеры
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
