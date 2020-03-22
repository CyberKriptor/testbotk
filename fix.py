import logging

from aioviber.bot import Bot
from aioviber.chat import Chat
from viberbot.api.viber_requests import ViberSubscribedRequest

logger = logging.getLogger(__name__)

bot = Bot(
    name='ViberBot',
    avatar='http://avatar.example.com/avatar.jpg',
    auth_token="BOT_TOKEN",  # Public account auth token
    #uld be available from wide area network
    
      # Webhook url
)

@bot.command('ping')
async def ping(chat: Chat, matched):
    await chat.send_text('pong')

@bot.event_handler('subscribed')
async def user_subscribed(chat: Chat, request: ViberSubscribedRequest):
    await chat.send_text('Welcome')

@bot.message_handler('sticker')
async def sticker(chat: Chat):
    await chat.send_sticker(5900)

if __name__ == '__main__':  # pragma: no branch
    bot.run()  # pragma: no cover
