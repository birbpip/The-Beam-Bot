from discord.ext import commands 
import discord

BOT_TOKEN = ""
CHANNEL_ID = 1224270693039079525
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
rock = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠋⠈⠀⠀⠀⠀⠐⠺⣖⢄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⢀⡆⠀⠀⠀⢋⣭⣽⡚⢮⣲⠆⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⡼⠀⠀⠀⠀⠈⠻⣅⣨⠇⠈⠀⠰⣀⣀⣀⡀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⢷⣶⠶⣃⢀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠈⠓⠚⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⡠⠀⡄⣀⠀⠀⠀⢻⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠐⠉⠀⠀⠙⠉⠀⠠⡶⣸⠁⠀⣠⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣦⡆⠀⠐⠒⠢⢤⣀⡰⠁⠇⠈⠘⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠠⣄⣉⣙⡉⠓⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⠀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""
sigmacopypasta = """2:00 am- Wake up

2.05am-Cold shower

2.15am-breakfast,almonds, breast milk bought off Facebook, 50mg adderall

2:30am- begin workout,incline bench 2 plates,12x12 with 30 seconds of rest, no warmup.

2:45am-edging,4hrs (for disipline)

6:45am-cold shower

7:00am-begin sprint to work

8:00am-arrive at work

8:05am-get called into boss' office

8:06am-get fired from job for "repeated inappropriate comments" and "predatory behaviour"

8:10am-sprint back home

9:10am- lunch-raw cod, berries foraged on the way home, small pebbles (for digestion),50mg of adderal

9:10am-edging(as punishment)

3:00pm- bed time"""
chineescopypasta = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠶⠾⣉⡉⠉⠑⠲⢤⡘⡏⠳⣄⢠⠴⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡖⢦⡀⠀⡠⠔⡲⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠳⡀⠀⠀⠙⠓⠀⠸⠃⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣳⠀⢳⠎⠀⢰⣁⡤⠒⠈⠉⠉⢉⣶⠦⠀⠀⠀
⠀⠀⣶⣀⣠⣶⣊⠉⠙⢷⡄⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠛⠁⠀⠀⠀⣠⠞⠉⠀⠀⠀⠀⠀
⠀⠀⣇⠈⠳⢤⣈⣳⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠋⠉⣙⣶⡄⠀⢀⠀
⠀⠀⠙⢦⡀⠀⠀⠀⠀⣀⡤⠖⠊⠉⠉⢉⣳⣤⡀⠀⠙⢆⠀⠀⠀⠀⠀⡴⠋⠀⠀⢀⣀⡤⢄⣀⡀⠀⠀⠀⠰⠾⠭⣀⡠⠤⠒⢹⠇
⠀⠀⠀⠀⣉⣱⠒⠊⠙⢧⠀⠀⠀⠀⢰⠋⠀⠈⢻⢦⣀⠈⣆⠀⠀⠀⡼⠀⢀⣴⠞⠉⠉⢳⠀⠀⠈⠑⠲⣤⣀⡀⠀⠀⠀⠀⣠⠞⠀
⠀⢀⡴⠋⢠⠇⠀⠀⠀⠈⣗⠦⣀⡀⠘⢦⣀⣠⠜⢀⣨⣿⠿⠓⠀⠘⠳⢾⣅⠘⣄⠀⢀⡼⠁⠀⠀⢀⣴⠃⠀⠈⡿⠿⣍⡉⠀⠀⠀
⢠⡏⠀⠀⢸⡄⠀⠀⠀⠀⠈⠲⢄⣉⠉⠒⠒⣒⡫⠝⠋⠁⠀⠀⠀⠀⠀⠀⠙⠫⣗⡯⣭⣤⣤⡤⣖⠽⠋⠀⠀⠀⣸⠀⠀⠙⢆⠀⠀
⣸⠀⠀⡀⠀⠹⣄⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⣰⠏⠀⡀⠀⠘⡆⠀
⢸⠀⠀⢹⣄⠀⠀⠙⠲⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⣰⡇⠀⠀⡇⠀
⢾⣧⣤⠐⠛⣦⡀⠀⠀⠀⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠖⠉⠀⠀⢀⣴⡟⠀⠀⣸⠁⠀
⠀⠘⠿⣍⠉⠙⢿⣦⣀⠀⠀⠙⢦⡀⠀⠀⠀⠀⢀⡤⠒⠉⠁⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀⣀⠔⠁⠀⠀⣠⣴⠧⠤⣈⣑⡶⠇⠀⠀
⠀⠀⠀⠈⢳⡀⠀⠉⠛⢷⣤⣀⠀⠈⣲⠤⠖⠒⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠑⠒⢴⡞⠁⠀⣀⡴⠞⠋⠀⠀⢰⠖⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⣦⡀⠀⠀⠈⠙⠻⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠹⡾⠛⠁⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⣷⣄⠀⠀⠀⢣⠀⠀⠀⠀⠈⠉⢦⠀⠀⠀⠀⠀⠀⡔⠉⠀⠉⠀⠀⢰⠇⠀⠀⠀⢠⡶⠊⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠻⣍⠉⠀⠀⢸⢦⣀⠀⠀⠀⢀⡼⠦⣄⣀⣀⣀⡴⣇⠀⠀⠀⠀⣠⡟⠀⠀⠀⢐⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠲⣿⡷⠬⣉⣉⡉⠉⠀⢀⣀⣀⣀⣀⡀⠈⠓⠶⢶⡾⢿⢿⠖⠒⠒⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⡱⣄⠀⠘⡏⠉⡏⠁⠀⠀⠀⠀⠉⢹⡋⠉⡇⣠⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡌⢆⠀⠙⠒⠃⠀⠀⠀⠀⠀⠀⠀⠙⠚⠀⣧⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⢸⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⢸⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⠀⡟⢦⠀⡀⠀⠀⠀⠀⣀⣰⢋⠃⡎⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡈⢆⣧⣘⣟⣙⣆⣀⣀⣏⣉⣇⡼⠛⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠒⠒⠊⠉⠀⠈⠉⠑⠒⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
result = ""
with open("ip.txt", "r") as file:
    result = file.read().replace("\n", "")
