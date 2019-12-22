import os, discord, random
from dotenv import load_dotenv
from content.quotes import *
from discord.ext import commands


#Storing API keys safely.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client()
bot = commands.Bot(command_prefix=">", description='A tasty bot for tasty food')

#on_ready() event handler, which handles the event when the Client has established a connection to Discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} connection established to Discord!')

@bot.event   #sending a welcome msg via dm
async def on_member_join(member):
    await member.create_dm()    
    await member.dm_channel.send(
        f'Hieee {member.name}, welcome to my Discord server!'
    )

@bot.event   #error handling
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            pass


@bot.command(name = "99") 
async def nine_nine(ctx):
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name = "yum")
async def nom_nome(ctx):
    try:
        response = random.choice(nom_nom_quotes)
        await ctx.send(response)
    except:
        raise discord.DiscordException

@bot.command(mame = "info")
async def info(ctx):
    embed = discord.Embed(title="NomNom", description="A discord bot dedicated to yummy food", color=0xeee657)

    # give info about you here
    embed.add_field(name="Maker", value="ScreX")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=289205523390267402&permissions=8&scope=bot)")
    await ctx.send(embed = embed)

@bot.command(name = "toni")
async def toni(ctx):
    #embed = discord.Embed()
    #embed.set_image(url = "https://imgur.com/gallery/iX06rQg")
    try:
        await ctx.send("https://imgur.com/gallery/iX06rQg")
    except:
        pass

@bot.command(name = "search")
async def search(ctx,*,arg):
    link = f'https://pixabay.com/images/search/{arg}/'
    await ctx.send(link.replace(" ",""))

@bot.command(name = "fsearch")
async def fsearch(ctx,*,arg):
    link = f'https://www.foodiesfeed.com/?s={arg}'
    await ctx.send(link.replace(" ","+"))
    
@bot.command(name = "recipe")
async def recipe(ctx,*,arg):
    link = f'https://www.allrecipes.com/search/results/?wt={arg}&sort=re'
    #print(link)
    await ctx.send(link.replace(" ",""))

#client.run(TOKEN)
bot.run(TOKEN)

