import asyncio

from discord.ext import commands
from discord import app_commands
import discord
import random

inventories = {}

class membinteract(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Interactions Cog has been loaded!')

        # Go Fuck Yourself
        @app_commands.allowed_installs(guilds=True, users=True)
        @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
        @app_commands.command(name="gfy", description="Tells you to go fuck yourself")
        async def gfy(self, interaction: discord.Interaction, user: discord.User):
            variable_list = [
                'https://c.tenor.com/GbwILUMfIkIAAAAd/tenor.gif',
                'https://c.tenor.com/fTz7Bko5y20AAAAC/tenor.gif',
                'https://c.tenor.com/7wmF5O6ECl8AAAAC/tenor.gif',
                'https://media.tenor.com/N4DkLsYBKxkAAAAi/pixel-middle-finger.gif',
                'https://c.tenor.com/j6RBLGjuH44AAAAC/tenor.gif',
            ]
            emb = discord.Embed(title=f"", color=discord.Color.dark_gray())
            emb.add_field(name="", value=f"GO FUCK YOURSELF!")
            emb.set_image(url=f"{random.choice(variable_list)}")
            await interaction.response.send_message(f"{user.mention}", embed=emb)

# Rate Users Command
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="rate", description="get a random rating number 1-100")
    async def rate(self, interaction: discord.Interaction, user: discord.User=None):
        target = user or interaction.user
        name = target.display_name
        mention = target.mention
        random_result = random.randint(1, 100)
        # Assign color based on range
        if random_result < 10:
            color = discord.Color.dark_red()
        elif random_result < 20:
            color = discord.Color.red()
        elif random_result < 30:
            color = discord.Color.orange()
        elif random_result < 40:
            color = discord.Color.dark_orange()
        elif random_result < 50:
            color = discord.Color.gold()
        elif random_result < 60:
            color = discord.Color.yellow()
        elif random_result < 70:
            color = discord.Color.dark_green()
        elif random_result < 80:
            color = discord.Color.green()
        elif random_result < 90:
            color = discord.Color.teal()
        else:
            color = discord.Color.blurple()

        embed = discord.Embed(
            title=f"{name}'s rating is:",
            color=color)
        embed.add_field(name="\u200b", value=f"**{random_result}** out of 100!")
        await interaction.response.send_message(content=mention, embed=embed)

