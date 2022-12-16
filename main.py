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
    await ctx.send(f"Ping! {bot.latency}ms")

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
            label=" Let's get straight to it: what's 1 + 1? HINT: its 2 jk its 5 dumbass",
            custom_id="text_input_response",
            min_length=2,
            max_length=10,
                )],
    )

    await ctx.popup(modal)
 
@bot.modal("mod_form")
async def modal_response(ctx, response: str):
    await ctx.send(f"You wrote: {response}", ephemeral=True)
    
@bot.command()
async def dual_modal_test(ctx):
    """dual modal test command"""
    dual_modal = interactions.Modal(
        title="Poggers",
        custom_id="dual_modal",
        components=[interactions.TextInput(
            style=interactions.TextStyleType.SHORT,
            label="1st input",
            custom_id="first_input",
        ),
        interactions.TextInput(
            style=interactions.TextStyleType.SHORT,
            label="2nd input",
            custom_id="sec_input",
        )],
    )

    await ctx.popup(dual_modal)

@bot.modal("dual_modal")
async def dual_modal_res(ctx, uno: str, sec: str):
    print(f"first input: {uno}, second input: {sec}")   
    await ctx.send(f"first input: {uno}, second input: {sec}")        
    
    
@bot.command()
async def select_test(ctx):
    """ Select Menu Test """
    Menu = interactions.SelectMenu(
        options=[
            interactions.SelectOption(
                label="opt 1",
                value="poggers",
                description="pogging",
            ),
            interactions.SelectOption(
                label="opt 2",
                value="memeing",
                description="we memeing",
            )
        ],
        placeholder="Check out these things",
        custom_id="select_test",
    )
    
    await ctx.send("**Choose!**", components=Menu)

@bot.component("select_test")
async def select_res(ctx, res: str):
    await ctx.edit(f"You chose {str(res)} from the SelectMenu", components="")
    
################# actual commands  #####################

 # functions to help with varying tasks

def convert_sec(sec):
    """
    Converts Seconds into a HH:MM:SS format
    Args:
        sec (string): Time in Seconds

    Returns:
        string : Time in HH:MM:SS format
    """
    
    td = timedelta(seconds = sec)
    return str(td)
  
def convert_hms(time):
    """
    Converts HH:MM:SS into Seconds

    Args:
        time (string): HH:MM:SS string

    Returns:
        string : Time in Seconds
    """    
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

   
# create continue/abort buttons
def create_con_btn(inputid):
    """
    Creates a Confirm and Abort button

    Args:
        inputid (str): custom id for confirm button

    Returns:
        ActionRow: Actionrow containing the Confirm and Abort buttons
    """    
    
    fixedid = str(inputid)
    con_button = interactions.Button(
        style=interactions.ButtonStyle.SUCCESS,
        label="Continue",
        custom_id=fixedid,
    )
  
    abr_button = interactions.Button(
        style=interactions.ButtonStyle.DANGER,
        label="Abort",
        custom_id="abort",
    )
    
    
    con_abr_row = interactions.ActionRow.new(con_button, abr_button)
    return con_abr_row
 
@bot.component("abort")
async def button2_response(ctx):
    await ctx.send("You chose to abort")

def createSelectOpt(dict):
    """ Create list of select Options from a dict """
    Selectopt = []
    for x, y in dict.items():
        Selectopt.append(interactions.SelectOption(label=x, value=y))
    return Selectopt



# make command

    # functions and Variables specific to the "make" command

vid_info = {}
res_itag = {}
download_con = False

def downloadCompleted(stream, path):
    download_con = True

@bot.command()
@autodefer(delay=3, ephemeral=True)
async def make(ctx: interactions.CommandContext):
    """make command"""
    pass


#make gif command
    # code for the "make gif" subcommand

