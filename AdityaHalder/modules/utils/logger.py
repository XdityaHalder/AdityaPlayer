from AdityaHalder import bot
from AdityaHalder.modules.database import is_on_off
from AdityaHalder.utilities.config import LOG, LOG_GROUP_ID


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Chat"
        if message.from_user.username:
            user_name = f"@{message.from_user.username}"
        else:
            user_name = f"{message.from_user.mention}"
        logger_text = f"""
**━━━━━━━━━━━━━━━━━━━**
**🤖 𝐀𝐝𝐢𝐭𝐲𝐚 𝐏𝐥𝐚𝐲𝐞𝐫 : 𝐒𝐦𝐚𝐫𝐭 𝐋𝐨𝐠𝐬.**
**━━━━━━━━━━━━━━━━━━━**
**👾 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐔𝐬𝐞𝐫 𝐃𝐞𝐭𝐚𝐢𝐥𝐬 :**
**🥀 𝐍𝐚𝐦𝐞 ›** {message.from_user.first_name}
**🌸 𝐋𝐢𝐧𝐤 : ›** {user_name}
**🌷 𝐈𝐃✩ : ›** `{message.from_user.id}`
**━━━━━━━━━━━━━━━━━━━**
**💬 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐂𝐡𝐚𝐭 𝐃𝐞𝐭𝐚𝐢𝐥𝐬 :**
**☘️ 𝐍𝐚𝐦𝐞 ›** {message.chat.title}
**🌿 𝐋𝐢𝐧𝐤 : ›** {chatusername}
**🌱 𝐈𝐃✩ : ›** `{message.chat.id}`
**━━━━━━━━━━━━━━━━━━━**
**🔥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : [𝐀𝐝𝐢𝐭𝐲𝐚 𝐒𝐞𝐫𝐯𝐞𝐫](https://t.me/adityaserver).**
**━━━━━━━━━━━━━━━━━━━**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await bot.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
