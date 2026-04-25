import telebot
import random
import os

# Pega o token da variável de ambiente (mais seguro)
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    print("ERRO: BOT_TOKEN não encontrado!")
    exit()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🎉 Bot online no Render.com!\n\nTeste /ajuda ou /piada")

@bot.message_handler(commands=['ajuda'])
def send_help(message):
    bot.reply_to(message, "Comandos disponíveis:\n/start\n/ajuda\n/piada")

@bot.message_handler(commands=['piada'])
def send_joke(message):
    piadas = [
        "Por que o livro de matemática estava triste? Porque tinha muitos problemas! 📚",
        "O que o pato disse pro outro pato? Estamos quack quack! 🦆",
        "Por que o computador foi ao médico? Porque estava com vírus! 💻"
    ]
    bot.reply_to(message, random.choice(piadas))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Você disse: {message.text}")

print("🤖 Bot iniciado com polling!")
bot.polling(none_stop=True)
