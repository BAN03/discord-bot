import discord
from discord.ext import commands

API = "OTk2OTA0NDQ1MjEwMjgwMDA3.Gassmm.e1SgziJFpPU_CIib3gE-1znHCMhd7ajlg8I2ZI"
bot = commands.Bot(command_prefix='>')

if __name__ == "__main__":

    #Inicio del bot
    @bot.event
    async def on_ready():
        print(f"La {bot.user} esta lista")

    @bot.command(name="ping")
    async def ping(ctx):
        await ctx.send(f"pong: {bot.latency}")

    @bot.command(name="pija")
    async def pija(ctx, arg="<@750802687917948958>"):
        await ctx.send(f"como te encanta la pija {arg}")

    @bot.command(name="lick")
    async def lick(ctx, arg="<@750802687917948958>"):
        await ctx.send(f"chupala {arg}")

    @bot.command(name="id")
    async def id(ctx, user:discord.User=None):
        if not user:
            userId = ctx.author.id
        else:
            userId = user.id
        await ctx.send(f"Id: {userId}")

    @bot.command(name="say")
    async def say(ctx, *, args):
        await ctx.send(args, tts=True)
    

    bot.run(API)

