import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply(
"""ʜᴏɪ,
ɪ'ᴍ ʜᴇʀᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ TAGALL ʏᴏᴜʀ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ɪ ᴍ ᴠᴇʀʏ ᴘᴏᴡᴇʀꜰᴜʟʟ ʙᴏᴛ! 
*SALAM ,*
┏━━━━━━━━━━━━━━━━
┣ ₪ *MENİ QRUPUNA ELAVE ET* `
┣ ₪ TAĞ BOTU
┗━━━━━━━━━━━━━━━━━
 
  ʜɪᴛ /help **kömek üçün**
 [❤](https://telegra.ph/file/2fa3a833f3ccc1d98dba1.jpg),
""",
    link_preview=False,
    buttons=(
       [
        Button.url(' kanal', 'https://t.me/imperialsupportt'),
        Button.url('creater', 'https://t.me/Ferid_mov')
    ],
    )
  )