with open("token.txt", "r") as file:
    BOT_TOKEN = file.read().replace("\n", "")

# will print ATCAGTGGAAACCCAGTGCTAGAGGATGGAATGACCTTAAATCAGGGACGATATTAAACGGAA


@bot.event
async def on_ready():
    print(result)
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("SKEBAB TOILET :fire:")
    
@bot.command()
async def skibidi(ctx):
    await ctx.send("Toilet!")
@bot.command()
async def ip(ctx):
    await ctx.send("The ip is %s:25565" % (result))
@bot.command()
async def therock(ctx):
    await ctx.send(rock)
@bot.command()
async def sigma(ctx):
    await ctx.send(sigmacopypasta)
@bot.command()
async def chinese(ctx):
    await ctx.send(chineescopypasta)
@bot.command()
async def nlgga(ctx):
    await ctx.send("nlgga :ngga:")
@bot.command()
async def bothelp(ctx):
    await ctx.send("Available Commands:")
    await ctx.send("!skibidi")
    await ctx.send("!ip")
    await ctx.send("!therock")
    await ctx.send("!sigma")
    await ctx.send("!chinese")
    await ctx.send("!nlgga")
    await ctx.send("!bothelp")
    await ctx.send("!botinfo")
@bot.command()
async def botinfo(ctx):
    await ctx.send("This bot is made by pipboy")
    await ctx.send("https://github.com/birbpip/birbpip")
@bot.command()
async def deleteallmessages(ctx):
    await ctx.channel.purge(limit=1000)
    await ctx.send("Deleted all messages")

@bot.command()
async def roastniki(ctx):
    await ctx.send("<@879686456002617414> you suck")





bot.run(BOT_TOKEN)
