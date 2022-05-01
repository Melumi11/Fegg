import discord

class Client(discord.Client):
    # -------------------------------"Global" Variables:-------------------------------#
    MELUMI = 640714673045504020  # my discord id
    SUICIDAL = ["kill me", "i'm just tired", "i'm having a bad time", "can this be over now", "no one cares about me", "i can't do this anymore", "i'm suicidal", "if anything happens to me", "no one cares about me", "kill myself", "wanna die", "i want to die", "shoot myself", "jump off a bridge", "committing suicide"]
    # ----------------------------------------------------------------------------------#
    # Launch text in terminal
    async def on_ready(self):  # login text, init fighters, self.turn = self.p1
        activity = discord.Activity(type=discord.ActivityType.playing,
                                    name="To the Moon")  # Playing, Listening to, Watching, also streaming, competing
        await self.change_presence(activity=activity)
        print('bot online')

    # Reading messages
    async def on_message(self, message):
        if message.author == self.user:  # so that the bot doesn't message itself
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
                                   value="`!help` (this command)\n`/roll` (rolls a single die with up to a billion faces)\n`/download` (given a link to a website with audio, Fegg attempts to find a direct link using youtube-dl)\n`!sweat` (:colinsweat:)",
                                   inline=False)
                await message.channel.send(embed=embedVar)
        elif 'parm' in message_lower:  # parm
                await message.channel.send("https://images.heb.com/is/image/HEBGrocery/000081264")
        for i in self.SUICIDAL:
            if i in message_lower:
                    await message.channel.send("Please do not worry. @​everyone is here to help. If you are suicidal, you can find help at: https://suicidepreventionlifeline.org/")
                    await message.author.send("Please do not worry. @everyone is here to help. If you are suicidal, you can find help at: https://suicidepreventionlifeline.org/")

# Reference

# wait:
# await asyncio.sleep(10)
# reply:
# await message.channel.reply('Hello!', mention_author=False)

# Very cool debug command that stops the script and shows all variables, can resume after
# import code
# code.interact(local=locals())