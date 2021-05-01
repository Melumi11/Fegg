import youtube_dl
import random
# from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

def init_slashcommands(slash):
    print("slash commands initialized!")

    # Roll
    @slash.slash(name="roll", description="Dice roll command, up to 999,999,999",
                options=[create_option(
                    name="d",
                    description="Roll a d-sided die",
                    option_type=3,
                    required=True)])
    async def roll(ctx, d):
        if len(d) < 17:  # dice roll command (up to 999,999,999)
            try:
                await ctx.send(content=f"Roll d{d}: `[{str(random.randint(1, int(d)))}]`")
            except:
                await ctx.send(content="Please enter a number between zero and one billion")


    def my_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [my_hook]}

    @slash.slash(name="download",
                description="Find an audio file, given a link. Use this if you want to quickly download something.",
                options=[create_option(
                    name="Source",
                    description="Link to the media you want to find.",
                    option_type=3,
                    required=True)])
    async def download(ctx, Source):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                r = ydl.extract_info(Source, download=False)
                await ctx.send(r['url'])
            except Exception as exception:
                await ctx.send(f"**{type(exception).__name__}**: `{str(exception)[18:-89]}`")