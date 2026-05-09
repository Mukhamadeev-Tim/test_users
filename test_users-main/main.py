# подключение библиотек
import json
from secrets import token_urlsafe

from faker import Faker
from telebot import TeleBot, types

# TODO: вставить свой токен
TOKEN = '8712768760:AAEfLgN3SoSCClbzIVKIT07zPyaiCIO8tA4'
bot = TeleBot(TOKEN, parse_mode='html')

# библиотека для генерации тестовых ФИО
faker = Faker('ru_RU') 

# объект клавиаутры
main_menu_reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

# первый ряд кнопок
main_menu_reply_markup.row(
    types.KeyboardButton(text="1️⃣"), types.KeyboardButton(text="3️⃣")
)

# второй ряд кнопок
main_menu_reply_markup.row(
    types.KeyboardButton(text="5️⃣"), types.KeyboardButton(text="🔟")
)
main_menu_reply_markup.row(
    types.KeyboardButton(text="Репозиторий автора")
)

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_message_handler(message: types.Message):

    # СТИКЕР (добавил правильно)
    with open('sticker.webp', 'rb') as sticker:
        bot.send_sticker(message.chat.id, sticker)

    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id,
        text="Привет!\nЭто бот для генерации тестовых пользователей. "
             "Выбери сколько пользователей тебе нужно 👇🏻",
        reply_markup=main_menu_reply_markup
    )


# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
  if message.text == "Мой репозиторий":
    bot.send_message(message.chat.id, "https://github.com/Mukhamadeev-Tim")
  if message.text == "Написать мне в личку":
    bot.send_message(message.chat.id, "https://t.me/Mukhamadeev_Ti")
    

    payload_len = 0
    if message.text == "1️⃣":
        payload_len = 1
    elif message.text == "3️⃣":
        payload_len = 3
    elif message.text == "5️⃣":
        payload_len = 5
    elif message.text == "🔟":
        payload_len = 10
    else:
        bot.send_message(chat_id=message.chat.id, text="Не понимаю тебя :( ")
        return

    total_payload = []
    for _ in range(payload_len):
        user_info = faker.simple_profile()
        user_info['phone'] = f'+7{faker.msisdn()[3:]}'
        user_info['password'] = token_urlsafe(10)
        total_payload.append(user_info)

    payload_str = json.dumps(
        obj=total_payload,
        indent=2,
        sort_keys=True,
        ensure_ascii=False,
        default=str
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f"Данные {payload_len} тестовых пользователей:\n<code>{payload_str}</code>"
    )

    bot.send_message(
        chat_id=message.chat.id,
        text="Если нужны еще данные, можешь выбрать еще раз 👇🏻",
        reply_markup=main_menu_reply_markup
    )


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()