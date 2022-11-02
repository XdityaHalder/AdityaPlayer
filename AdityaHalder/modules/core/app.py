# Aditya Halder

import sys
from pyrogram import Client
from AdityaHalder.utilities import config
from AdityaHalder.console import LOGGER

assistants = []
assistantids = []


class App(Client):
    def __init__(self):
        self.one = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"🥀 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐂𝐥𝐢𝐞𝐧𝐭𝐬 🌷...")
        if config.STRING1:
            await self.one.start()
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            try:
                await self.one.join_chat("kaalware")
                await self.one.join_chat("adityaserver")
                await self.one.join_chat("adityadiscus")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID,
                    f"**━━━━━━━━━━━━━━━━━━━**\n**✅ 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝟏 𝐇𝐚𝐬 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🥳**\n**━━━━━━━━━━━━━━━━━━━**\n**🥀 𝐍𝐚𝐦𝐞 ›** {self.one.name}\n**🌸 𝐋𝐢𝐧𝐤 : ›** @{self.one.username}\n**🌷 𝐈𝐃✩ : ›** `{self.one.id}`\n**━━━━━━━━━━━━━━━━━━━**\n**🔥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : [loveofmusic](https://t.me/loveofmusicsupport).**\n**━━━━━━━━━━━━━━━━━━━**",
                  disable_web_page_preview=True
                )
            except:
                LOGGER(__name__).error(
                    f"🥀𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝟏 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐀𝐜𝐜𝐞𝐬𝐬\n𝐋𝐨𝐠'𝐬 𝐆𝐫𝐨𝐮𝐩 ✨ ...\n\n🌷 𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐝𝐝 𝐚𝐧𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐀𝐬\n𝐀𝐧 𝐀𝐝𝐦𝐢𝐧 💞 ..."
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🥀 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝟏 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🌿 𝐀𝐬 {self.one.name} ✨..."
            )
        if config.STRING2:
            await self.two.start()
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            try:
                await self.two.join_chat("kaalware")
                await self.two.join_chat("adityaserver")
                await self.two.join_chat("adityadiscus")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID,
                    f"**━━━━━━━━━━━━━━━━━━━**\n**✅ 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝟐 𝐇𝐚𝐬 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🥳**\n**━━━━━━━━━━━━━━━━━━━**\n**🥀 𝐍𝐚𝐦𝐞 ›** {self.two.name}\n**🌸 𝐋𝐢𝐧𝐤 : ›** @{self.two.username}\n**🌷 𝐈𝐃✩ : ›** `{self.two.id}`\n**━━━━━━━━━━━━━━━━━━━**\n**🔥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : [loveofmusic](https://t.me/loveofmusicsupport).**\n**━━━━━━━━━━━━━━━━━━━**",
                  disable_web_page_preview=True
                )
            except:
                LOGGER(__name__).error(
                    f"🥀𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝟐 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐀𝐜𝐜𝐞𝐬𝐬\n𝐋𝐨𝐠'𝐬 𝐆𝐫𝐨𝐮𝐩 ✨ ...\n\n🌷 𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐝𝐝 𝐚𝐧𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐀𝐬\n𝐀𝐧 𝐀𝐝𝐦𝐢𝐧 💞 ..."
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🥀 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝟐 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🌿 𝐀𝐬 {self.two.name} ✨..."
            )
        if config.STRING3:
            await self.three.start()
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            try:
                await self.three.join_chat("kaalware")
                await self.three.join_chat("adityaserver")
                await self.three.join_chat("adityadiscus")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID,
                    f"**━━━━━━━━━━━━━━━━━━━**\n**✅ 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝟑 𝐇𝐚𝐬 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🥳**\n**━━━━━━━━━━━━━━━━━━━**\n**🥀 𝐍𝐚𝐦𝐞 ›** {self.three.name}\n**🌸 𝐋𝐢𝐧𝐤 : ›** @{self.three.username}\n**🌷 𝐈𝐃✩ : ›** `{self.three.id}`\n**━━━━━━━━━━━━━━━━━━━**\n**🔥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : [𝐀𝐝𝐢𝐭𝐲𝐚 𝐒𝐞𝐫𝐯𝐞𝐫](https://t.me/adityaserver).**\n**━━━━━━━━━━━━━━━━━━━**",
                  disable_web_page_preview=True
                )
            except:
                LOGGER(__name__).error(
                    f"🥀𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝟑 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐀𝐜𝐜𝐞𝐬𝐬\n𝐋𝐨𝐠'𝐬 𝐆𝐫𝐨𝐮𝐩 ✨ ...\n\n🌷 𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐝𝐝 𝐚𝐧𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐀𝐬\n𝐀𝐧 𝐀𝐝𝐦𝐢𝐧 💞 ..."
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🥀 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝟑 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🌿 𝐀𝐬 {self.three.name} ✨..."
            )
        if config.STRING4:
            await self.four.start()
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            try:
                await self.four.join_chat("kaalware")
                await self.four.join_chat("adityaserver")
                await self.four.join_chat("adityadiscus")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID,
                    f"**━━━━━━━━━━━━━━━━━━━**\n**✅ 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝟒 𝐇𝐚𝐬 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🥳**\n**━━━━━━━━━━━━━━━━━━━**\n**🥀 𝐍𝐚𝐦𝐞 ›** {self.four.name}\n**🌸 𝐋𝐢𝐧𝐤 : ›** @{self.four.username}\n**🌷 𝐈𝐃✩ : ›** `{self.four.id}`\n**━━━━━━━━━━━━━━━━━━━**\n**🔥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : [𝐀𝐝𝐢𝐭𝐲𝐚 𝐒𝐞𝐫𝐯𝐞𝐫](https://t.me/adityaserver).**\n**━━━━━━━━━━━━━━━━━━━**",
                  disable_web_page_preview=True
                )
            except:
                LOGGER(__name__).error(
                    f"🥀𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝟒 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐀𝐜𝐜𝐞𝐬𝐬\n𝐋𝐨𝐠'𝐬 𝐆𝐫𝐨𝐮𝐩 ✨ ...\n\n🌷 𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐝𝐝 𝐚𝐧𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐀𝐬\n𝐀𝐧 𝐀𝐝𝐦𝐢𝐧 💞 ..."
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🥀 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝟒 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🌿 𝐀𝐬 {self.four.name} ✨..."
            )
        if config.STRING5:
            await self.five.start()
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            try:
                await self.five.join_chat("kaalware")
                await self.five.join_chat("adityaserver")
                await self.five.join_chat("adityadiscus")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID,
                    f"**━━━━━━━━━━━━━━━━━━━**\n**✅ 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝟓 𝐇𝐚𝐬 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🥳**\n**━━━━━━━━━━━━━━━━━━━**\n**🥀 𝐍𝐚𝐦𝐞 ›** {self.one.name}\n**🌸 𝐋𝐢𝐧𝐤 : ›** @{self.one.username}\n**🌷 𝐈𝐃✩ : ›** `{self.one.id}`\n━━━━━━━━━━━━━━━━━━━\n**🔥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : [𝐀𝐝𝐢𝐭𝐲𝐚 𝐒𝐞𝐫𝐯𝐞𝐫](https://t.me/adityaserver).**\n**━━━━━━━━━━━━━━━━━━━**",
                  disable_web_page_preview=True
                )
            except:
                LOGGER(__name__).error(
                    f"🥀𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝟓 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐀𝐜𝐜𝐞𝐬𝐬\n𝐋𝐨𝐠'𝐬 𝐆𝐫𝐨𝐮𝐩 ✨ ...\n\n🌷 𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐝𝐝 𝐚𝐧𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐀𝐬\n𝐀𝐧 𝐀𝐝𝐦𝐢𝐧 💞 ..."
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🥀 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝟓 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🌿 𝐀𝐬 {self.five.name} ✨..."
            )
