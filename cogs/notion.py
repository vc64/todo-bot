from discord.ext import commands, tasks
import datetime
import pytz
import os
from notion-client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])

# est = pytz.timezone('US/Eastern')
utc = datetime.timezone.utc

# If no tzinfo is given then UTC is assumed.
times = [
    datetime.time(hour=8, tzinfo=utc),
    datetime.time(hour=12, tzinfo=utc),
    datetime.time(hour=16, minute=30, tzinfo=utc),
    datetime.time(hour=18, minute=30, tzinfo=utc),
    datetime.time(hour=22, tzinfo=utc)
]

class NotionPolling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=times)
    async def my_task(self):
        users = notion.users.list()
      
        for user in users.get("results"):
          name, user_type = user["name"], user["type"]
          emoji = "😅" if user["type"] == "bot" else "🙋‍♂️"
          print(f"{name} is a {user_type} {emoji}")

async def setup(bot):
    await bot.add_cog(NotionPolling(bot))