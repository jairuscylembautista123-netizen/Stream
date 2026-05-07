
from discord.ext import commands
import os

client = commands.Bot(command_prefix="!", self_bot=True)

@client.event
async def on_ready():
    # This is the "Smart Analysis" bypass to turn you purple!
    await client.change_presence(activity=discord.Streaming(name="GRINDING XIALITY_SMP 🗿", url="https://twitch.tv/xiality"))
    print(f"STATUS: PURPLE_MAXXING | USER: {client.user}")

client.run(os.getenv("TOKEN"), bot=False)
