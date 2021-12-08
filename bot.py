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
  await event.reply("**Ali'nin Botu**, Selam Ben Sana Beni Tanıtıcam!★\nBeni tanımak için **/ali**'i tıklayın.",
                    reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Sahip", url="https://t.me/mmagneto"
                        )
                    ]
                ]
@client.on(events.NewMessage(pattern="^/start$"))
  await event.reply("**Ali Kimdir**, Ali Sadece Kendini Geliştirmeye Çalışan Biri Azimli Bir Şekilde İlerliyor\nDaha fazla bilgi için Aşağıdaki Butonlardan Ali'nin kanal ve grupların akatılabilir botlarını kullanabilirsin eğer gruba girersen onunla birebir sohbet edebilirsin.",
                    reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Marvel Sohbet", url="https://t.me/sohbetgnl"
                        )
                    ]
                ]
