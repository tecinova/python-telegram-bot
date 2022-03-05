#from telegram import Update
#from telegram.ext import Updater, CommandHandler, CallbackContext
#import os


from bs4 import BeautifulSoup
	import requests
	from pprint import pprint

	def getMeaning(text):
	    # create url
	    url = 'https://www.oxfordlearnersdictionaries.com/definition/english/' + text
	    # get page
	    page = requests.get(url)
	    # let's soup the page
	    soup = BeautifulSoup(page.text, 'html.parser')
	    pprint(soup)
	    try:
	        # get MP3 and definition
	        try:
	            # get MP3
	            mp3link = soup.find('div', {'class': 'sound audio_play_button pron-uk icon-audio'}).get('data-src-mp3')
	            pprint(mp3link)
	        except:
	            pprint('Pronunciation not found!')
	        try:
	            # get definition
	            definition = soup.find('span', {'class': 'def'}).text
	            pprint(definition)
	        except:
	            pprint('Meaning not found!')
	    except:
	        pprint('Something went wrong...')

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
