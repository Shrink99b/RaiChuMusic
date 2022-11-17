## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQC6aaMA0kHg--djxKOHdT1tSRXKIAjRwooDSc3pGHpXQfSK3UpbbriRGPdyNxTk-8Ml_3C2KnGJU5KOFLkgSAqelkafRq23E_vdhwj2oslvSjDudWVWMMZwUIsnLZifwDnT8IdvwF7hfRXeResPqVV62mDZ8sXa77A4xFvRw2pCyZ-3VCAOHfxOBX6VSg6PUrm7ItS_l8DTAoW3rcURjXnUUOXf5WSRst0VbEkVPuHaMzGJ4s4XV7eANco3Amnhqrp9YvnctZm7Dw54gQTzuqMkJ6KW_sdPeVdb-y1Emd5i5zqC0iQadQD_PLACcTQLMiBrNg-J7CG5F6W03LstqgxhAAAAAU8LgScA")
BOT_TOKEN = getenv("BOT_TOKEN","5525655523:AAHButJPUaGQW1uAcdZOgFOjw6zdQleDMFw")
BOT_NAME = getenv("BOT_NAME","VARSHIT MUSIC")
API_ID = int(getenv("API_ID", "24132032"))
API_HASH = getenv("API_HASH", "528c5163fcbe0a4b3300c92f73ea8cb3")
OWNER_NAME = getenv("OWNER_NAME", "HM_APKE_HAI_KAUN")
ALIVE_NAME = getenv("ALIVE_NAME", "VARSHIT MUSIC")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "vs_asisstant")
BOT_USERNAME = getenv("BOT_USERNAME","vs_vc_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "vs_asisstant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT","https://t.me/loggervi")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL","https://t.me/loggervi")
SUDO_USERS = list(map(int, getenv("SUDO_USERS","5717137175").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
