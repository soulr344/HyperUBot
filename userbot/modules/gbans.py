# Copyright 2020 nunopenim @github
#
# Licensed under the DBADPL-B (Don't Be A Dick Public License B), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the DBADPL-B (So use it freely, but if you make a
# shitload of cash, buy me a beer or a pizza. Thanks.

from userbot import tgclient, log
from telethon.events import NewMessage
from userbot.include.aux_funcs import fetch_user
from userbot.config import GbanConfigs as cfg
from os.path import basename
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from asyncio.exceptions import TimeoutError as Timeout
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler

from asyncio import sleep
from logging import getLogger

log = getLogger(__name__)
ehandler = EventHandler(log)
LOGGING = getConfig("LOGGING")

VERSION = "1.0.2"

GBAN = cfg.GBAN
GBAN_BOT_IDS = cfg.GBAN_BOT_IDS

@ehandler.on(command="gban", hasArgs=True, outgoing=True)
async def gbanner(request):
    if not GBAN:
        await request.edit("`You haven't enable the gban router in config.py!`")
        return
    message = request.pattern_match.group(1)
    args = message.split()
    response = ''
    user = await fetch_user(request, full_user=True, get_chat=False)
    if str(type(user)) != '<class \'telethon.tl.types.UserFull\'>':
        await request.edit("`I am gonna gban myself because my owner is an idiot (give me a proper username ffs!)`")
        return
    user = str(user.user.id)
    if len(args) >= 2 and not request.reply_to_msg_id:
        reason = str(message.split(' ', 1)[1])
    elif len(args) == 1 and not request.reply_to_msg_id:
        reason = ""
    elif len(args) == 0 and not request.reply_to_msg_id:
        await request.edit("`Lemme gban you for not giving a proper username!`")
        return
    else:
        reason = message
    gbantext = '/gban ' + user + ' ' + reason
    for i in GBAN_BOT_IDS:
        async with tgclient.conversation(i) as conv:
            await conv.send_message(gbantext)
            x = None
            try:
                x = await conv.get_response()
            except Timeout:
                log.warning("@" + i + " took too much to respond, likely it is offline!\n")
            if x:
                response += i + ': ' + x.text.replace("**", "").replace("`", "").replace("tg://user?id=", "") + '\n\n'
            else:
                response += i + " took too much time to respond, likely it is offline!\n"
    await request.edit("`" + response + "`")
    return

@ehandler.on(command="ungban", hasArgs=True, outgoing=True)
async def ungbanner(request):
    if not GBAN:
        await request.edit("`You haven't enable the gban router in config.py!`")
        return
    message = request.pattern_match.group(1)
    args = message.split()
    response = ''
    user = await fetch_user(request, full_user=True, get_chat=False)
    if str(type(user)) != '<class \'telethon.tl.types.UserFull\'>':
        await request.edit("`I am gonna gban myself because my owner is an idiot (give me a proper username ffs!)`")
        return
    user = str(user.user.id)
    if len(args) >= 2 and not request.reply_to_msg_id:
        reason = str(message.split(' ', 1)[1])
    elif len(args) == 1 and not request.reply_to_msg_id:
        reason = ""
    elif len(args) == 0 and not request.reply_to_msg_id:
        await request.edit("`Lemme gban you for not giving a proper username!`")
        return
    else:
        reason = message
    gbantext = '/ungban ' + user + ' ' + reason
    for i in GBAN_BOT_IDS:
        async with tgclient.conversation(i) as conv:
            await conv.send_message(gbantext)
            x = None
            try:
                x = await conv.get_response()
            except Timeout:
                log.warning("@" + i + " took too much to respond, likely it is offline!\n")
            if x:
                response += i + ': ' + x.text.replace("**", "").replace("`", "").replace("tg://user?id=", "") + '\n\n'
            else:
                response += i + " took too much time to respond, likely it is offline!\n"
    await request.edit("`" + response + "`")
    return

@ehandler.on(command="gkick", hasArgs=True, outgoing=True)
async def ungkicker(request):
    if not GBAN:
        await request.edit("`You haven't enable the gban router in config.py!`")
        return
    message = request.pattern_match.group(1)
    args = message.split()
    response = ''
    user = await fetch_user(request, full_user=True, get_chat=False)
    if str(type(user)) != '<class \'telethon.tl.types.UserFull\'>':
        await request.edit("`I am gonna gkick myself because my owner is an idiot (give me a proper username ffs!)`")
        return
    user = str(user.user.id)
    if len(args) >= 2 and not request.reply_to_msg_id:
        reason = str(message.split(' ', 1)[1])
    elif len(args) == 1 and not request.reply_to_msg_id:
        reason = ""
    elif len(args) == 0 and not request.reply_to_msg_id:
        await request.edit("`Lemme gkick you for not giving a proper username!`")
        return
    else:
        reason = message
    gbantext = '/gkick ' + user + ' ' + reason
    for i in GBAN_BOT_IDS:
        async with tgclient.conversation(i) as conv:
            await conv.send_message(gbantext)
            x = None
            try:
                x = await conv.get_response()
            except Timeout:
                log.warning("@" + i + " took too much to respond, likely it is offline!\n")
            if x:
                response += i + ': ' + x.text.replace("**", "").replace("`", "").replace("tg://user?id=", "") + '\n\n'
            else:
                response += i + " took too much time to respond, likely it is offline!\n"
    await request.edit("`" + response + "`")
    return

DESC = "~nunos-private-repo modules are not for human consumption! This is the global bans module, which will redirect the gban command to group management bots (based on Marie), gbanning people on multiple bots at the same time.~"
USAGE = {"gban": "`.gban` <optional: user identifier> \
        \nUsage: Globally bans a user in the specified Marie based bots.",
        "ungban": "\n\n`.ungban` <optional: user identifier> \
        \nUsage: Globally unbans a user in the specified Marie based bots.",
        "gkick": "\n\n`.gkick` <optional: user identifier> \
        \nUsage: Globally kicks a user in the specified Marie based bots."}

for cmd in ("gban", "gkick", "ungban"):
    register_cmd_usage(cmd,
                       "",
                       USAGE[cmd])

# register_module_desc(DESC)
