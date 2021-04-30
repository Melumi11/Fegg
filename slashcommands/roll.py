# Roll
import random
from Fegg import slash, create_option

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