@make.subcommand()
@interactions.option()
async def gif(ctx: interactions.CommandContext, gif_link: str):
    """Make a gif from a video"""
    
    
    print(f"Link: {gif_link}")
    
    video_url = str(gif_link)
    global videoobj 
    videoobj = YouTube(url=video_url, on_complete_callback=downloadCompleted(stream, path))
    
    # check video avalability
    videoobj.check_availability()
    
    print(f"Video title: '{videoobj.title}' video has length of '{videoobj.length}' seconds") 

    # add video info to vid_info 
    vid_info["video link:"] = video_url
    vid_info["video title:"] = videoobj.title
    vid_info["video length:"] = convert_sec(videoobj.length)
    
    
    # make gif start modal
    gif_start_modal = interactions.Modal(
        title="(gif) Choose Start time",
        custom_id="gif_start",
        components=[interactions.TextInput(
            style=interactions.TextStyleType.SHORT,
            label="start time (format HH:MM:SS)",
            custom_id="gif_start_time",
            min_length=1,
            max_length=8,
        )],
    )
    
    # send start modal
    await ctx.popup(gif_start_modal)



@bot.modal("gif_start")
async def modal_response(ctx, start_time: str):
  
  
  vid_info["start time:"] = start_time
  
  await ctx.send(content="choose end time", components=create_con_btn("gif_start_con"))

  

@bot.component("gif_start_con")
async def gif_start_con_response(ctx):
    
    # make gif end modal
    
    end_label = str(f'end time MAX: {vid_info.get("video length:").upper()} (format HH:MM:SS)')
    
    gif_end_modal = interactions.Modal(
            title="(gif) Choose end time",
            custom_id="gif_end",
            components=[interactions.TextInput(
                style=interactions.TextStyleType.SHORT,
                label=end_label,
                custom_id="gif_end_time",
                min_length=1,
                max_length=10,
            )],
        )
    
    await ctx.popup(gif_end_modal)
    

@bot.modal("gif_end")
async def modal_response(ctx, end_time: str):
    
    vid_info["end time:"] = end_time
    
    # make gif quality Selectmenu
    
    video_streams = videoobj.streams.filter(only_video=True, file_extension="webm")

    
    for x in video_streams:
        res_itag[x.resolution] = x.itag
    
    
    Menu = interactions.SelectMenu(
            placeholder="Check out these things",
            custom_id="select_qual",
            options=createSelectOpt(res_itag),
            
        )
    
    await ctx.send(components=Menu)

  
@bot.component("select_qual")
async def select_qual_res(ctx, response: str):
    
    
    vid_info["resolution:"] = videoobj.streams.get_by_itag(int(response[0])).resolution
    
    vid_info["approx size:"] = videoobj.streams.get_by_itag(int(response[0])).filesize_mb
    
    vid_info["itag:"] = response[0]
    
    
    await ctx.edit(content="Final confirm", components=create_con_btn("gif_qual"))
    
    

@bot.component("gif_qual")
async def final_confirm(ctx):
    
    #make vid_info embed
    
    info_embed = interactions.Embed(title='Confirm Options', description='Are these correct?')
    for x, y in vid_info.items():
        info_embed.add_field(name=str(x) , value=str(y), inline=False)
   
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
    await ctx.send(embeds=info_embed, components=row) 


@bot.component("good_confirm")
async def good_confirm_res(ctx):
    await ctx.disable_all_components()
    await ctx.send("Downloading video now")
    
    # download the video
    print("downlading the video")
    videopath = videoobj.streams.get_by_itag(int(vid_info["itag:"])).download(filename=ytvid_gif)
    if download_con == True:
        print("Video Downloaded")
        await ctx.edit("Video Downloaded \n Beginning the clipping process")
    
    # moviepy shit
    
    #vidClip = VideoFileClip
    
    
@bot.component("bad_confirm")
async def bad_confirm_res(ctx):
    await ctx.disable_all_components()
    await ctx.send("Command Canceled, please run it again")
  
  

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


