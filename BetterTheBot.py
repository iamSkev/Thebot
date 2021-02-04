import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix = "-")


@bot.event
async def on_ready():
  print('Bot is ready')


@bot.command()
async def ping(ctx):
  await ctx.send(f'Ping! {round(bot.latency * 1000)}ms ')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)

@bot.command()
async def say(ctx, *, message=" "):
	if message == " ":
		await ctx.send("Dumbass try writing something for me to copy smh.")
	
	else:
		await ctx.send(message)
		await ctx.message.delete()




bot.run('Nzk5NzczMzIyNzE5MjY0ODg4.YAIc8w.hDzL1h8_m48KmTBrPkJ-l1LZFgw')