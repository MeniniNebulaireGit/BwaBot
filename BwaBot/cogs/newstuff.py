import discord
import discord.ext
from discord import channel
from discord.ext import commands


class newstuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.messagelog = get_messagelog_from_txt("config.txt")  # your log channel ID here
        self.guild_id = get_guild_id_from_txt("config.txt")  # guild to restrict logging to

    @commands.Cog.listener()
    async def on_ready(self):
        print('New Stuff Cog has been loaded!')

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message, guild: self.guild_id):
        channel = self.bot.get_channel(self.messagelog.channel_id)
        if before.author.bot:
            return
        if channel is None:
            return
        embed = discord.Embed(title="Edited message!", description=f"before: {before.content}\nafter: {after.content}")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if message.author.bot:
            return
        if message.guild is None:
            return
        if channel is None:
            return
        embed = discord.Embed(title="Deleted message!", description=f"")
        embed.add_field(name="Message", value=message.content, inline=False)
        embed.add_field(name="Author", value=message.author.mention, inline=False)
        await message.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(newstuff(bot))