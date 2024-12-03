import os
import logging
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# config vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER = os.getenv("OWNER")

# pyrogram client
app = Client(
            "banall",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
)

@app.on_message(
filters.command("start")
& filters.private            
)
async def start_command(client, message: Message):
  await message.reply_photo(
        photo="https://files.catbox.moe/jbc3mk.jpg",
        caption=(
            "**╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ──────⏤͟͟͞͞★**\n"
            "**┆● ʜᴇʏ ɪ ᴀᴍ ʙᴀɴ-ᴀʟʟ ʙᴏᴛ**\n"
            "**┆● ᴡɪᴛʜ ᴘᴏᴡᴇʀғᴜʟ ғᴇᴀᴛᴜʀᴇs**\n"
            "**╰─────────────────────────**\n"
            "**──────────────────────────**\n"
            "**❖ ɪ ᴀᴍ ᴀ ᴠᴇʀʀʏ ᴘᴏᴡᴇʀ ғᴜʟʟ ʙᴀɴᴀʟʟ ʙᴏᴛ**\n"
            "**ᴀɴʏ ɢʀᴘ ᴄᴀɴ ʙʟᴏᴡ ᴜᴘ ɪɴ ᴊᴜsᴛ ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs**\n"
            "**ᴀᴅᴅ ᴍᴇ ᴀɴʏ ɢʀᴏᴜᴘ ᴀɴᴅ ɢɪᴠᴇ ʙᴀɴ ᴘᴏᴡᴇʀ**\n"
            "**──────────────────────────**\n"
            "**❖ ᴜꜱᴇ » /banall ᴛᴏ sᴇᴇ ᴍᴀɢɪᴄ ɪɴ ɢʀᴏᴜᴘ**\n"
            "**──────────────────────────**"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
              [
                  InlineKeyboardButton(text="▪️sᴇssɪᴏɴ ɢᴇɴ ʙᴏᴛ▪️", url="https://t.me/StringSesssionGeneratorRobot"),
              ],
              [
                  InlineKeyboardButton(text="▪️ғʀᴇᴇ ɪᴅ ᴜsᴇʀ-ʙᴏᴛ▪️", url="https://t.me/Shukla_op_clone1bot"),
              ],
              [
                  InlineKeyboardButton("▪️sᴜᴘᴘᴏʀᴛ▪️", url="https://t.me/MASTIWITHFRIENDSXD"),
                  InlineKeyboardButton("▪️ᴜᴘᴅᴀᴛᴇ▪️", url="https://t.me/StrangerAssociation"),
              ],
              [
                  InlineKeyboardButton("▪️sʜɪᴠàɴsʜ-xᴅ▪️", url="https://t.me/ITSZ_SHIVANSH"),
              ],
            ]
        ),
    )

@app.on_message(
filters.command("banall") 
& filters.group
)
async def banall_command(client, message: Message):
    print("getting memebers from {}".format(message.chat.id))
    async for i in app.get_chat_members(message.chat.id):
        try:
            await app.ban_chat_member(chat_id = message.chat.id, user_id = i.user.id)
            print("kicked {} from {}".format(i.user.id, message.chat.id))
        except Exception as e:
            print("failed to kicked {} from {}".format(i.user.id, e))           
    print("process completed")


# start bot client
app.start()
print("Banall-Bot Booted Successfully")
idle()