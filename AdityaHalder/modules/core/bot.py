# Aditya Halder

import sys
from pyrogram import Client
from AdityaHalder.utilities import config
from AdityaHalder.console import LOGGER


class Bot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"🥀 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 💞...")
        super().__init__(
            "AdityaPlayer",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID,
                f"**━━━━━━━━━━━━━━━━━━━**\n**✅ 𝐁𝐨𝐭 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🥳**\n**━━━━━━━━━━━━━━━━━━━**\n**🥀 𝐍𝐚𝐦𝐞 ›** {self.name}\n**🌸 𝐋𝐢𝐧𝐤 : ›** @{self.username}\n**🌷 𝐈𝐃✩ : ›** `{self.id}`\n━━━━━━━━━━━━━━━━━━━\n**🔥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : [𝐀𝐝𝐢𝐭𝐲𝐚 𝐒𝐞𝐫𝐯𝐞𝐫](https://t.me/adityaserver).**\n**━━━━━━━━━━━━━━━━━━━**",
              disable_web_page_preview=True
            )
        except:
            LOGGER(__name__).error(
                "🥀 𝐏𝐥𝐞𝐚𝐬𝐞, 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐀𝐝𝐝 𝐁𝐨𝐭 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐌𝐚𝐤𝐞 𝐀𝐧 𝐀𝐝𝐦𝐢𝐧 🌷..."
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "🥀 𝐏𝐥𝐞𝐚𝐬𝐞 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐁𝐨𝐭 𝐚𝐬 𝐀𝐧 𝐀𝐝𝐦𝐢𝐧 𝐢𝐧 𝐘𝐨𝐮𝐫 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩 🌷..."
            )
            sys.exit()
        LOGGER(__name__).info(f"━━━━━━━━━━━━━━━━━━━\n✅ 𝐁𝐨𝐭 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🥳\n━━━━━━━━━━━━━━━━━━━\n🥀 𝐍𝐚𝐦𝐞 » {self.name}\n🌸 𝐋𝐢𝐧𝐤 :» {self.username}\n🌷 𝐈𝐃✩ :» `{self.id}`\n━━━━━━━━━━━━━━━━━━━\n🔥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : 𝐀𝐝𝐢𝐭𝐲𝐚 𝐒𝐞𝐫𝐯𝐞𝐫.\n━━━━━━━━━━━━━━━━━━━")
