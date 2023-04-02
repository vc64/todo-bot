import os
import discord
import asyncio
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(intents=discord.Intents.all(), command_prefix = "!")

async def load():
  for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      await bot.load_extension(f"cogs.{filename[:-3]}")
# await bot.add_cog(NotionPolling(bot))

# @client.event
# async def on_ready():
#     print("I'm in")
#     print(client.user)

async def main():
  await load()
  keep_alive()
  await bot.start(os.environ['DISCORD_BOT_SECRET'])

asyncio.run(main())
# keep_alive()
# my_secret = os.environ['DISCORD_BOT_SECRET']
# client.run(my_secret)