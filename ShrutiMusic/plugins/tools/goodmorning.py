import asyncio
import random
from pyrogram import filters
from pyrogram.types import Message
from ShrutiMusic import app

active_chats = {}
GM_MESSAGES = [
    "🌞 Gᴏᴏᴅ Mᴏʀɴɪɴɢ 🌼 {mention}",
    "☕ Rise and Shine, {mention}!",
    "🌄 Sᴜʀᴀᴊ Nɪᴋʜʀᴀ, Tᴜᴍʜᴀʀᴀ Dɪɴ Sᴜʙʜ Hᴏ {mention}",
    "🌻 Nᴇᴇᴛʜ Kʜᴀᴛᴀᴍ, Aʙ Kᴀᴀᴍ Sʜᴜʀᴜ {mention}",
    "💫 Jᴀɢᴏ Mᴇʀᴇ Sʜᴇʀᴏ! {mention}",
    "🕊️ Sᴜᴋʜ Sᴀʙʜᴀ Gᴏᴏᴅ Mᴏʀɴɪɴɢ {mention}",
]

@app.on_message(filters.command("gmtag") & filters.group)
async def gmtag(_, message: Message):
    chat_id = message.chat.id
    if chat_id in active_chats:
        return await message.reply("⚠️ Gᴏᴏᴅ Mᴏʀɴɪɴɢ Tᴀɢɢɪɴɢ Aʟʀᴇᴀᴅʏ Rᴜɴɴɪɴɢ.")
    
    active_chats[chat_id] = True
    await message.reply("☀️ Gᴏᴏᴅ Mᴏʀɴɪɴɢ Tᴀɢɢɪɴɢ Sᴛᴀʀᴛᴇᴅ...")

    users = []
    async for member in app.get_chat_members(chat_id):
        if member.user.is_bot or member.user.is_deleted:
            continue
        users.append(member.user)

    for i in range(0, len(users), 5):
        if chat_id not in active_chats:
            break
        batch = users[i:i+5]
        mentions = " ".join([f"[{u.first_name}](tg://user?id={u.id})" for u in batch])
        msg = random.choice(GM_MESSAGES).format(mention=mentions)
        await app.send_message(chat_id, msg, disable_web_page_preview=True)
        await asyncio.sleep(2)

    active_chats.pop(chat_id, None)
    await app.send_message(chat_id, "✅ Gᴏᴏᴅ Mᴏʀɴɪɴɢ Tᴀɢɢɪɴɢ Dᴏɴᴇ!")

@app.on_message(filters.command("gmstop") & filters.group)
async def gmstop(_, message: Message):
    chat_id = message.chat.id
    if chat_id in active_chats:
        del active_chats[chat_id]
        await message.reply("🛑 Gᴏᴏᴅ Mᴏʀɴɪɴɢ Tᴀɢɢɪɴɢ Sᴛᴏᴘᴘᴇᴅ.")
    else:
        await message.reply("❌ Nᴏᴛʜɪɴɢ Rᴜɴɴɪɴɢ.")
