import os, discord, random
from dotenv import load_dotenv
from content.quotes import nom_nom_quotes
from discord.ext import commands


#Storing API keys safely.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
#######bot = commands.Bot(command_prefix=">")
#on_ready() event handler, which handles the event when the Client has established a connection to Discord
@client.event
async def on_ready():
    print(f'{client.user} connection established to Discord!')

@client.event   #sending a welcome msg via dm
async def on_member_join(member):
    await member.create_dm()    
    await member.dm_channel.send(
        f'Hieee {member.name}, welcome to my Discord server!'
    )

@client.event   #error handling
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            pass

@client.event 
async def on_message(message):
    if(message.author == client.user):   
        return                          #Preventing recursive hole of bot replying to itself 
    
    if(message.content == "yum"):
        response = random.choice(nom_nom_quotes)
        await message.channel.send(response)
    elif(message.content == "Yum"):
        response = random.choice(nom_nom_quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

'''@bot.command(name="99")
async def nine_nine(ctx):
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name="yum")
async def nom_nome(ctx):
    response = random.choice(nom_nom_quotes)
    await ctx.send(response)'''

client.run(TOKEN)
#bot.run(TOKEN)

