import discord
from discord.ext import commands
from discord import app_commands
import logging
from discord import colour
import asyncio
import datetime
from discord.webhook.async_ import interaction_response_params


class admincmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin Commands Cog has been loaded!')


# Timeout Command
    @app_commands.command(name="timeout", description="Timeout jail")
    @discord.app_commands.checks.has_permissions(moderate_members=True)
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.allowed_contexts(guilds=True, dms=False, private_channels=False)
    async def timeout(self, interaction: discord.Interaction, member: discord.Member, seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0, reason: str=None):
        duration = datetime.timedelta(seconds=seconds, minutes=minutes, hours= hours, days=days)
        await member.timeout(duration, reason=reason)
        embed = discord.Embed(title="Timed Out!", description=f"{member.mention} was timed out!", color=discord.Color.dark_red())
        embed.add_field(name="Duration", value=f"{duration}", inline=False)
        embed.add_field(name="Reason", value=f"{reason}", inline=False)
        embed.set_footer(text=f"Timed out by {interaction.user.name}")

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="kick", description="Kick a member")
    @discord.app_commands.checks.has_permissions(kick_members=True)
    @app_commands.allowed_installs(guilds=True, users=False)
    async def kickmember(self, interaction: discord.Interaction, member: discord.Member, reason: str=None):
        await member.kick(reason=reason)
        embed=discord.Embed(name="Kicked member:", description=f"{member.mention} was kicked!", color=discord.Color.dark_red())
        embed.add_field(name="Reason", value=f"{reason}", inline=False)
        embed.set_footer(text=f"Kicked by {interaction.user.name}")
        await interaction.response.send_message(embed=embed)




# Announcement Command
    @app_commands.command(name="psa", description="Make a Public Service Announcement")
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.allowed_contexts(guilds=True, dms=False, private_channels=False)
    @discord.app_commands.checks.has_permissions(manage_messages=True)
    async def psa(self, interaction: discord.Interaction, channel: discord.TextChannel, line1: str, role: discord.Role=None, line2: str=None, line3: str=None):
        if role is None:
            if line2 is None and line3 is None:
                embed = discord.Embed(title=f"", color=discord.Color.blurple())
                embed.set_author(name=f"{interaction.user.display_name} has an announcement!", icon_url=f"{interaction.user.avatar}")
                embed.add_field(name="Announcement:", value=f"{line1}", inline=False)
                await channel.send(f"{role.mention}", embed=embed)
                await interaction.response.send_message(f"Announcement has been sent to {channel.mention}!")
            if line2 is not None and line3 is None:
                embed = discord.Embed(title=f"", color=discord.Color.blurple())
                embed.set_author(name=f"{interaction.user.display_name} has an announcement!", icon_url=f"{interaction.user.avatar}")
                embed.add_field(name="Announcement:", value=f"{line1}\n{line2}", inline=False)
                await channel.send(f"{role.mention}", embed=embed)
                await interaction.response.send_message(f"Announcement has been sent to {channel.mention}!")
            if line2 is not None and line3 is not None:
                embed = discord.Embed(title=f"", color=discord.Color.blurple())
                embed.set_author(name=f"{interaction.user.display_name} has an announcement!", icon_url=f"{interaction.user.avatar}")
                embed.add_field(name="Announcement:", value=f"{line1}\n{line2}\n{line3}", inline=False)
                await channel.send(f"{role.mention}", embed=embed)
                await interaction.response.send_message(f"Announcement has been sent to {channel.mention}!")
            if line2 is None and line3 is not None:
                embed = discord.Embed(title=f"", color=discord.Color.blurple())
                embed.set_author(name=f"{interaction.user.display_name} has an announcement!", icon_url=f"{interaction.user.avatar}")
                embed.add_field(name="Announcement:", value=f"{line1}\n{line3}", inline=False)
                await channel.send(f"{role.mention}", embed=embed)
                await interaction.response.send_message(f"Announcement has been sent to {channel.mention}!")

        if role is not None:
            if line2 is None and line3 is None:
                embed = discord.Embed(title=f"", color=discord.Color.blurple())
                embed.set_author(name=f"{interaction.user.display_name} has an announcement!", icon_url=f"{interaction.user.avatar}")
                embed.add_field(name="Announcement:", value=f"{line1}", inline=False)
                await channel.send(f"{role.mention}", embed=embed)
                await interaction.response.send_message(f"Announcement has been sent to {channel.mention}!")
            if line2 is not None and line3 is None:
                embed = discord.Embed(title=f"", color=discord.Color.blurple())
                embed.set_author(name=f"{interaction.user.display_name} has an announcement!", icon_url=f"{interaction.user.avatar}")
                embed.add_field(name="Announcement:", value=f"{line1}\n{line2}", inline=False)
                await channel.send(f"{role.mention}", embed=embed)
                await interaction.response.send_message(f"Announcement has been sent to {channel.mention}!")
            if line2 is not None and line3 is not None:
                embed = discord.Embed(title=f"", color=discord.Color.blurple())
                embed.set_author(name=f"{interaction.user.display_name} has an announcement!", icon_url=f"{interaction.user.avatar}")
                embed.add_field(name="Announcement:", value=f"{line1}\n{line2}\n{line3}", inline=False)
                await channel.send(f"{role.mention}", embed=embed)
                await interaction.response.send_message(f"Announcement has been sent to {channel.mention}!")
            if line2 is None and line3 is not None:
                embed = discord.Embed(title=f"", color=discord.Color.blurple())
                embed.set_author(name=f"{interaction.user.display_name} has an announcement!", icon_url=f"{interaction.user.avatar}")
                embed.add_field(name="Announcement:", value=f"{line1}\n{line3}", inline=False)
                await channel.send(f"{role.mention}", embed=embed)
                await interaction.response.send_message(f"Announcement has been sent to {channel.mention}!")


