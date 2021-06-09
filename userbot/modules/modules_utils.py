# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import SAFEMODE
from userbot.include.aux_funcs import sizeStrMaker
from userbot.include.language_processor import (ModulesUtilsText as msgRep,
                                                ModuleUsages as usageRep)
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (getAllModules, getLoadModules,
                                           getUserModules, getModuleDesc,
                                           getModuleInfo, getRegisteredCMDs,
                                           register_cmd_usage)
from userbot.sysutils.sys_funcs import isMacOS, isWindows
from logging import getLogger
from os.path import basename, exists, getctime, getsize, join
from os import stat
from time import ctime

log = getLogger(__name__)
ehandler = EventHandler(log)
MODULES_LISTED = {}


@ehandler.on(command="listcmds", alt="help", hasArgs=True, outgoing=True)
async def list_commands(event):
    arg_from_event = event.pattern_match.group(1)
    cmd_not_found = False
    command = None
    cmds_dict = getRegisteredCMDs()
    if arg_from_event:
        command, command_value = (None,)*2
        for key, value in cmds_dict.items():
            alt_cmd = value.get("alt_cmd")
            if key == arg_from_event.lower():
                command, command_value = key, value
                break
            elif alt_cmd and alt_cmd == arg_from_event.lower():
                command, command_value = key, value
                break

        if command_value:
            cmd_alt = command_value.get("alt_cmd")
            cmd_hasArgs = command_value.get("hasArgs")
            cmd_prefix = command_value.get("prefix")
            cmd_no_space_arg = command_value.get("no_space_arg")
            cmd_no_command = command_value.get("no_cmd")
            cmd_args = command_value.get("args")
            cmd_usage = command_value.get("usage")
            space = "" if cmd_no_space_arg else " "
            if cmd_no_command:
                cmd_args = ""
            elif not cmd_hasArgs:
                cmd_args = f"__{msgRep.ARGS_NOT_REQ}__"
            elif cmd_hasArgs and not cmd_args:
                cmd_args = f"__{msgRep.ARGS_NOT_AVAILABLE}__"
            if not cmd_usage:
                cmd_usage = f"__{msgRep.MODULE_NO_USAGE.lower()}__"

            if cmd_alt:
                cmd_info = f"`{cmd_prefix}{command}`/`"\
                           f"{cmd_prefix}{cmd_alt}`{space}{cmd_args}\n"
            else:
                cmd_info = f"`{cmd_prefix}{command}`{space}{cmd_args}\n"

            cmd_info += f"{msgRep.USAGE}: {cmd_usage}\n\n"
            await event.edit(cmd_info)
            return
        else:
            cmd_not_found = True

    cmds_amount = len(cmds_dict)
    all_cmds = f"**{msgRep.LISTCMDS_TITLE} ({cmds_amount})**\n\n"
    if cmd_not_found:
        all_cmds += msgRep.CMD_NOT_FOUND.format(arg_from_event) + "\n"
    all_cmds += msgRep.LISTCMDS_USAGE.format("`.listcmds`/`.help`") + "\n\n"
    for cmd, value in cmds_dict.items():
        alt_cmd = value.get("alt_cmd")
        if alt_cmd:
            all_cmds += f"`{cmd}` (`{alt_cmd}`)\t\t\t\t"
        else:
            all_cmds += f"`{cmd}`\n"
    await event.edit(all_cmds)


register_cmd_usage("listcmds",
                   usageRep.MODULES_UTILS_USAGE.get(
                       "listcmds", {}).get("args"),
                   usageRep.MODULES_UTILS_USAGE.get(
                       "listcmds", {}).get("usage"))
