# Aditya Halder
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

from AdityaHalder.utilities import config
from AdityaHalder.console import LOGGER

TEMP_MONGODB = "mongodb+srv://aditya:aditya@aditya.ah7ixut.mongodb.net/?retryWrites=true&w=majority"


if config.MONGO_DB_URL is None:
    LOGGER(__name__).warning(
        "🥀 𝐍𝐨 𝐌𝐨𝐧𝐠𝐨 𝐃𝐁 𝐔𝐫𝐥 𝐅𝐨𝐮𝐧𝐝 ✨...\n\n🌹 𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐖𝐢𝐥𝐥 𝐖𝐨𝐫𝐤 𝐎𝐧\n𝐀𝐝𝐢𝐭𝐲𝐚'𝐬 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 ✨ ..."
    )
    temp_client = Client(
        "Aditya",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URL)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URL)
    mongodb = _mongo_async_.Aditya
    pymongodb = _mongo_sync_.Aditya
