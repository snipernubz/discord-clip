import interactions
import json
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


# create continue/abort buttons
def create_con_btn(conid, contxt = "Continue", badid = "abort", badtxt = "Abort"):
    """
    Creates a Confirm and Abort button

    Args:
        conid (str): custom id for confirm button
        contxt (str): custom txt for confirm button
        badid (str): custom id for abort button
        badtxt (str): custom txt for abort button
    Returns:
        ActionRow: Actionrow containing the Confirm and Abort buttons
    """    
    
    fixedconid = str(conid)
    fixedcontxt = str(contxt)
    con_button = interactions.Button(
        style=interactions.ButtonStyle.SUCCESS,
        label=fixedcontxt,
        custom_id=fixedconid,
    )
    fixedbadid = str(badid)
    fixedbadtxt = str(badtxt)
    abr_button = interactions.Button(
        style=interactions.ButtonStyle.DANGER,
        label=fixedbadtxt,
        custom_id=fixedbadid,
    )
    
    
    con_abr_row = interactions.ActionRow.new(con_button, abr_button)
    return con_abr_row

@bot.command()
async def modal_pog(ctx):
    modal_pog = interactions.Modal(
        title="(clip) Choose Start time",
        custom_id="modal_start",
        components=[interactions.TextInput(
            style=interactions.TextStyleType.SHORT,
            label="Do some bull",
            custom_id="clip_start_time",
            min_length=1,
            max_length=8,
        )],
    )
    
    # send start modal
    await ctx.popup(modal_pog)
                    
@bot.modal("modal_start")
async def modal_response(ctx, start_pog: str):
  await ctx.send(content="continue", components=create_con_btn("pog_start_con"))

@bot.component("pog_start_con")
async def pog_start_con_response(ctx):
  pog_end_modal = interactions.Modal(
            title="(clip) Choose end time",
            custom_id="pog_end",
            components=[interactions.TextInput(
                style=interactions.TextStyleType.SHORT,
                label="more bull",
                custom_id="clip_end_time",
                min_length=1,
                max_length=10,
            )],
        )
  await ctx.popup(pog_end_modal)

@bot.modal("pog_end")
async def modal_response(ctx, end_time: str):
    await ctx.send(content="continue", components=create_con_btn("pog_end_con", "good", "pog_end_con_bad", "bad"))
    
@bot.component("pog_end_con")
async def pog_end_res(ctx):
    await ctx.send("good")
    
@bot.component("pog_end_con_bad")
async def pog_end_res_bad(ctx):
    await ctx.send("bad")
    
    
@bot.command()
async def modal_poggers(ctx):
    modal_poggers = interactions.Modal(
        title="(clip) Choose Start time",
        custom_id="modal_start_poggers",
        components=[interactions.TextInput(
            style=interactions.TextStyleType.SHORT,
            label="Do some bull",
            custom_id="clip_start_time",
            min_length=1,
            max_length=8,
        )],
    )
    
    # send start modal
    await ctx.popup(modal_poggers)
                    
@bot.modal("modal_start_poggers")
async def modal_response(ctx, start_poggers: str):
    await ctx.send(ephemral=True, content="continue", components=create_con_btn("poggers_start_con"))
@bot.component("poggers_start_con")
async def poggers_start_con_response(ctx):
    
    poggers_end_modal = interactions.Modal(
            title="(clip) Choose end time",
            custom_id="poggers_end",
            components=[interactions.TextInput(
                style=interactions.TextStyleType.SHORT,
                label="more bull",
                custom_id="clip_end_time",
                min_length=1,
                max_length=10,
            )],
        )
    
    await ctx.send(poggers_end_modal)

@bot.modal("poggers_end")
async def modal_response(ctx, end_time: str):
    await uno_ctx.edit(ephemral=True, content="continue", components=create_con_btn("poggers_end_con", "good", "poggers_end_con_bad", "bad"))
    
@bot.component("poggers_end_con")
async def poggers_end_res(ctx):
    await ctx.send("good")
    
@bot.component("poggers_end_con_bad")
async def poggers_end_res_bad(ctx):
    await ctx.send("bad")
    
bot.start()