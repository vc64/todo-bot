import discord
from discord.ext import commands

class main(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready():
      print("I'm in")
      print(client.user)


async def setup(bot):
  await bot.add_cog(main(bot))