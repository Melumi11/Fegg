import youtube_dl
import random
# from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option


def roll(slash):
    description = "Dice roll command, up to 999,999,999"
    options = [create_option(
                    name="d",
                    description="Roll a d-sided die",
                    option_type=4,
                    required=True)]
    
    @slash.slash(name="roll", description=description, options=options)
    async def roll(ctx, d):
        if 0 < d <= 999999999:  # dice roll command (up to 999,999,999)
            await ctx.send(content=f"Roll d{d}: `[{str(random.randint(1, d))}]`")
        else:
            await ctx.send(content="Please enter a number between one and one billion")

def download(slash):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': []}

    description = "Find an audio file, given a link. Use this if you want to quickly download something."
    options=[create_option(
                    name="Source",
                    description="Link to the media you want to find.",
                    option_type=3,
                    required=True)]

    @slash.slash(name="download",
                description=description,
                options=options)
    async def download(ctx, source):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                r = ydl.extract_info(source, download=False)
                await ctx.send(r['url'])
            except Exception as exception:
                length = 19 + len(source) + 21
                await ctx.send(f"**{type(exception).__name__}**: `{str(exception)[18:length]}`")


commands = {roll, download}

def init_slashcommands(slash):
    for i in commands:
        i(slash)
    print("slash commands initialized!")