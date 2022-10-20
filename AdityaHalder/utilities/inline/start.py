# Powered By @AdityaHalder

from typing import Union
from pyrogram.types import InlineKeyboardButton

from AdityaHalder import bot
from AdityaHalder.utilities.config import SUPPORT_CHANNEL, SUPPORT_GROUP


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 ✨",
                url=f"https://t.me/{bot.username}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="📡 𝐔𝐩𝐝𝐚𝐭𝐞𝐬",
                url=f"{SUPPORT_CHANNEL}",
            ),
            InlineKeyboardButton(
                text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💬",
                url=f"{SUPPORT_GROUP}",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙ 𝐁𝐨𝐭 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 ⚙", callback_data="settings_helper"
            )
        ]
    ]
    return buttons

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ❰ 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕",
                url=f"https://t.me/{bot.username}?startgroup=true"),
        ],
        [
            InlineKeyboardButton(
                text="📡 𝐔𝐩𝐝𝐚𝐭𝐞𝐬",
                url=f"{SUPPORT_CHANNEL}"),
            InlineKeyboardButton(
                text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💬",
                url=f"{SUPPORT_GROUP}")
        ],
        [
            InlineKeyboardButton(
                text="⚙ ❰ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 ❱ ⚙",
                callback_data="settings_back_helper"
            )
        ]
    ]
    return buttons

def private_panelx(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ❰ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕",
                url=f"https://t.me/{bot.username}?startgroup=true"),
        ],
        [
            InlineKeyboardButton(
                text="⚙ ❰ 𝐎𝐩𝐞𝐧 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐌𝐞𝐧𝐮 ❱ ⚙",
                callback_data="settings_back_helper"
            )
        ]
    ]
    return buttons
