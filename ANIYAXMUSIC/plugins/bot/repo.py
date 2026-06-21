from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ANIYAXMUSIC import app
from config import BOT_USERNAME
from ANIYAXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
❥ ωєℓ¢σмє тσ  ˹ 𝐒ʜ𝛊⃡ɀυ𝛋⃨𝛂 𝚳𝛖𝛅𝛊҆𝛓 ♪ 

❥ ʀᴇᴘᴏ ᴄʜᴀᴀʜɪʏe ᴛᴏ ʙᴏᴛ ᴋᴏ 

❥ 3 ɢᴄ ᴍᴀɪ ᴀᴅᴅ ᴋᴀʀ ᴋᴇ 

❥ ᴀᴅᴍɪɴ ʙᴀɴᴏ ᴀᴜʀ sᴄʀᴇᴇɴsʜᴏᴛ 
     
❥ ᴏᴡɴᴇʀ @zctol ᴋᴏ ᴅᴏ ғɪʀ ʀᴇᴘᴏ ᴍɪʟ sᴀᴋᴛɪ ʜᴀɪ 

"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("♡ α∂∂ иσω ♡", url=f"https://t.me/ShizukaxMusic_Robot?startgroup=true")
        ],
        [
          InlineKeyboardButton("ѕυρρσɾƚ", url="https://t.me/Ig_Aanyaa"),
          InlineKeyboardButton(" ⋆ ˚｡⋆ Iᴢᴜᴍɪ ⋆｡˚ ⋆ </𝟑𒌋", url="https://t.me/ig_izumi"),
          ],
               [
                InlineKeyboardButton("ᴏᴛʜᴇʀ ʙᴏᴛs", url=f"https://t.me/heartstealer_x"),
],
[
InlineKeyboardButton("ᴄʜᴇᴄᴋ", url=f"https://t.me/ShizukaxMusic_Robot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/7jleru.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
