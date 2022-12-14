import json
import interactions
import moviepy
from pytube import YouTube
from datetime import timedelta
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

def convert_sec(sec):
    """Get time from seconds"""
    td = timedelta(seconds = sec)
    return str(td)
  
def convert_hms(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


# make command
@bot.command()
async def make(ctx: interactions.CommandContext):
    """make command"""
    pass


#make gif command

gif_info = {}

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

    # add video info to gif_info 
    gif_info["video link"] = video_url
    gif_info["video title"] = video.title
    gif_info["video length"] = convert_sec(video.length)
    
    
    # make gif start modal
    gif_start_modal = interactions.Modal(
        title="Make a gif",
        custom_id="gif_start",
        components=[interactions.TextInput(
            style=interactions.TextStyleType.SHORT,
            label="start time (format HH:MM:SS)",
            custom_id="gif_start_time",
            min_length=1,
        )],
    )
    
    # send start modal
    await ctx.popup(gif_start_modal)

@bot.modal("gif_start")
async def modal_response(ctx, start_time: str):
  
  gif_info["start time"] = start_time
  
  # end_label = str(f'end time (format HH:MM:SS) max: {gif_info.get("video length")} ')
  
  # await ctx.send(f"pog {start_time}")
  
  # make gif end modal
  gif_end_modal = interactions.Modal(
        title="Make a gif",
        custom_id="gif_end",
        components=[interactions.TextInput(
            style=interactions.TextStyleType.SHORT,
            label="end time (format HH:MM:SS)",
            custom_id="gif_end_time",
            min_length=1,
            max_length=10,
        )],
    )
  
  await ctx.popup(gif_end_modal)
   
@bot.modal("gif_end")
async def modal_response(ctx, end_time: str):
    
  
  gif_info["end time"] = end_time
  
  await ctx.send(f"poggers {end_time}")
  
  '''
  #make gif_info embed
  embed = discord.Embed(title='Confirm Options', description='Are these correct?')
  for x, y in gif_info.items():
      embed.add_field(name=str(x) , value=str(y), inline=False)
   
  #create y/n buttons
  ybutton = interactions.Button(
      style=interactions.ButtonStyle.SUCCESS,
      label="Yes",
      custom_id="good_confirm",
  )
  
  nbutton = interactions.Button(
      style=interactions.ButtonStyle.DANGER,
      label="No",
      custom_id="bad_confirm",
  )
  
  row = interactions.ActionRow.new(ybutton, nbutton)
  
  # send embed and buttons
  await ctx.send(embeds=embed, components=row)
  '''
  
  
  


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

