import math
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ANIYAXMUSIC import app
import config
from ANIYAXMUSIC.utils.formatters import time_to_seconds

# HACK: Pyrogram bypass ke liye raw JSON dictionaries (Updated for Premium Emojis)
def api_btn(text, callback_data=None, url=None, style=None, custom_emoji_id=None):
    btn = {"text": text}
    if callback_data:
        btn["callback_data"] = callback_data
    if url:
        url_str = str(url)
        if not url_str.startswith("http") and not url_str.startswith("tg://"):
            url_str = f"https://t.me/{url_str.replace('@', '')}"
        btn["url"] = url_str
        
    if style in ["primary", "danger", "success"]:
        btn["style"] = style  # 'primary' = Blue, 'danger' = Red, 'success' = Green
        
    if custom_emoji_id:
        btn["icon_custom_emoji_id"] = str(custom_emoji_id) 
    return btn

def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            api_btn(text=_["P_B_1"], callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}", style="primary"),
            api_btn(text=_["P_B_2"], callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}", style="primary"),
        ],
        [
            # Cleaned text
            api_btn(text=str(_["CLOSE_BUTTON"]).strip(), callback_data=f"forceclose {videoid}|{user_id}", style="danger", custom_emoji_id="5219805369806629055")
        ],
    ]
    return buttons

def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    
    # Safe Division & Percentage Logic
    if duration_sec == 0:
        percentage = 0
    else:
        percentage = (played_sec / duration_sec) * 100
        
    # ==========================================
    # VIP SPOTIFY SLIDER WITH EMOJI KNOB
    # ==========================================
    length = 11
    pos = math.floor((percentage / 100) * length)
    bar = ""
    for i in range(length):
        if i < pos:
            bar += "━"
        elif i == pos:
            bar += "✨"  # Premium Emoji as the slider dot!
        else:
            bar += "─"
            
    buttons = [
        [
            # Full Premium Timer Bar! (Kyunki ab call.py isko support karta hai)
            api_btn(text=f"{played}  {bar}  {dur}", callback_data="GetTimer", style="primary", custom_emoji_id="5258113901106580375")
        ],
        [
            # 4 Premium Emoji Buttons (Play, Pause, Skip, Stop)
            api_btn(text=" ", callback_data=f"ADMIN Resume|{chat_id}", style="primary", custom_emoji_id="5219899949281453881"), 
            api_btn(text=" ", callback_data=f"ADMIN Pause|{chat_id}", style="danger", custom_emoji_id="5334811859415477124"), 
            api_btn(text=" ", callback_data=f"ADMIN Skip|{chat_id}", style="success", custom_emoji_id="5222148368955877900"), 
            api_btn(text=" ", callback_data=f"ADMIN Stop|{chat_id}", style="danger", custom_emoji_id="5219805369806629055"), 
        ],
        [
            # Tunes & Home
            api_btn(text="𝚻𝛖𝛏𝛆𝛔 🎶", url="https://t.me/UrVenatrix_music_bot", style="primary", custom_emoji_id="5222472119295684375"),
            api_btn(text="𝚮𝛐𝛍𝛆", url="https://t.me/ABOUTxYUTAA", style="primary", custom_emoji_id="5294017134756636818"),
        ],
        [
            # Privacy Policy
            api_btn(text="ᴘʀɪᴠᴀᴄʏ  ", url="https://telegra.ph/Privacy-Policy-03-15-2", style="success", custom_emoji_id="5393302369024882368")
        ],
        [
            # Close Red
            api_btn(text=str(_["CLOSE_BUTTON"]).strip(), callback_data="close", style="danger", custom_emoji_id="5219805369806629055")
        ],
    ]
    return buttons

def stream_markup(_, chat_id):
    buttons = [
        [
            api_btn(text=" ", callback_data=f"ADMIN Resume|{chat_id}", style="primary", custom_emoji_id="5219899949281453881"), 
            api_btn(text=" ", callback_data=f"ADMIN Pause|{chat_id}", style="danger", custom_emoji_id="5334811859415477124"), 
            api_btn(text=" ", callback_data=f"ADMIN Skip|{chat_id}", style="success", custom_emoji_id="5222148368955877900"), 
            api_btn(text=" ", callback_data=f"ADMIN Stop|{chat_id}", style="danger", custom_emoji_id="5219805369806629055"), 
        ],
        [
            api_btn(text="𝚻𝛖𝛏𝛆𝛔 🎶", url="https://t.me/UrVenatrix_music_bot", style="primary", custom_emoji_id="5222472119295684375"),
            api_btn(text="𝚮𝛐𝛍𝛆", url="https://t.me/ABOUTxYUTAA", style="primary", custom_emoji_id="5294017134756636818"),
        ],
        [
            api_btn(text="ᴘʀɪᴠᴀᴄʏ. ", url="https://telegra.ph/Privacy-Policy-03-15-2", style="success", custom_emoji_id="5393302369024882368")
        ],
        [
            api_btn(text=str(_["CLOSE_BUTTON"]).strip(), callback_data="close", style="danger", custom_emoji_id="5219805369806629055")
        ],
    ]
    return buttons

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            api_btn(text=_["P_B_1"], callback_data=f"ANIYAPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}", style="primary"),
            api_btn(text=_["P_B_2"], callback_data=f"ANIYAPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}", style="primary"),
        ],
        [
            api_btn(text=str(_["CLOSE_BUTTON"]).strip(), callback_data=f"forceclose {videoid}|{user_id}", style="danger", custom_emoji_id="5219805369806629055"),
        ],
    ]
    return buttons

def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            api_btn(text=_["P_B_3"], callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}", style="primary"),
        ],
        [
            api_btn(text=str(_["CLOSE_BUTTON"]).strip(), callback_data=f"forceclose {videoid}|{user_id}", style="danger", custom_emoji_id="5219805369806629055"),
        ],
    ]
    return buttons

def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            api_btn(text=_["P_B_1"], callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}", style="primary"),
            api_btn(text=_["P_B_2"], callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}", style="primary"),
        ],
        [
            api_btn(text="◁", callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}", style="primary"),
            api_btn(text=str(_["CLOSE_BUTTON"]).strip(), callback_data=f"forceclose {query}|{user_id}", style="danger", custom_emoji_id="5219805369806629055"),
            api_btn(text="▷", callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}", style="primary"),
        ],
    ]
    return buttons

# ==========================================
# SAFE VIP MUSIC END MARKUP
# ==========================================
def music_end_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text="➕ ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{app.username}?startgroup=true"),
            InlineKeyboardButton(text="🏠 ʜᴏᴍᴇ", url=f"https://t.me/{app.username}?start=help"),
        ],
        [
            InlineKeyboardButton(text="🔐 ᴘʀɪᴠᴀᴄʏ", url=getattr(config, "SUPPORT_CHAT", f"https://t.me/{app.username}")),
            InlineKeyboardButton(text=str(_["CLOSE_BUTTON"]).strip(), callback_data="close"),
        ],
    ]
    return InlineKeyboardMarkup(buttons)

