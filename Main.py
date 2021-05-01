# -------------------------------import----------------------------------#
import logging
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from Client import *

# -----------------------------------------------------------------------#

# -------------------------------variables-------------------------------#
client = Client()
# -----------------------------------------------------------------------#

# Logging errors
logging.basicConfig(level=logging.ERROR)


# -----------------------------slash commands----------------------------#
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.
from slashcommands import *

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