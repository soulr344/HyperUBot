# My stuff
from tg_userbot import tgclient

# Telethon stuff
from telethon.events import NewMessage

# Misc imports
from subprocess import check_output, CalledProcessError

@tgclient.on(NewMessage(pattern=r"^\.bash(?: |$)(.*)", outgoing=True))
async def bash(command):
    commandArray = command.text.split(" ")
    bashCmd = ""
    for word in commandArray: #building the command
        if not word == ".bash":
            bashCmd += word + " "
    try:
        cmd_output = check_output(bashCmd, shell=True).decode()
    except CalledProcessError:
        cmd_output = "There has been an unspecified error, likely bad arguments or that command does not exist"
    output = "$ " + bashCmd + "\n\n" + cmd_output
    await command.edit("`" + output + "`")
    return