#Gaydar Command
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="gaydar", description="Gaydar Command")
    async def gaydar(self, interaction: discord.Interaction, user: discord.User):
        random_result = random.randint(1, 100)
        if user is not None:
            if user.id == 340546691491168257:
                embed = discord.Embed(title=f"SCANNING {user.name} WITH GAYDAR:", color=discord.Color.blurple())
                embed.add_field(name=f"", value=f"{user.mention} is 100000000% gay! <a:gaysheep:1398109951267836035> ")
                await interaction.response.send_message(embed=embed)
            if user.id == 699805861404737567:
                embed = discord.Embed(title=f"SCANNING {user.name} WITH GAYDAR:", color=discord.Color.blurple())
                embed.add_field(name=f"", value=f"{user.mention} is 400% gay! <a:gaysheep:1398109951267836035> ", inline=False)
                embed.add_field(name="", value="``████████████████``", inline=False)
                await interaction.response.send_message(embed=embed)
            elif user.id != 340546691491168257 or user.id != 699805861404737567:
                if random_result < 5:
                    embed = discord.Embed(title=f"SCANNING {interaction.user.mention} WITH GAYDAR:", color=discord.Color.dark_red())
                    embed.add_field(name=f"", value=f"{interaction.user.mention} is {random_result}% Gay!", inline=False)
                    embed.add_field(name="", value="``███_______``", inline=False)
                    await interaction.response.send_message(embed=embed)
                if random_result < 25:
                    embed = discord.Embed(title=f"SCANNING {user.name} WITH GAYDAR:", color=discord.Color.red())
                    embed.add_field(name=f"", value=f"{user.mention} is {random_result}% Gay <:VivianBwaah:1393137248219824168>", inline=False)
                    embed.add_field(name="", value="``███_______``", inline=False)
                    await interaction.response.send_message(embed=embed)
                elif random_result > 25 and random_result < 50:
                    embed = discord.Embed(title=f"SCANNING {user.name} WITH GAYDAR:", color=discord.Color.orange())
                    embed.add_field(name=f"", value=f"{user.mention} is {random_result}% Gay <:Robin_DontWanttoLook:1393137127751155712>", inline=False)
                    embed.add_field(name="", value="``█████____``", inline=False)
                    await interaction.response.send_message(embed=embed)
                elif random_result > 50 and random_result < 75:
                    embed = discord.Embed(title=f"SCANNING {user.name} WITH GAYDAR:", color=discord.Color.yellow())
                    embed.add_field(name=f"", value=f"{user.mention} is {random_result}% Gay! <:FuwaApprob:1393869229052395631>", inline=False)
                    embed.add_field(name="", value="``███████___``", inline=False)
                    await interaction.response.send_message(embed=embed)
                elif random_result > 75:
                    embed = discord.Embed(title=f"SCANNING {user.name} WITH GAYDAR:", color=discord.Color.green())
                    embed.add_field(name=f"", value=f"{user.mention} is {random_result}% Gay!!! <:Shaved:1396614898867241052>", inline=False)
                    embed.add_field(name="", value="``██████████``", inline=False)
                    await interaction.response.send_message(embed=embed)
            if user is None:
                if random_result < 5:
                    embed = discord.Embed(title=f"SCANNING {interaction.user.mention} WITH GAYDAR:", color=discord.Color.dark_red())
                    embed.add_field(name=f"", value=f"{interaction.user.mention} is {random_result}% Gay!", inline=False)
                    embed.add_field(name="", value="``███_______``", inline=False)
                    await interaction.response.send_message(embed=embed)
                if random_result < 25:
                    embed = discord.Embed(title=f"SCANNING {interaction.user.mention} WITH GAYDAR:", color=discord.Color.red())
                    embed.add_field(name=f"", value=f"{interaction.user.mention} is {random_result}% Gay!", inline=False)
                    embed.add_field(name="", value="``███_______``", inline=False)
                    await interaction.response.send_message(embed=embed)
                elif random_result > 25 and random_result < 50:
                    embed = discord.Embed(title=f"SCANNING {interaction.user.mention} WITH GAYDAR:", color=discord.Color.red())
                    embed.add_field(name=f"", value=f"{interaction.user.mention} is {random_result}% Gay!", inline=False)
                    embed.add_field(name="", value="``█████____``", inline=False)
                    await interaction.response.send_message(embed=embed)
                elif random_result > 50 and random_result < 75:
                    embed = discord.Embed(title=f"SCANNING {interaction.user.mention} WITH GAYDAR:", color=discord.Color.yellow())
                    embed.add_field(name=f"", value=f"{interaction.user.mention} is {random_result}% Gay!", inline=False)
                    embed.add_field(name="", value="``███████___``", inline=False)
                    await interaction.response.send_message(embed=embed)
                elif random_result > 75:
                    embed = discord.Embed(title=f"SCANNING {interaction.user.mention} WITH GAYDAR:", color=discord.Color.green())
                    embed.add_field(name=f"", value=f"{interaction.user.mention} is {random_result}% Gay!", inline=False)
                    embed.add_field(name="", value="``██████████``", inline=False)
                    await interaction.response.send_message(embed=embed)

# Testing
    @app_commands.command(name="ping2", description="Ping")
    async def ping2(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong!")

# Cog Command Test
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.allowed_contexts(guilds=True, dms=False, private_channels=False)
    @app_commands.command(name="cogtest", description="Tests if cog commands function")
    async def cogtest(self, interaction: discord.Interaction, user: discord.User):
        emb = discord.Embed(title=f"test success", color=discord.Color.dark_gray())
        await interaction.response.send_message(f"{interaction.user.mention}", embed=emb)

# KYS
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="kys", description="Tell someone they should keep themselves safe.")
    async def kys(self, interaction: discord.Interaction, user: discord.User):
        emb = discord.Embed(title=f"", color=discord.Color.orange())
        emb.add_field(name="", value=f"YOU SHOULD KEEP YOURSELF SAFE!")
        emb.set_image(url="https://c.tenor.com/GbwILUMfIkIAAAAd/tenor.gif")
        await interaction.response.send_message(f"{interaction.user.display_name} has a message for {user.mention}...", embed=emb)

