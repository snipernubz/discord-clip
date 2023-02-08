import json
import interactions
from interactions import autodefer
import asyncio

import tracemalloc

tracemalloc.start()


with open('config.json', 'r') as configfile:
    config = json.load(configfile)
    token = config["token"]
    guild = config["guild"]

bot = interactions.Client(
    token=str(token),
    default_scope=int(guild),
    )
    
@bot.command()
@autodefer()
async def test_edit(ctx):
    await ctx.send(content="poggers")
    print(ctx)
    print(f"channel id = \n {ctx.channel_id}")
    channel = await interactions.get(bot, interactions.Channel, object_id=ctx.channel_id)
    print(f"channel obj = \n {channel}")
    msgId = ctx.message.id
    print(f"{msgId}")
    asyncio.sleep(5)
    await msgId.edit(content="edited pog")
    
    #pog
    
bot.start()
    