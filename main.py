import telegram

api_key = '985545259:AAF8vaxtq_M-Xw4R5KrFTDeSyn_T4QuA9dI'

bot = telegram.Bot(token=api_key)

#chat_id = bot.get_updates()[-1].message.chat_id
chat_id = 677188660

bot.sendMessage(chat_id = chat_id, text = '안녕하세요')