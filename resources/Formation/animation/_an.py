
#  ======================================================= #

from userbot.Config import Config

USERID = Config.OWNER_ID 
ALIVE_NAME = Config.ALIVE_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "svillethon Userbot"
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"

#  ======================================================= #
