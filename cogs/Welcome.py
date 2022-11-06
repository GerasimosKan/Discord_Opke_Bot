from GlobalVar import Role, Channel
import discord
import asyncio
from PIL import Image
from io import BytesIO
from turtle import stamp
from PIL import ImageFont
from PIL import ImageDraw
from discord.utils import *
from discord.ext import commands
from discord.ext.commands import Bot


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):

        guild = member.guild
        channel = self.bot.get_channel(Channel)
        role = discord.utils.get(member.guild.roles, id=Role)

        img = Image.open('/images/id.jpg')  # image
        asset = member.avatar_url_as(size=512)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((178, 180))  # border size
        img.paste(pfp, (119, 63))  # image paste location

        img.save("MyID.jpg")
        # End of image processing

        await channel.send(f"Welcome, {member.mention}, Η καινούργια σου ταυτότητα!\n", file=discord.File("MyID.jpg"))
        await member.add_roles(role)


async def setup(bot):
    await bot.add_cog(Welcome(bot))
