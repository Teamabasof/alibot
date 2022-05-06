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
  await event.reply("**TEAMABASOF'Bot**, Salam mən Sənə Sahibim haqqında melumat vercem!★\nMəni tanımaq ucun **/teamabasof**'i yazın.",
                                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Sahibim", url=f"https://t.me/TTteamabasof")]]),
                             disable_web_page_preview=True

@client.on(events.NewMessage(pattern="^/teamabasof$"))
async def help(event):
  await event.reply("**Teamabasof Kimdir**, Teamabasof Adı Rəhimdi TELEGRAMDA Botlariyaratmaqi sevir onun arzuzusu Futbolcu olmaq\nDaha Çox məlumat ücun Aşağıdaki Butonlardan TEAMABASOF'un kanal və qrupların baxa bilərsən botlarını islede bilərsən əyər qruba girərsən onla birebir sohbet edəbilərsən.",
                                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Team Sohbet", url=f"https://t.me/teamabasofsohbet"),
                                                                 InlineKeyboardButton("Rəssmi Kanalım", url=f"https://t.me/texnoteamm"),
                                                                 InlineKeyboardButton("Musiqi Botu", url=f"https://t.me/wolfmusiqiBot"),
                                                                 
                                InlineKeyboardButton("Tagger Bot", url=f"https://t.me/texnotagger_bot"),
                                                                 InlineKeyboardButton("TEAM BOTS 🇦🇿", url=f"https://t.me/alitaggerbot"),
                                                                 InlineKeyboardButton("Şəxsi Blog", url=f"https://t.me/teamabasofblog")]]),
                             disable_web_page_preview=True
