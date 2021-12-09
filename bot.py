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
  await event.reply("**Ali'nin Botu**, Selam Ben Sana Beni Tanıtıcam!★\nBeni tanımak için **/mmagneto**'i tıklayın."),
                                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Sahibim", url=f"https://t.me/mmagneto")]]),
                             disable_web_page_preview=True

@client.on(events.NewMessage(pattern="^/mmagneto$"))
  await event.reply("**Ali Kimdir**, Ali Sadece Kendini Geliştirmeye Çalışan Biri Azimli Bir Şekilde İlerliyor\nDaha fazla bilgi için Aşağıdaki Butonlardan Ali'nin kanal ve grupların akatılabilir botlarını kullanabilirsin eğer gruba girersen onunla birebir sohbet edebilirsin."),
                                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Marvel Sohbet", url=f"https://t.me/sohbetgnl"),
                                                                 InlineKeyboardButton("Film Kanalı", url=f"https://t.me/quickwaste"),
                                                                 InlineKeyboardButton("Film Botu", url=f"https://t.me/quickwastebot"),
                                                                 InlineKeyboardButton("Tagger Bot", url=f"https://t.me/alitaggerbot"),
                                                                 InlineKeyboardButton("Kişisel Blog", url=f"https://t.me/mmagneto3")]]),
                             disable_web_page_preview=True
