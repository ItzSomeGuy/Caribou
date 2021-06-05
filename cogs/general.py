import discord
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ban(self, ctx):
        await ctx.message.delete()

        target = ctx.message.mentions[0]
        await ctx.guild.ban(target, delete_message_days=0)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("👋 hello!")

    @commands.command(pass_context=True)
    async def help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour=discord.Colour.blurple()
        )

        embed.set_author(name="Help")

        # embed.add_field(name="", value="", inline=False)
        # embed.add_field(name="8ball [question]", value="does some spooky shit", inline=False)
        embed.add_field(name="ban [member]", value="beans someone", inline=False)
        embed.add_field(name="hello", value="used as a greeting or to begin a telephone conversation", inline=False)
        embed.add_field(name="help", value="this..", inline=False)
        # embed.add_field(name="insult [member]", value="use it to help win arguments", inline=False)
        embed.add_field(name="rename [member] [nickname]", value="use to rename a member", inline=False)
        embed.add_field(name="stalk [member]", value="fetches avatar of someone", inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def rename(self, ctx):
        await ctx.message.delete()

        target = ctx.message.mentions[0]

    @commands.command()
    async def stalk(self, ctx, target):
        await ctx.message.delete()

        pfp = None
        members = ctx.guild.fetch_members()

        async for m in ctx.guild.fetch_members():
            if m.name == target:
                pfp = m.avatar_url

        if pfp is not None:
            await ctx.message.author.send(pfp)


def setup(client):
    client.add_cog(General(client))
