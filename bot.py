#from telegram import Update
#from telegram.ext import Updater, CommandHandler, CallbackContext
#import os

import requests
from pprint import pprint
from bs4 import BeautifulSoup

 def getMeaning(text):
        # create url
        url = 'https://www.oxfordlearnersdictionaries.com/definition/english/' + text
        # get page
        page = requests.get(url)
        # let's soup the page
        soup = BeautifulSoup(page.text, 'html.parser')
        pprint(soup)
	
	
	word = 'Mathematics'
	word = word.strip()
	getMeaning(word.lower())



#def start(update: Update, context: CallbackContext) -> None:
  #  update.message.reply_text(f'Olá, {update.effective_user.first_name}!\nJosemaria aqui 🙋‍♂️ \nSalve Maria Santíssima e viva Cristo Rei.')

#updater = Updater(os.environ.get("TOKEN"), use_context=True)

#updater.dispatcher.add_handler(CommandHandler('start', start))

#print("Bot started successfully")

#updater.start_polling()
#updater.idle()
