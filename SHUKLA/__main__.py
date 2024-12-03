import os
import logging
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import RPCError
from typing import Union
import asyncio

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
    """Handle the /start command."""
    await message.reply_photo(
        photo="https://files.catbox.moe/jbc3mk.jpg",
        caption=(
            "**╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ──────⏤͟͟͞͞★**\n"
            "**┆● ʜᴇʏ ɪ ᴀᴍ ʙᴀɴ-ᴀʟʟ ʙᴏᴛ**\n"
            "**┆● ᴡɪᴛʜ ᴘᴏᴡᴇʀғᴜʟ ғᴇᴀᴛᴜʀᴇs**\n"
            "**╰─────────────────────────**\n"
            "**──────────────────────────**\n"
            "**❖ ᴜꜱᴇ » /banall ᴛᴏ sᴇᴇ ᴍᴀɢɪᴄ ɪɴ ɢʀᴏᴜᴘ**\n"
            "**──────────────────────────**"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="▪️Session Gen Bot▪️", url="https://t.me/StringSesssionGeneratorRobot"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="▪️Support▪️", url="https://t.me/MASTIWITHFRIENDSXD"
                    ),
                    InlineKeyboardButton(
                        text="▪️Update▪️", url="https://t.me/StrangerAssociation"
                    ),
                ],
            ]
        ),
    )
    # Log the interaction
    await client.send_message(
        chat_id=LOGGER_ID,
        text=(
            f"{message.from_user.mention} started the bot.\n\n"
            f"<b>User ID:</b> <code>{message.from_user.id}</code>\n"
            f"<b>Username:</b> @{message.from_user.username or 'N/A'}"
        ),
    )


@app.on_message(filters.new_chat_members)
async def join_watcher(client: Client, message: Message):
    """Log when the bot is added to a group."""
    try:
        chat = message.chat
        bot_user = await client.get_me()
        link = await client.export_chat_invite_link(chat.id)

        for member in message.new_chat_members:
            if member.id == bot_user.id:
                count = await client.get_chat_members_count(chat.id)
                await client.send_message(
                    LOGGER_ID,
                    f"Bot added to {chat.title} ({chat.id}) by {message.from_user.mention}. Members: {count}.\nLink: {link}",
                )
    except RPCError as e:
        logging.error(f"Error in join_watcher: {e}")


@app.on_message(filters.command("banall") & filters.group)
async def banall_command(client, message: Message):
    """Ban all members in a group."""
    try:
        async for member in client.get_chat_members(message.chat.id):
            try:
                await client.ban_chat_member(message.chat.id, member.user.id)
                logging.info(f"Banned {member.user.id} from {message.chat.id}")
            except Exception as e:
                logging.warning(f"Failed to ban {member.user.id}: {e}")
        logging.info("Banall process completed")
    except RPCError as e:
        logging.error(f"Error in banall_command: {e}")


if __name__ == "__main__":
    logging.info("Banall-Bot Booted Successfully")
    app.run()
