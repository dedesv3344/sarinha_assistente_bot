import telebot
import random
import os

# Pega o token da variável de ambiente
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    print("ERRO: BOT_TOKEN não encontrado!")
    exit()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def enviar_boas_vindas(message):
    bot.reply_to(message, "🎉 Bot online!\n\nTeste /ajuda")

@bot.message_handler(commands=['ajuda'])
def enviar_ajuda(message):
    bot.reply_to(message, "Comandos:\n/start\n/ajuda\n/piada")

@bot.message_handler(commands=['piada'])
def enviar_piada(message):
    piadas = [
        "Por que o livro de matemática estava triste? Porque tinha muitos problemas!",
        "O que o pato disse? Quack quack!",
        "Por que o computador foi ao médico? Porque estava com vírus!"
    ]
    bot.reply_to(message, random.choice(piadas))

@bot.message_handler(func=lambda message: True)
def eco_tudo(message):
    bot.reply_to(message, f"Você disse: {message.text}")

print("🤖 Bot iniciado!")
bot.polling(none_stop=True)
