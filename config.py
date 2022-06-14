from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "1234567"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","Zara_Vcbot")
BOT_USERNAME = getenv("BOT_USERNAME", "Zara_Vcbot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "zara_THE_addiction")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+TFNht-Xwon1lM2Y1")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/bb7f23ae8d5024eb1c8b4.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/601b1330bbdd725b488f2.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5102663914 5166884358").split()))
