import discord
import discord.ext
from discord import channel
from discord.ext import commands
from discord import app_commands
import json
import os

dailycheck = "daily.json"
default_data = {}
if not os.path.exists(dailycheck):
    with open(dailycheck, 'w') as f:
        json.dump(default_data, f)

def load_json(file):
    with open(file, "r") as f:
            return json.load(f)

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

data = load_json(dailycheck)



class daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Daily Cog has been loaded!')

    @app_commands.command(name="daily")
    async def daily(self, interaction: discord.Interaction):
        data = load_json(dailycheck)
        user_id = str(interaction.user.id)
        if 'daily' not in data:
            data['daily'] = []
        if user_id in data['daily']:
            await interaction.response.send_message("Already run this command")
            return

        if 'daily' not in data:
            data['daily'] = []



        if user_id not in data['daily']:
            data['daily'].append(user_id)

        save_json(dailycheck, data)

        await interaction.response.send_message("Daily commands executed successfully")


    @app_commands.command(name="dailyboard", description="List who's claimed their dailies!")
    async def dailyboard(self, interaction: discord.Interaction):
        data = load_json(dailycheck)
        claimed = data.get("daily", [])
        if not claimed:
            await interaction.response.send_message("No Claimed Dailies Yet")
            return

        user_names = []
        for user_id_str in claimed:
            try:
                user_id = int(user_id_str)
                user = await self.bot.fetch_user(user_id)
                if user:
                    user_names.append(user.display_name)
            except discord.NotFound:
                user_names.append(f"Unknown User (ID: {user_id_str})")
            except ValueError:
                user_names.append(f"Invalid ID: {user_id_str}")
        if user_names:
            board_message = "Users who claimed their daily:\n" + "\n".join(user_names)
        else:
            board_message = "Could not retrieve any user names."

        await interaction.response.send_message(board_message)





async def setup(bot):
    await bot.add_cog(daily(bot))



