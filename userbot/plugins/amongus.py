

import asyncio

from . import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "svillethon"


@bot.on(admin_cmd(pattern="امبوستر(|n) (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="امبوستر(|n) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    hmm = bot.uid
    USERNAME = f"tg://user?id={hmm}"
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()
    text1 = await edit_or_reply(event, "**⌔∮ يوجد خطأ هنا**")
    await asyncio.sleep(2)
    await text1.delete()
    stcr1 = await event.client.send_file(
        event.chat_id, "CAADAQADRwADnjOcH98isYD5RJTwAg"
    )
    text2 = await event.reply(
        f"**⌔∮ [{DEFAULTUSER}]({USERNAME}) :** لا بد لي من الاتصال بالمناقشة. "
    )
    await asyncio.sleep(3)
    await stcr1.delete()
    await text2.delete()
    stcr2 = await event.client.send_file(
        event.chat_id, "CAADAQADRgADnjOcH9odHIXtfgmvAg"
    )
    text3 = await event.reply(
        f"**⌔∮ [{DEFAULTUSER}]({USERNAME}) :** يجب علينا كشف القاتل او سنخسر ! "
    )
    await asyncio.sleep(3)
    await stcr2.delete()
    await text3.delete()
    stcr3 = await event.client.send_file(
        event.chat_id, "CAADAQADOwADnjOcH77v3Ap51R7gAg"
    )
    text4 = await event.reply(f"**⌔∮ الاخرين :**اين هم ؟؟")
    await asyncio.sleep(2)
    await text4.edit(f"**⌔∮ الاخرين :** من هو ؟؟ ")
    await asyncio.sleep(2)
    await text4.edit(
        f"**⌔∮ [{DEFAULTUSER}]({USERNAME}) :** انه {name} , لقد رأيته {name}  يستخدم vent,"
    )
    await asyncio.sleep(3)
    await text4.edit(f"**⌔∮ الاخرين :**تمام صوتو على {name} ")
    await asyncio.sleep(2)
    await stcr3.delete()
    await text4.delete()
    stcr4 = await event.client.send_file(
        event.chat_id, "CAADAQADLwADnjOcH-wxu-ehy6NRAg"
    )
    catevent = await event.reply(f"⌔∮ {name} يتم اخراجه..")
    await asyncio.sleep(2)
    await catevent.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    await asyncio.sleep(0.5)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    await asyncio.sleep(0.2)
    await stcr4.delete()
    if cmd == "":
        await catevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ**⪼ {name} هو القاتل.**      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         0 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
        await asyncio.sleep(4)
        await catevent.delete()
        await event.client.send_file(event.chat_id, "CAADAQADLQADnjOcH39IqwyR6Q_0Ag")
    elif cmd == "n":
        await catevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ**⪼ {name} لم يكن القاتل.**      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         1 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
        await asyncio.sleep(4)
        await catevent.delete()
        await event.client.send_file(event.chat_id, "CAADAQADQAADnjOcH-WOkB8DEctJAg")


@icssbot.on(admin_cmd(pattern="timp(|n) (.*)", outgoing=True))
@icssbot.on(sudo_cmd(pattern="timp(|n) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()
    catevent = await edit_or_reply(event, f"{name} is ejected.......")
    await asyncio.sleep(2)
    await catevent.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    await asyncio.sleep(0.8)
    await catevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    await asyncio.sleep(0.2)
    if cmd == "":
        await catevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ {name} was an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         0 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
    elif cmd == "n":
        await catevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ {name} was not an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         1 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )


CMD_HELP.update(
    {
        "imposter": "**Plugin :** `imposter__`\
\n\n**Syntax : **`.امبوستر` / `.امبوستر` <text>\
\n**Usage : ** Find imposter with stickers.\
\n\n**Syntax : **`.timp` / `.timpn` <text>\
\n**Usage : ** Find imposter only text."
    }
)
