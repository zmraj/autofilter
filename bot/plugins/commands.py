#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & Wafikh

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
import random
import html
import re
import time
from functools import partial
from contextlib import suppress

PHOTOS = [
    "https://telegra.ph/file/2f4475621bd45ef834196.jpg",
    "https://telegra.ph/file/2f4475621bd45ef834196.jpg",
    "https://telegra.ph/file/15829f51bad4db9608af0.jpg",
    "https://telegra.ph/file/15829f51bad4db9608af0.jpg",
    "https://telegra.ph/file/608313fb9f529b6bc8ec1.jpg",
    "https://telegra.ph/file/608313fb9f529b6bc8ec1.jpg",
    "https://telegra.ph/file/52809564a7d6d5c73c8a2.jpg",
    "https://telegra.ph/file/52809564a7d6d5c73c8a2.jpg",
    "https://telegra.ph/file/c686d9040de18c17cc1e0.jpg",
    "https://telegra.ph/file/c686d9040de18c17cc1e0.jpg",
    "https://telegra.ph/file/9da2d9bc599aa36b9d89a.jpg",
    "https://telegra.ph/file/9da2d9bc599aa36b9d89a.jpg",
]

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = "@sumeshandrameshhd2021"
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("🤭 Sorry Dude, You are B A N N E D 🤣🤣🤣")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="<b>🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭\n\nനിങ്ങൾക് സിനിമകൾ വെന്നോ? അതിനായി അത്യം ങ്ങളുടെ മെയിൻ ചാനലിൽ ജോയിൻ ചെയ്യണം... 😁\n\nJoin ചെയതത്തിനു ശേഷം വീണ്ടും ബോട്ട് /start ആക്കൂ.😁</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" 🔰JOIN OUR CHANNEL🔰 ", url=f"https://t.me/sumeshandrameshhd2021")]
              ])
            )
            return
        except Exception:
            await update.reply_text("Something Wrong. Contact my Support Group")
            return
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = "<b>┈••✿ @MGMOVIEGRAM ✿••┈\n\n➠𝐂ʜᴀɴɴᴇʟ :https://t.me/joinchat/nppwyzxMr8NhN2M9\n\n➠Gʀᴏᴜᴘ : https://t.me/MGMOVIEGRAM</b>",
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🎖𝙎𝙃𝘼𝙍𝙀 🎖', url='https://t.me/share/url?url=https://t.me/MGMOVIEGRAM')
                ],
                [
                    InlineKeyboardButton('𝙂𝙍𝙊𝙐𝙋 💬', url='https://t.me/MGMOVIEGRAM'),
                    InlineKeyboardButton('📣 𝘾𝙃𝘼𝙉𝙉𝙀𝙇', url='https://t.me/MG_MEDIA')
                ]
            ]
        )
    )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🎖𝙎𝙃𝘼𝙍𝙀 🎖', url='https://t.me/share/url?url=https://t.me/MGMOVIEGRAM')
                ],
                [
                    InlineKeyboardButton('𝙂𝙍𝙊𝙐𝙋 💬', url='https://t.me/MGMOVIEGRAM'),
                    InlineKeyboardButton('📣 𝘾𝙃𝘼𝙉𝙉𝙀𝙇', url='https://t.me/MG_MEDIA')
                ]
            ]
        )
    )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '⚠️ 𝗝𝗢𝗜𝗡 𝗢𝗨𝗥 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ⚠️', url="https://t.me/joinchat/5UxSr0XIphVhYjc9"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('⚠️ 𝙂𝙍𝙊𝙐𝙋', url='https://t.me/MGMOVIEGRAM'),
        InlineKeyboardButton('🕵‍♂ 𝘾𝙍𝙀𝘼𝙏𝙊𝙍', url ='https://t.me/xxxtentacion_OF_TG')
        ],[
        InlineKeyboardButton('♻️ 𝙅𝙊𝙄𝙉 𝙊𝙐𝙍 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ♻️', url ='https://t.me/MG_MEDIA')
        ],[
        InlineKeyboardButton('💡 𝙃𝙀𝙇𝙋', callback_data="help"),
        InlineKeyboardButton('🔐 𝘾𝙇𝙊𝙎𝙀', callback_data="close")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo=random.choice(PHOTOS),
        caption=Translation.START_TEXT.format(
                update.from_user.mention),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('𝙃𝙤𝙢𝙚 🏘', callback_data='start'),
        InlineKeyboardButton('𝘼𝙗𝙤𝙪𝙩 🕵‍♂', callback_data='about')
    ],[
        InlineKeyboardButton('𝘾𝙡𝙤𝙨𝙚 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo=random.choice(randomphotos.photos),
        caption=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('𝙃𝙤𝙢𝙚 🏘', callback_data='start'),
        InlineKeyboardButton('𝘾𝙡𝙤𝙨𝙚 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
