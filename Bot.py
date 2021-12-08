import os, logging, asyncio
import io, os, sys, setuptools, tokenize
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**Ali'nin Botu**, Selam Ben Sana Beni Tanıtıcam!★\nBeni tanımak için **/ali**'i tıklayın.",
                    buttons=(
                      [Button.url('🚀 Sahibim', 'https://t.me/mmagneto')]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/ali$"))
async def start(event):
  await event.reply("**Ali Kimdir**, Ali Sadece Kendini Geliştirmeye Çalışan Bir Coder Azimli Bir Şekilde İlerliyor\nDaha fazla bilgi için Aşağıdaki Butonlardan Ali'nin kanal ve grupların akatılabilir botlarını kullanabilirsin eğer gruba girersen onunla birebir sohbet edebilirsin.",
                    buttons=(
                      [Button.url('🌟 Marvel Sohbet Grubu', 'https://t.me/sohbetgnl'),
                      Button.url('Film Kanalı', 'https://t.me/quickwaste'),
                      Button.url('Tag Botu', 'https://t.me/alitaggerbot')
                      Button.url('Film Botu', 'https://t.me/quickwastebot' )
                      Button.url('Kişisel Blog', 'https://t.me/mmagneto3')]
                    ),
                    link_preview=False
                   )
