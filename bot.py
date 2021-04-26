from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
symbols = ['!', '@', '#', '$', '%', ',', '.', '^', ':', ';', '&', '?', '<', '>', '\\']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.


def start(update, context):
    update.message.reply_text("Это бот-калькулятор. Он умеет вычислять простые и сложные выражения.\n"
                              "Вводите выражение в одну строку и отправляйте одним сообщением.\n"
                              "Не используйте других знаков, кроме арабских цифр и символов "
                              ' - ,  + ,  * ,  / ,  **n (возведение в степень),  (   ) .')


def echo(update, context):
    print(update.message.text)
    if update.message.text[-2] == '/' and update.message.text[-1] == '0':
        update.message.reply_text(f'Error')
    for i in update.message.text.split():
        flag = False
        for j in i:
            if j.isalpha() or j in symbols:
                update.message.reply_text(f'Error')
                break
            if j in nums:
                flag = True
        if not flag:
            update.message.reply_text(f'Error')
    update.message.reply_text(f'{eval(update.message.text)}')


def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater('1767778845:AAEvevOykVA53QvD9pW2P6nZB1GVRUbrCUU', use_context=True)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(text_handler)
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()