# svillethon - Userbot
# 𝑺𝑶𝑼𝑹𝑪𝑬 svillethon - 𝑺𝑺𝑻𝑹𝑰𝑵𝑮_𝑺𝑬𝑺𝑺𝑰𝑶𝑵
# Owner ~ @svillethon

from telethon.sessions import StringSession as ss
from telethon.sync import TelegramClient as tc

print("𓆩 SOURCE svillethon -  STRING SESSION 𓆪")
print("")

APP_ID = int(input("⌔∮ ENTER APP ID HERE - "))
API_HASH = input("⌔∮ ENTER API HASH HERE - ")

with tc(ss(), APP_ID, API_HASH) as client:
    ics = client.send_message("me", client.session.save())
    ics.reply("⌔∮ هذا هو كود التيرمكس الخاص بك.\n⌔∮ المطور - @svillethon. ")
    print("")
    print("")
    print(
        "⌔∮ Below is the STRING_SESSION. You can also find it in your Telegram Saved Messages."
    )
    print("")
    print("")
    print(client.session.save())
