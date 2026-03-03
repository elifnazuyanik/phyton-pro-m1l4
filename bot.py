import discord
from discord.ext import commands
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def biktim(ctx):
    await ctx.send(f'ben de. Hadi camdan atlayalım')

@bot.command()
async def dizi(ctx):
    await ctx.send(f'hmm... The Amazing Dijital Circus, Murder Drones,Stranger Things ya da Umbrella Academy olabilir. Daha aklıma gelirse yazarım.')



@bot.group()
async def cool(ctx):

    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')
bot.run(TOKEN)

