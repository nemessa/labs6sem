from telegram import Bot
from prt.config import TG_TOKEN, TG_API_URL

def print_b(message):
    bot = Bot(
        token=TG_TOKEN,
        base_url=TG_API_URL
    )
    bot.send_message(
        chat_id=781127991,
        text=message
    )
