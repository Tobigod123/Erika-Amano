import os, sys, logging
from pyrogram import Client 

if os.path.exists('error.log'):
    os.remove('error.log')
        
#<-----------LOGGING------------>
logging.basicConfig(level=logging.INFO, filename='error.log')
LOG = logging.getLogger("Bot by @soheru")
LOG.setLevel(level=logging.INFO)
#<-----------Variables-------------->
LOG.info('❤️ Checking Bot Variables.....')
TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
BOT_TOKEN = os.environ.get('BOT_TOKEN', '6979551576:AAE35Fp2ui6XXyJ629EEN_ZXlpgaZsZgqzY') #BOT Token Add
API_ID = int(os.environ.get('API_ID', 3847632)) #Telgram Api id
APP_HASH = os.environ.get('APP_HASH', '1a9708f807ddd06b10337f2091c67657')# Telgram App hash  
OWNER_ID = int(os.environ.get('OWNER_ID', 6748415360))
MONGO_DB = os.environ.get("MONGO_DB", 'mongodb+srv://k7c7i:P4ATAn0S6f4smn4u@cluster0.bu2dbgw.mongodb.net/?retryWrites=true&w=majority') #MONGO DB FOR ANIME DATA
FILES_CHANNEL = os.environ.get("FILES_CHANNEL",-1001940830839)
BOT_NAME = os.environ.get('BOT_NAME', 'fucking encoding bot')
#<---------------Connecting-------------->
if BOT_TOKEN is not None:
    try:
        encoder  = Client('AutoEncoder', api_id=API_ID, api_hash=APP_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
        LOG.info('❤️ Bot Connected Created By Github @soheru || Telegram @sohailkhan_indianime ')
    except Exception as e:
        LOG.warn(f'😞 Error While Connecting To Bot\nCheck Errors: {e}')
        sys.exit()       
