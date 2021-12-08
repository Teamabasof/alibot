import requests
import json
import pyrogram
from pyrogram import Client
from pyrogram import filters
import os


#load_dotenv(".env", override=True)
bot_token = os.environ['BOT_TOKEN']
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']

# Telegram sunucusuna bagliyoruz
app = Client(
    "LambdaBot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash
)
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
