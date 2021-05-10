# -------------------------------import----------------------------------#
import logging
from discord_slash.utils.manage_commands import create_option
from client import *
import slashcommands
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
with open('token.txt') as f:
    TOKEN = f.readline() # bot token in git ignored file
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