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
    print("replace this with whatever u want it to say in console when bot is online")
@bot.event
async def on_member_join(member: discord.Member):
    member.create_dm()
    member.dm_channel.send("Welcome to the server :D")

@bot.command()
async def test1(ctx):
    ctx.send("This is a test!")

@bot.command()
async def test2(ctx):
    embed = discord.Embed(title="This is a test embed!", colour="blurple").add_field(name="Field 1", value="Field 2 (NOT IN LINE)", inline=False)

bot.run(os.getenv("BOT_TOKEN"))