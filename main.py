# -------------------------------import----------------------------------#
import logging
from client import *
import slashcommands
from os import getenv, environ
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
        environ["TOKEN"] = f.readline() # bot token in git ignored file
except: pass
try:
    TOKEN = getenv('TOKEN') # set environment variable in github
except: pass
client.run(TOKEN)
# -----------------------------------------------------------------------#