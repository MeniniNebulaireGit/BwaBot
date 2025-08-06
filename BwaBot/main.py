import discord
from discord.ext import commands, tasks
from discord import app_commands
import os
import logging
import datetime
import asyncio
import tracemalloc
import sys
from dotenv import load_dotenv
import json
import asyncio
from datetime import datetime, time

tracemalloc.start()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='bwa!', intents=intents)

async def load():
    for item in os.listdir("./cogs"):
        if item.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{item[:-3]}")
            except Exception as e:
                print(f"BWAAA ERROR from {item}: {e}")
def load_json(file):
    with open(file, "r") as f:
            return json.load(f)

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

@bot.tree.command(name="ping", description="Latency Pings")
async def ping(interaction: discord.Interaction):
    emb=discord.Embed(title="Pong!", description=f"{round(bot.latency * 1000)}ms", color=discord.Color.green())
    await interaction.response.send_message(embed=emb)

@tasks.loop(time=time(0,0))
async def dailyreset(interaction: discord.Interaction):
    default_data = {}
    print("Resetting Daily.Json")
    save_json("daily.json", default_data)
    print ("Json Reset")
    await interaction.response.send_message("Successfully reset Daily.Json")

@bot.event
async def on_ready():
    channel = bot.get_channel(1397856242281746464)
    starttime = datetime.datetime.now()

    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(type=discord.ActivityType.playing, name="BWA")
    )
    embed = discord.Embed(title="Bot Online!", color=discord.Color.dark_green())
    embed.add_field(name="Start Day:", value=f"```{starttime:%m/%d/%Y}```", inline=True)
    embed.add_field(name="Start Time:", value=f"```{starttime:%I:%M:%S %p}```", inline=True)
    embed.add_field(name="Bot Status:", value="```Ready!```", inline=False)
    await channel.send(embed=embed)

@bot.tree.command(name="sync", description="Syncs slash commands.")
@app_commands.allowed_installs(guilds=True, users=False)
async def sync(interaction: discord.Interaction, guild_id: str = None):
    if guild_id:
        guild = discord.Object(id=guild_id)
        bot.tree.copy_global_to(guild=guild)
        await bot.tree.sync(guild=guild)
        embed = discord.Embed(title="Synced slash commands!", color=discord.Color.green())
        embed.add_field(name="Guild", value=f"Synced to guild `{guild_id}`", inline=False)
        await interaction.response.send_message(embed=embed)
        print(f"{interaction.user.name} synced commands to guild {guild_id}")
    else:
        await bot.tree.sync()
        embed = discord.Embed(title="Synced slash commands!", color=discord.Color.green())
        embed.add_field(name="Global", value="Successfully synced commands globally!", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        print(f"{interaction.user.name} synced commands globally")

# Global app command error handler
@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error):
    logchannel = bot.get_channel(1397856242281746464)
    embed = discord.Embed(title="An error has occurred!", color=discord.Color.dark_red())
    embed.add_field(name="Error", value=f"```{error}```", inline=False)

    try:
        await interaction.response.send_message("An error has occurred! Check the logs channel.", ephemeral=True)
    except discord.InteractionResponded:
        await interaction.followup.send("An error has occurred! Check the logs channel.", ephemeral=True)

    await logchannel.send(embed=embed)

# Main entry
async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())