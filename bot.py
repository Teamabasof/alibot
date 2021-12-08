import os, logging, asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient, events


bot_token = os.environ['BOT_TOKEN']
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']

app = Client(
    "Alibot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash
)
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**Ali'nin Botu**, Selam Ben Sana Beni Tanıtıcam!★\nBeni tanımak için **/ali**'i tıklayın.",
                    reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="Bot Sahibi", url=f"https://t.me/mmagneto")]
                ])
@client.on(events.NewMessage(pattern="^/ali$"))
async def start(event):
  await event.reply("**Ali Kimdir**, Ali Sadece Kendini Geliştirmeye Çalışan Biri Azimli Bir Şekilde İlerliyor\nDaha fazla bilgi için Aşağıdaki Butonlardan Ali'nin kanal ve grupların akatılabilir botlarını kullanabilirsin eğer gruba girersen onunla birebir sohbet edebilirsin.",
                    reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="Marvel Sohbet", url=f"https://t.me/sohbetgnl"), 
                    InlineKeyboardButton(text="Film Kanalı", url=f"https://t.me/quickwaste"), 
                    InlineKeyboardButton(text="Tagger Bot", url=f"https://t.me/alitaggerbot"), 
                    InlineKeyboardButton(text="Film Botu", url=f"https://t.me/quickwastebot"), 
                    InlineKeyboardButton(text="Kişisel Blog", url=f"https://t.me/mmagneto3"), 
                    ]
                ])
