# Aditya Halder

import os
import sys
from os import listdir, mkdir

from AdityaHalder.console import LOGGER


def dirr():
    if "AdityaHalder" not in listdir():
        LOGGER(__name__).warning(
            f"🥀 𝐓𝐡𝐢𝐬 𝐑𝐞𝐩𝐨 𝐢𝐬 𝐍𝐨𝐭 𝐎𝐫𝐢𝐠𝐢𝐧𝐚𝐥❗\n𝐏𝐥𝐞𝐚𝐬𝐞 𝐔𝐬𝐞 𝐎𝐫𝐢𝐠𝐢𝐧𝐚𝐥 𝐑𝐞𝐩𝐨 ✨..."
        )
        sys.exit()
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    if "downloads" not in listdir():
        mkdir("downloads")
    if "cache" not in listdir():
        mkdir("cache")
    LOGGER(__name__).info("🥀 𝐀𝐥𝐥 𝐃𝐢𝐫𝐞𝐜𝐭𝐨𝐫𝐢𝐞𝐬 𝐔𝐩𝐝𝐚𝐭𝐞𝐝 ✨...")
