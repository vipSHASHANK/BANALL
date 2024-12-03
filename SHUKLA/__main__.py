import os
import logging
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# Logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Config vars
API_ID = int(os.getenv("API_ID", "12345"))  # Replace with a fallback value
API_HASH = os.getenv("API_HASH", "your_api_hash")  # Replace with your fallback value
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")  # Replace with your fallback value
LOGGER_ID = int(os.getenv("LOGGER_ID", "0"))  # Fallback to 0 if not provided

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
                    InlineKeyboardButton(
                        text="▪️sᴇssɪᴏɴ ɢᴇɴ ʙᴏᴛ▪️", url="https://t.me/StringSesssionGeneratorRobot"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="▪️ғʀᴇᴇ ɪᴅ ᴜsᴇʀ-ʙᴏᴛ▪️", url="https://t.me/Shukla_op_clone1bot"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "▪️sᴜᴘᴘᴏʀᴛ▪️", url="https://t.me/MASTIWITHFRIENDSXD"
                    ),
                    InlineKeyboardButton(
                        "▪️ᴜᴘᴅᴀᴛᴇ▪️", url="https://t.me/StrangerAssociation"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "▪️sʜɪᴠàɴsʜ-xᴅ▪️", url="https://t.me/ITSZ_SHIVANSH"
                    ),
                ],
            ]
        ),
    )
    await client.send_message(
        chat_id=LOGGER_ID,
        text=(
            f"{message.from_user.mention} just started the bot.\n\n"
            f"<b>User ID:</b> <code>{message.from_user.id}</code>\n"
            f"<b>Username:</b> @{message.from_user.username or 'N/A'}"
        ),
    )


@app.on_message(filters.command("banall") & filters.group)
async def banall_command(client, message: Message):
    print(f"Getting members from {message.chat.id}")
    async for member in client.get_chat_members(message.chat.id):
        try:
            await client.ban_chat_member(chat_id=message.chat.id, user_id=member.user.id)
            print(f"Kicked {member.user.id} from {message.chat.id}")
        except Exception as e:
            print(f"Failed to kick {member.user.id}: {e}")
    print("Process completed")


# Start the bot
if __name__ == "__main__":
    print("Banall-Bot Booted Successfully")
    app.run()
