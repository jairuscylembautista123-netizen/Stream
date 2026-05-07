import discord
from discord.ext import commands

# You'll need to install: pip install discord.py-self
client = commands.Bot(command_prefix='.', self_bot=True)

@client.event
async def on_ready():
    print(f'Connected to: {client.user}')
    
    # This triggers the purple "Streaming" status
    await client.change_presence(
        activity=discord.Streaming(
            name="Your Custom Text Here", 
            url="https://www.twitch.tv/discord"
        )
    )

# Use your Account Token here (NOT a bot token)
client.run("MTQxOTE5Nzc0NTk2NDY1MDQ5OA.GEb7BE.d5hITN3zg2-85IQK2w_Sg8RJV2CbnCoMKDMbUE")
