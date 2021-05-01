# Sweat
def init(slash):
    @slash.slash(name="sweat", description=":colinsweat:")
    async def sweat(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/822493563619246131/822498710873178133/unknown.png")