# Add Role Command
    @app_commands.command(name="addrole",description="Adds a role to a member")
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.allowed_contexts(guilds=True, dms=False, private_channels=False)
    @discord.app_commands.checks.has_permissions(manage_roles=True)
    async def addrole(self, interaction: discord.Interaction, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await interaction.response.send_message(f"{member.mention} has been given {role.mention} by {interaction.user.mention}")

# Remove Role Command
    @app_commands.command(name="removerole", description="Remove a role from a member")
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.allowed_contexts(guilds=True, dms=False, private_channels=False)
    @discord.app_commands.checks.has_permissions(manage_roles=True)
    async def addrole(self, interaction: discord.Interaction, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)
        await interaction.response.send_message(f"{member.mention} has had {role.mention} removed by {interaction.user.mention}")

# UserID Grab Command
#@app_commands.command(name="userid", description="Gets the mentioned users UserID")
#@discord.app_commands.checks.has_role("Staff")
#async def get_userid(interaction: discord.Interaction, user: discord.User):
#    await interaction.response.send_message(f"{user.id}")

# Embed Test Command
#@app_commands.command(name="embed_test", description="Tests the bot embed capabilities")
#async def embed_test(interaction: discord.Interaction):
#    emb = discord.Embed(title="Testing Bot Embed Capabilities")
#    emb.set_author(name="MelBot")
#    await interaction.response.send_message(embed=emb, ephemeral=True)

# Get Roles V1
#@app_commands.command(name="get_roles", description="Gets a list of the users roles")
#async def get_user_roles(interaction: discord.Interaction, user: discord.User):
#    await interaction.response.send_message(f"{user.mention} has the roles {user.roles}")

    # Get Info (Get Roles V2)
    @app_commands.command(name="userinfo", description="Gets a list of information about a member")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def userinfo(self, interaction: discord.Interaction, member: discord.User):
        joined_at = member.joined_at.strftime("%b %d, %Y, %T")
        created_at = member.created_at.strftime("%b %d, %Y, %T")
        roles = member.roles
        role_names = ' '.join([role.mention for role in roles if role.name != '@everyone'])
        emb = discord.Embed(title=f"", color=discord.Color.yellow())
        emb.add_field(name=f"Member display name:", value=f"{member.display_name}", inline=False)
        emb.add_field(name=f"Member username:", value=f"{member.name}", inline=False)
        emb.add_field(name=f"User ID:", value=f"{member.id}", inline=False)
        emb.add_field(name=f"Joined the server on:", value=f"{joined_at}", inline=False)
        emb.add_field(name=f"Created account on:", value=f"{created_at}", inline=False)
        emb.add_field(name=f"Current roles:", value=f"{role_names}", inline=False)
        emb.set_author(name=f"Requested info for {member.display_name}", icon_url=f"{member.avatar}")
        emb.set_thumbnail(url=f"{member.avatar}")
        await interaction.response.send_message(embed=emb)

    # Walkie System V1
    #@app_commands.command(name="walkie", description="Current Walkie System.")
    #@discord.app_commands.checks.has_role("Staff")
    #async def walkie(interaction: discord.Interaction, role: discord.Role, message: str):
    #    if discord.app_commands.checks.has_role("Staff"):
    #        await interaction.response.send_message(f"{role.mention} paged by {interaction.user.name} Reason: {message}")


    # Walkie System V2
    @app_commands.command(name="walkie", description="Current Walkie System")
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.allowed_contexts(guilds=True, dms=False, private_channels=False)
    @discord.app_commands.checks.has_permissions(moderate_members=True)
    async def walkie(self, interaction: discord.Interaction, team: discord.Role, reason: str, user: discord.User):
        if discord.app_commands.checks.has_role("Staff"):
            emb = discord.Embed(title=f"{reason}", color=discord.Color.blurple())
            emb.set_author(name=f"Requested by {interaction.user.name}")
            emb.add_field(name=f"{team.mention}", value=f"{user.mention}")
            emb.set_thumbnail(url=user.avatar)
            await interaction.response.send_message(f"{team.mention}", embed=emb)

async def setup(bot):
    await bot.add_cog(admincmds(bot))