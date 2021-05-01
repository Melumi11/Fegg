# -------------------------------import----------------------------------#
import discord
import logging
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

# -----------------------------------------------------------------------#

# -------------------------------variables-------------------------------#
TOKEN = ''
# -----------------------------------------------------------------------#

# Logging errors
logging.basicConfig(level=logging.ERROR)

class MyClient(discord.Client):
    # -------------------------------"Global" Variables:-------------------------------#
    MELUMI = 640714673045504020  # my discord id

    # ----------------------------------------------------------------------------------#
    # Launch text in terminal
    async def on_ready(self):  # login text, init fighters, self.turn = self.p1
        activity = discord.Activity(type=discord.ActivityType.competing,
                                    name="the Arena")  # Playing, Listening to, Watching, also streaming, competing
        await client.change_presence(activity=activity)
        print(f'We have logged in as {self.user}')

    # Reading messages
    async def on_message(self, message):
        if message.author == client.user:  # so that the bot doesn't message itself
            return
        
        message_lower = message.content.lower()

        if message_lower.startswith('!'):
            if message_lower == '!sweat':
                await message.channel.send(
                    "https://cdn.discordapp.com/attachments/822493563619246131/822498710873178133/unknown.png")
            elif message_lower == '!help':  # help command
                embedVar = discord.Embed(title="Hi, my name is Fegg!",
                                         description="I am a bot coded by Melumi#5395. You can find my source code at https://github.com/Melumi11/Fegg/\nAll commands can be viewed by typing `/`",
                                         color=0x00ff00)
                embedVar.add_field(name=("List of commands:"),
                                   value="`!help` (this command)\n`/sweat` (For the Colin Cult big-sweaters) ||Also `!sweat`||\n`/roll` (rolls a single die with up to a billion faces)\n`/download` (given a link to a website with audio, Fegg attempts to find a direct link using youtube-dl)",
                                   inline=False)
                await message.channel.send(embed=embedVar)
        elif 'parm' in message_lower:  # parm
                await message.channel.send("https://images.heb.com/is/image/HEBGrocery/000081264")
        elif 'please kill me' in message_lower:
                await message.channel.send("HELP")
                await message.author.send("https://images.heb.com/is/image/HEBGrocery/000081264")

# -----------------------------Slash Commands----------------------------#
client = MyClient()
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.
import slashcommands
# -----------------------------------------------------------------------#

# -------------------------------Launch bot------------------------------#
# bot token
with open('token.txt') as f:
    TOKEN = f.readline()
client.run(TOKEN)

# Reference

# wait:
# await asyncio.sleep(10)
# reply:
# await message.channel.reply('Hello!', mention_author=False)

# Very cool debug command that stops the script and shows all variables, can resume after
# import code
# code.interact(local=locals())