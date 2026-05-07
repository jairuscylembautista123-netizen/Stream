import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    # This is the "Streaming" activity that turns the status purple
    await bot.change_presence(activity=discord.Streaming(
        name="Custom Status Text Here", 
        url="https://www.twitch.tv/directory"
    ))
    print(f'Logged in as {bot.user.name} and set purple status!')

bot.run('YOUR_TOKEN_HERE')
