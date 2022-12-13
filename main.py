import json
import interactions
import moviepy
from pytube import YouTube


with open('config.json', 'r') as configfile:
    config = json.load(configfile)
    token = config["token"]
    guild = config["guild"]

bot = interactions.Client(
    token=str(token),
    default_scope=int(guild),
    )

@bot.event
async def on_start():
    print("Bot started")

# testing commands


@bot.command()
async def pog(ctx: interactions.CommandContext):
    """basic ping command"""
    await  ctx.send(f"Ping! {bot.latency}ms")

@bot.command()
@interactions.option()
async def relay(ctx: interactions.CommandContext, text: str):
    """relay what u say"""
    await ctx.send(f"You said '{text}'!")
    
    
 
button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="hello bot!",
    custom_id="hello"
)
button2 = interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="bye bot!",
    custom_id="bye",
)

row = interactions.ActionRow.new(button, button2)



@bot.command()
async def button_test(ctx):
  """a test for buttons"""
  await ctx.send("testing", components=row)
  
@bot.component("hello")
async def button_response(ctx):
    await ctx.send("Hello user :)", ephemeral=True)
    
@bot.component("bye")
async def button2_response(ctx):
    await ctx.send("aww bye bye user :(", ephemeral=True)

# real commmands  



@bot.command(
    name="make",
    description="makes a clip from a youtube video",
    options=[
    interactions.Option(
        name="typ",
        description="what do you want to do",
        type=interactions.OptionType.STRING,
        autocomplete=True,
        required=True
    ),
    interactions.Option(
        name="link",
        description="Link to youtube video",
        type=interactions.OptionType.STRING,
        required=True,
    )
])


  
@bot.autocomplete(command="make", name="typ")
async def auto_make(ctx, typ: str = ""):
        await ctx.populate([
            interactions.Choice(name= "webm :(",value ="webm"),
            interactions.Choice(name= "gif :(",value ="gif"),
        ])

async def make(ctx: interactions.CommandContext, typ: str, link: str):
    
    await ctx.send(f"you chose {link} to be made into {typ}")




bot.start()

