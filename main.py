from telebot import TeleBot
import g4f

TOKEN = ""  # http API BotFather

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    print(message)
    bot.send_message(message.chat.id, "Bot use model chatgpt3.5")


@bot.message_handler(func=lambda message: True)
def answer(message):
    print(message)
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            messages=[{"role": "user", "content": message.text}],
        )
        bot.send_message(message.chat.id, response)
    except:
        bot.send_message(message.chat.id, "repeat message")


bot.infinity_polling()
