import os
import logging
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Config vars
API_ID = int(os.getenv("API_ID", "12345"))  # Replace default with your API ID
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
OWNER = os.getenv("OWNER", "default_owner_username")

# Pyrogram client
app = Client(
    "banall",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message: Message):
    await message.reply_photo(
        photo="https://files.catbox.moe/tndcfj.jpg",
        caption=(
            "ʜᴇʏ ɪᴍ ʙᴀɴ ᴀʟʟ ʙᴏᴛ ᴠᴇʀʏ ᴘᴏᴡᴇʀғᴜʟʟ\n\n"
            "ᴀɴʏ ɢʀᴘ ᴄᴀɴ ʙʟᴏᴡ ᴜᴘ ɪɴ ᴊᴜsᴛ ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs\n\n"
            "ᴀᴅᴅ ᴍᴇ ᴀɴʏ ɢʀᴘ ᴀɴᴅ ɢɪᴠᴇ ʙᴀɴ ᴘᴏᴡᴇʀ\n\n"
            "ᴛʏᴘᴇ /banall ᴛᴏ sᴇᴇ ᴍᴀɢɪᴄ ɪɴ ɢʀᴘ\n\n"
            "ᴘᴏᴡᴇʀᴇᴅ ʙʏ: [sᴛʀᴀɴɢᴇʀ](https://t.me/SHIVANSH474)"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("ᴏᴡɴᴇʀ", url=f"https://t.me/{OWNER}")],
                [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/mastiwithfriendsxd")],
                [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/strangerassociation")],
                [InlineKeyboardButton("sʜɪᴠᴀɴsʜ-xᴅ", url="https://t.me/shivansh474")],
            ]
        ),
    )

@app.on_message(filters.command("banall") & filters.group)
async def banall_command(client, message: Message):
    print(f"Getting members from chat {message.chat.id}")
    async for member in app.get_chat_members(message.chat.id):
        try:
            await app.ban_chat_member(chat_id=message.chat.id, user_id=member.user.id)
            print(f"Banned {member.user.id} from {message.chat.id}")
        except ChatAdminRequired:
            print(f"Cannot ban {member.user.id}: Missing admin rights")
        except Exception as e:
            print(f"Failed to ban {member.user.id}: {e}")
    print("Banall process completed.")

# Start bot client
app.start()
print("Banall-Bot Booted Successfully")
idle()
