from dotenv import load_dotenv
from discord.ext import commands
import discord
import os

load_dotenv()

intents = discord.Intents.default()
discord.Intents.members = True
discord.Intents.message_content = True


bot = commands.Bot(command_prefix="proto ", intents=intents)

@bot.event
async def on_ready():
    print("hi im online lol")
@bot.event
async def on_member_join(member: discord.Member):
    member.create_dm()
    member.dm_channel.send("welcome to the server :D \n hope you'll have fun! \n \n Link is here if you want to join again ^^ \n https://discord.gg/bspWs6v59G")

@bot.command()
async def yt(ctx):
    ctx.send("BZZRT- here you go! ^^ \n https://www.youtube.com/channel/UCZsVjiMSN9Y2s3gFnMNwxqg")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="proto help", colour="blurple").add_field(name="Field 1", value="Field 2 (NOT IN LINE)", inline=False)

bot.run(os.getenv("BOT_TOKEN"))