# Beg
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="beg", description="Beg for money")
    async def beg(self, interaction: discord.Interaction, user: discord.User):
        emb = discord.Embed(title=f"", color=discord.Color.orange())
        emb.add_field(name="", value=f"<:hampter:1394254552387293297>")
        emb.set_image(url="https://c.tenor.com/vcYOSa1pAcQAAAAd/tenor.gif")
        await interaction.response.send_message(f"{interaction.user.mention} begs {user.mention} for money", embed=emb)

    # You've lost them
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="lose", description="Lose your companion...")
    async def lose(self, interaction: discord.Interaction, user: discord.User):
        emb = discord.Embed(title=f"", color=discord.Color.orange())
        emb.add_field(name="", value=f"You've been sent to.. huh? where the hell are you?!")
        emb.set_image(url="https://cdn.discordapp.com/attachments/1393044025258545152/1395057116120612934/lv_0_20250713093411.gif?ex=687b09ef&is=6879b86f&hm=1b109984db7e57f1c0aa657da3af88141ebe17c5006ef262063f39a6012aa187&")
        await interaction.response.send_message(f"{interaction.user.mention} has lost {user.mention}", embed=emb)



# Rarity Testing
    @app_commands.command(name="search", description="Search for items")
    async def searchitems(self, interaction: discord.Interaction):
        choices = [
        {"name": "Sword", "rarity_value": 1},
        {"name": "Shield", "rarity_value": 3},
        {"name": "Helm", "rarity_value": 4},
        {"name": "Potion", "rarity_value": 2},
        {"name": "Potion", "rarity_value":1},
        {"name": "Scroll", "rarity_value":2},
        {"name": "Sword", "rarity_value":4},
        {"name": "Battleaxe", "rarity_value":5},
        {"name": "Beggars Mug", "rarity_value":0},
        {"name": "Bottle of Water", "rarity_value":0}

        ]
        rarity_map = {
            0: 'Scrap',
            1: 'Common',
            2: 'Uncommon',
            3: 'Rare',
            4: 'Legendary',
            5: 'Mystic',
        }
        weights = [75, 42, 0.3, 45, 70, 25, 5, 0.5, 75, 50]
        values = [1, 2, 3, 4, 5, 6]
        ranchoice = random.choice(values)
        # Get the rarity string from the map

        await interaction.response.defer(thinking=True)
        await asyncio.sleep(0)
        msg = await interaction.followup.send(f"Searching for items...")
        await asyncio.sleep(3)
        chosen_items = random.choices(choices, weights=weights, k=ranchoice)

        display_items = []
        for item in chosen_items:
            rarity_text = rarity_map.get(item["rarity_value"], "Unknown")
            display_items.append(f"**{rarity_text}**: {item["name"]}")

        # Sort the items based on their rarity_value (assuming 0 is lowest)
        # You'll need to re-fetch the rarity_value for sorting if you want to sort by value
        sorted_display_items = sorted(chosen_items, key=lambda x: x["rarity_value"])
        sorted_result_messages = []
        for item in sorted_display_items:
            rarity_text = rarity_map.get(item["rarity_value"], "Unknown")
            sorted_result_messages.append(f"**{rarity_text}**: {item["name"]}")


        emb=discord.Embed(title="Found:", description=f"{"\n".join(sorted_result_messages)}", color=discord.Color.green())
        await msg.delete()
        await interaction.followup.send(embed=emb)

# Go Fuck Yourself
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="gfy", description="Tells you to go fuck yourself")
    async def gfy(self, interaction: discord.Interaction, user: discord.User):
        variable_list = [
            'https://c.tenor.com/GbwILUMfIkIAAAAd/tenor.gif',
            'https://c.tenor.com/fTz7Bko5y20AAAAC/tenor.gif',
            'https://c.tenor.com/7wmF5O6ECl8AAAAC/tenor.gif',
            'https://media.tenor.com/N4DkLsYBKxkAAAAi/pixel-middle-finger.gif',
            'https://c.tenor.com/j6RBLGjuH44AAAAC/tenor.gif',
        ]
        emb = discord.Embed(title=f"", color=discord.Color.dark_gray())
        emb.add_field(name="", value=f"GO FUCK YOURSELF!")
        emb.set_image(url=f"{random.choice(variable_list)}")
        await interaction.response.send_message(f"{user.mention}", embed=emb)


async def setup(bot):
    await bot.add_cog(membinteract(bot))

