# Download
import youtube_dl
from discord_slash.utils.manage_commands import create_option

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

def init(slash):
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