# -------------------------------import----------------------------------#
import logging
from client import *
import slashcommands
from os import getenv
# -----------------------------------------------------------------------#


# Logging errors
logging.basicConfig(level=logging.ERROR)


# -------------------------------variables-------------------------------#
client = Client()

# -----------------------------------------------------------------------#


# -----------------------------slash commands----------------------------#
slashcommands.init_slashcommands(client)

# -----------------------------------------------------------------------#


# -------------------------------launch bot------------------------------#

try:
    with open('token.txt') as f:
        TOKEN = f.readline() # bot token in git ignored file
except: pass
try:
    TOKEN = getenv('TOKEN') # set environment variable in github
except: pass
client.run(TOKEN)
# -----------------------------------------------------------------------#

# Reference

# wait:
# await asyncio.sleep(10)
# reply:
# await message.channel.reply('Hello!', mention_author=False)

# Very cool debug command that stops the script and shows all variables, can resume after
# import code
# code.interact(local=locals())