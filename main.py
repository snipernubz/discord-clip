import json
import interactions
import moviepy
from pytube import YouTube
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

@bot.event
async def on_start():
    print("Bot started")

# test commands


@bot.command()
async def pog(ctx: interactions.CommandContext):
    """basic ping command"""
    await  ctx.send(f"Ping! {bot.latency}ms")

@bot.command()
@interactions.option()
async def relay(ctx: interactions.CommandContext, text: str):
    """relay what u say"""
    await ctx.send(f"You said '{text}'!")
    
@bot.command()
async def base_sub_test(ctx: interactions.CommandContext):
    """This description isn't seen in UI (yet?)"""
    pass

@base_sub_test.subcommand()
@interactions.option()
async def sub_uno(ctx: interactions.CommandContext, option: int = None):
    """first sub"""
    await ctx.send(f"You selected the command_name sub command and put in {option}")

@base_sub_test.subcommand()
@interactions.option()
async def sub_dos(ctx: interactions.CommandContext, second_option: str):
    """second sub"""
    await ctx.send(f"You selected the second_command sub command and put in {second_option}")
 
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

@bot.command()
async def modal_test(ctx):
    """model test command"""
    modal = interactions.Modal(
        title="Test Model",
        custom_id="mod_form",
        components=[interactions.TextInput(
            style=interactions.TextStyleType.SHORT,
            label="Let's get straight to it: what's 1 + 1?",
            custom_id="text_input_response",
            min_length=2,
            max_length=3,
            )],
    )

    await ctx.popup(modal)
 
@bot.modal("mod_form")
async def modal_response(ctx, response: str):
    await ctx.send(f"You wrote: {response}", ephemeral=True)

# real commmands  

# make command
@bot.command()
async def make(ctx: interactions.CommandContext):
    """make command"""
    pass


#make gif command
@make.subcommand()
@interactions.option()
async def gif(ctx: interactions.CommandContext, gif_link: str):
    """Make a gif from a video"""
    
    print(f"Link: {gif_link}")
    
    video_url = str(gif_link)
    video = YouTube(video_url)
    
    # check video avalability
    video.check_availability()
    
  
    print(f"Video title: '{video.title}' video has length of '{video.length}' seconds") 

    
    
    # make gif modal
    gif_modal = interactions.Modal(
        title="Make a gif",
        custom_id="gif_start",
        components=[interactions.TextInput(
            style=interactions.TextStyleType.SHORT,
            label="start time (format HH:MM:SS)",
            custom_id="gif_start_time",
            min_length=1,
        )],
    )
    
    # send modal
    await ctx.popup(gif_modal)

@gif.error
async def gif_error(ctx: interactions.CommandContext, error: Exception):
    print(f"ERROR: {error}")
    await ctx.send(f"ERROR: {error}")
    
    


@make.subcommand()
@interactions.option()
async def webm(ctx: interactions.CommandContext, webm_link: str):
    """make a webm from video"""
    await ctx.send(f"You selected the make webm sub command and chose video {webm_link}")

    webm_modal = interactions.Modal(
        title="Make a webm",
        custom_id="webm_model",
        components=[interactions.TextInput(...)],
    )



bot.start()

