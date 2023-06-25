import telebot
import parser_market
import settings

bot = telebot.TeleBot(settings.API_KEY)

@bot.message_handler(commands = ["start"])
def start(message):
	bot.send_message(message.chat.id, "Привет, чтобы получить курс криптовалюты"
		" напиши пару криптовалюты, например, BTCUSDT")


@bot.message_handler()
def start(message):
	res = parser_market.binance_bybit(message.text)
	if type(res) == dict:
		for i in res.values():
			bot.send_message(message.chat.id, i)
	else:
		bot.send_message(message.chat.id, res)
	

bot.polling()



