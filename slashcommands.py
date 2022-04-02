import yt_dlp
import random
from discord_slash.utils.manage_commands import create_option
from discord_slash import SlashCommand
from discord_slash.model import SlashCommandOptionType

def roll():
    description = "Dice roll command, up to 999,999,999"
    options = [create_option(
                    name="d",
                    description="Roll a d-sided die",
                    option_type=SlashCommandOptionType.INTEGER,
                    required=True)]
    
    @slash.slash(name="roll", description=description, options=options)
    async def roll(ctx, d):
        if 0 < d <= 999999999:  # dice roll command (up to 999,999,999)
            await ctx.send(content=f"Roll d{d}: `[{str(random.randint(1, d))}]`")
        else:
            await ctx.send(content="Please enter a number between one and one billion")

# yt-dlp stuff below:
error = "no error"
class MyLogger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        global error 
        end = -1 if "Set --default-search \"ytsearch\"" not in msg else msg.find("Set --default-search \"ytsearch\"")
        error = msg[7:end] # also gets rid of "ERROR: " in output
ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'no_color': True, # gets rid of console color things that show up on discord
        'progress_hooks': []}
def downloadvideo():
    description = "Download a video from youtube.com or other video platforms."
    options=[create_option(
                    name="source",
                    description="Link to the video you want to download.",
                    option_type=SlashCommandOptionType.STRING,
                    required=True)]

    @slash.slash(name="downloadvideo", description=description, options=options)
    async def download(ctx, source):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                r = ydl.extract_info(source, download=False)
                urls = [f['url'] for f in r['formats'] if f['acodec'] != 'none' and f['vcodec'] != 'none'] # gets urls with video and audio
                await ctx.send(urls[-1]) # this is too op
            except Exception as exception:
                await ctx.send(f"**{type(exception).__name__}**: {error}]")

def downloadaudio():
    description = "Download an audio file, given a media link. Works on YouTube and other sites."
    options=[create_option(
                    name="source",
                    description="Link to the media you want to hear.",
                    option_type=SlashCommandOptionType.STRING,
                    required=True)]

    @slash.slash(name="downloadaudio", description=description, options=options)
    async def download(ctx, source):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                r = ydl.extract_info(source, download=False)
                await ctx.send(r['url']) # gets first audio link
            except Exception as exception:
                await ctx.send(f"**{type(exception).__name__}**: {error}")

commands = {roll, downloadvideo, downloadaudio}

def init_slashcommands(client):
    global slash
    slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.
    for i in commands:
        i()
    print("slash commands initialized!")