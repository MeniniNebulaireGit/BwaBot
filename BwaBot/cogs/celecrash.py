from discord.ext import commands
from discord import app_commands
import discord

class celecrash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Celebrate/Crashout Cog has been loaded!')

    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(
        name="celebrate",
        description="Celebrate!",
    )
    async def celebrate(self, interaction: discord.Interaction, celebrating: str=None):
        if celebrating:
            embed=discord.Embed(title=f"{interaction.user.display_name} is celebrating:", description=f"{celebrating}", color=discord.Color.green())
            embed.set_image(url="https://c.tenor.com/U-dCikr2sLIAAAAd/tenor.gif")
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title=f"{interaction.user.display_name} is celebrating:", description=f"", color=discord.Color.green())
            embed.set_image(url="https://c.tenor.com/U-dCikr2sLIAAAAd/tenor.gif")
            await interaction.response.send_message(embed=embed)

    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(
        name="crash-out",
        description="Crash the fuck out",
    )
    async def crashout(self, interaction: discord.Interaction):
        embed=discord.Embed(title=f"{interaction.user.display_name} is crashing out!", color=discord.Color.dark_red())
        embed.set_image(url="https://c.tenor.com/2W8tjsbzPXYAAAAd/tenor.gif")
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(celecrash(bot))