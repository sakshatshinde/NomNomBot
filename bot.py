import os, discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#on_ready() event handler, which handles the event when the Client has established a connection to Discord
@client.event
async def on_ready():
    print(f'{client.user} connection established to Discord!')

client.run(token)