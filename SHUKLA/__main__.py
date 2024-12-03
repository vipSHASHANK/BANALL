import os
import random
import logging
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired
from pyrogram.errors import RPCError
from typing import Union
import asyncio

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
LOGGER_ID = int(os.getenv("LOGGER_ID"))

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
await client.send_message(
                LOGGER_ID,
                f"{mention} Has Just Started The Bot"
            )
    
# Handler for new chat members
@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(client: Client, message: Message):    
    try:
        chat = message.chat
        link = await client.export_chat_invite_link(chat.id)
        for member in message.new_chat_members:
            if member.id == (await client.get_me()).id:
                count = await client.get_chat_members_count(chat.id)
                msg = (
                    f"📝 ʙᴀɴᴀʟʟ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                    f"____________________________________\n\n"
                    f"📌 ᴄʜᴀᴛ ɴᴀᴍᴇ: {chat.title}\n"
                    f"🍂 ᴄʜᴀᴛ ɪᴅ: {chat.id}\n"
                    f"🔐 ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{chat.username or 'N/A'}\n"
                    f"🛰 ᴄʜᴀᴛ ʟɪɴᴋ: [ᴄʟɪᴄᴋ]({link})\n"
                    f"📈 ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count}\n"
                    f"🤔 ᴀᴅᴅᴇᴅ ʙʏ: {message.from_user.mention}"
                )
                await client.send_photo(
                    LOGGER_ID, 
                    photo=random.choice(photo), 
                    caption=msg, 
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("sᴇᴇ ɢʀᴏᴜᴘ👀", url=link)]
                    ])
                )
    except RPCError as e:
        print(f"Error in join_watcher: {e}")

# Handler for when the bot leaves a chat
@app.on_message(filters.left_chat_member)
async def on_left_chat_member(client: Client, message: Message):
    try:
        if (await client.get_me()).id == message.left_chat_member.id:
            remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
            title = message.chat.title
            username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
            chat_id = message.chat.id
            bot_username = (await client.get_me()).username
            left_msg = (
                f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n"
                f"𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ: {title}\n\n"
                f"𝐂ʜᴀᴛ 𝐈ᴅ: {chat_id}\n\n"
                f"𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ: {remove_by}\n\n"
                f"𝐁ᴏᴛ: @{bot_username}"
            )
            await client.send_photo(
                LOGGER_ID, 
                photo=random.choice(photo), 
                caption=left_msg
            )
    except RPCError as e:
        print(f"Error in on_left_chat_member: {e}")

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