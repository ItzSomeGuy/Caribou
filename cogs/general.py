import random
import discord
from discord.ext import commands

a_punishments = []



class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel and before.channel.category is None and before.channel.members == []:
            for p in a_punishments:
                if p.id == before.channel.id:
                    await before.channel.delete()
                    a_punishments.remove(p)

    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful."]

        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

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
        embed.add_field(name="8ball [question]", value="does some spooky shit", inline=False)
        embed.add_field(name="ban [member]", value="beans someone", inline=False)
        embed.add_field(name="hello", value="used as a greeting or to begin a telephone conversation", inline=False)
        embed.add_field(name="help", value="this..", inline=False)
        embed.add_field(name="music", value="shows all music related commands", inline=False)
        embed.add_field(name="punish [member]", value="punishes a user that you see fit", inline=False)
        embed.add_field(name="rename [member] [nickname]", value="use to rename a member", inline=False)
        embed.add_field(name="stalk [member]", value="fetches avatar of someone", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def music(self, ctx):

        author = ctx.message.author

        embed = discord.Embed(
            colour=discord.Colour.blurple()
        )

        embed.set_author(name="Music")

        embed.add_field(name="play", value="usage: ~play [youtube link here without brackets]. This plays audio from any youtube link", inline=False)
        embed.add_field(name="pause", value="pauses any currently playing audio", inline=False)
        embed.add_field(name="resume", value="resumes any paused audio", inline=False)
        embed.add_field(name="skip", value="skips currently playing audio", inline=False)
        embed.add_field(name="stop", value="stops all audio", inline=False)
        await ctx.send(embed=embed)
    @commands.command()
    async def punish(self, ctx):
        if ctx.message.mentions[0].voice:
            names = ['Auschwitz', 'Literal Hell', 'The Void',
                     'The Shadow Realm', 'The Firing Squad',
                     'Guantanamo Bay', '6 Feet Under',
                     'The Gulag', 'Back to Canada',
                     'The Crucifixion Cross', 'The Midnight Facility']
            channel = await ctx.guild.create_voice_channel(random.choice(names))
            a_punishments.append(channel)

            target = ctx.message.mentions[0]
            await target.move_to(channel)



    @commands.command()
    async def rename(self, ctx, target, *args):
        await ctx.message.delete()

        target = ctx.message.mentions[0]

        new_name = ""

        if args is not None:
            new_name = " ".join(args[:])

        await target.edit(nick=new_name)
        print(f"renamed {target.name} to {new_name}")

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
