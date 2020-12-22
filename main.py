import discord
import datetime
import asyncio
import random

import os
from discord.ext import commands

client = commands.Bot(command_prefix="t!")

@client.event
async def on_ready():
    print("Bot is Ready!")

@client.event
async def on_guild_join(guild):
    log_channel = client.get_channel(LOGGING CHANNEL ID)
    await log_channel.send(f"Joined - {guild.name}\nServer ID - {guild.id}\nOwner - {guild.owner}")

@client.event
async def on_guild_remove(guild):
    log_channel = client.get_channel(LOGGING CHANNEL ID)
    await log_channel.send(f"Left - {guild.name}\nServer ID - {guild.id}\nOwner - {guild.owner}")

#music command starts here
'''
@client.command()
async def play(ctx, url : str, channel):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")
@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")
@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")
@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    '''

#music command ends here
@client.command(aliases=['user','info'])
@commands.has_permissions(kick_members=True)
async def whois(ctx,member : discord.Member):
  embed = discord.Embed(title = member.name , description = member.mention , color = discord.Colour.green())
  embed.add_field(name = "ID", value = member.id , inline = True)
  embed.set_thumbnail(url = member.avatar_url)
  embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
  await ctx.send(embed=embed)
  
@client.command()
async def invite(ctx):
  await ctx.send("https://discord.com/api/oauth2/authorize?client_id=784460732502507560&permissions=8&scope=bot")

@client.command()
async def hello(ctx):
  await ctx.send("hi")

@client.command()
async def ping(ctx):
    ping = round(client.latency * 1000)
    await ctx.send(f'🏓Pong `{ping}ms`')

@client.command(name="support")
async def support(ctx):
    await ctx.send('[Support Server](https://discord.gg/XJNg4yRuU8)')

@client.command(name="owner")
async def owner(ctx):
    await ctx.send('https://discord.bio/p/neilop')

warn_count = {}

@client.command(name="serverinfo", aliases=['si'])
async def serverinfo(ctx):
    name = ctx.guild.name
    description = ctx.guild.description
    owner = ctx.guild.owner
    guild_id = ctx.guild.id
    region = ctx.guild.region
    member_count = ctx.guild.member_count
    icon = ctx.guild.icon_url

    embed = discord.Embed(
        title=f"{name} Server Information",
        description=description,
        color=discord.Colour.red()
        )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=guild_id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=member_count, inline=True)

    await ctx.send(embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(manage_channels = True)
async def announce(ctx, channel: discord.TextChannel,*,msg):
    await ctx.send(f'Message sended to {channel}')
    embed = discord.Embed(
    description = msg,
    colour= discord.Colour.red())
    await channel.send(embed=embed)

@client.command()
@commands.has_guild_permissions(manage_channels=True)
async def poll(ctx,*,msg):
    channel = ctx.channel
    try:
        op1, op2 = msg.split("or")
        txt = f"React with 👍🏼 {op1} or 👎🏼 {op2}"
    except:
        await channel.send("Correct Syntex: [Choice1] or [Choice2]")
        return
  
    embed = discord.Embed(title= "POLL", description=txt, color= discord.Colour.red())
    message_ = await channel.send(embed=embed)
    await message_.add_reaction("👍🏼")
    await message_.add_reaction("👎🏼")
    await ctx.message.delete()
'''
@client.command(name="slowmode", aliases=['sm'])
@commands.has_guild_permissions(manage_guild=True)
async def setdelay(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode in this channel to **{seconds}** seconds!")
'''

@client.command(pass_context = True)
async def helpme(ctx):
    author = ctx.message.author  

    embed = discord.Embed(
    title = f"Hello {author.name}" "\n" "Here are all Commands",
    description =  "**Member Commands**" "\n" "`help`, `hello`" "\n" "`ping`, `support`, `whois`," "\n" "`serverinfo`,`avatar`""\n"
    "**Music Commands(Development)**""\n""`play <url> <channel voice channel name>`""\n""`leave`,`pause`""\n""`resume`""\n"
    "**Mod Commands**" "\n" "`kick`, `ban`," "\n" "`unban`, `addrole`," "\n" "`removerole`, `mute`," "\n" "`unmute`, `clear`," "\n"
    "`warn`, `warncount`,`embed`" "\n"
    "**Management Commands**" "\n" "`lockchannel`, `unlockchannel`," "\n" "`say`,"  "\n" "`announce`, `poll`,",
    colour = discord.Colour.red()
    )
    await ctx.send(f"**Hello {ctx.author.mention} Check Your DM**", delete_after = 60)
    await author.send(embed=embed)

@client.command(name="lockchannel", aliases=['lock'])
@commands.has_guild_permissions(manage_guild=True)
async def lockchannel(ctx, channel: discord.TextChannel = None):
    if channel is None:
        channel = ctx.channel

    for role in ctx.guild.roles:
        if role.permissions.administrator:
            await channel.set_permissions(role, send_messages=True, read_messages=True)
        elif role.name == "@everyone":
            await channel.set_permissions(role, send_messages=False)

    await ctx.send(f"🔒The channel {channel.mention} has been locked")

@client.command(name="unlockchannel", aliases=['unlock'])
@commands.has_guild_permissions(manage_guild=True)
async def unlockchannel(ctx, channel: discord.TextChannel = None):
    if channel is None:
        channel = ctx.channel

    await channel.set_permissions(ctx.guild.roles[0], send_messages=True)

    await ctx.send(f"🔓The channel {channel.mention} has been unlocked")

@client.command(name="slowmode", aliases=['sm'])
@commands.has_guild_permissions(manage_guild=True)
async def setdelay(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode in this channel to **{seconds}** seconds!")

@client.command(name="avatar", aliases=['av'])
async def avatar(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author

    aembed = discord.Embed(
        color=discord.Colour.red(),
        title=f"{user}"
    )

    aembed.set_image(url=f"{user.avatar_url}")
    await ctx.send(embed=aembed)

@client.command(name="addrole",aliases=['ad'])
@commands.has_permissions(manage_roles = True)
async def addrole(ctx,role: discord.Role ,user: discord.Member):
    await user.add_roles(role)
    await ctx.send(f"Successfully Added {role.mention} to {user.mention}")

@client.command(name= "removerole",aliases=['rd'])
@commands.has_permissions(manage_roles = True)
async def removerole(ctx,role: discord.Role ,user: discord.Member):
    await user.remove_roles(role)
    await ctx.send(f"Successfully Removed {role.mention} to {user.mention}")

@client.command()
@commands.has_permissions(administrator=True)
async def say(ctx , *, msg):
    await ctx.message.delete() 
    await ctx.send("{}".format(msg))

@client.command(pass_context = True)
@commands.has_permissions(manage_channels = True)
async def embed(ctx, channel: discord.TextChannel,*,msg):
    await ctx.send(f'Message sent to {channel}')
    embed = discord.Embed(
    description = msg,
    colour= discord.Colour.green())
    await channel.send(embed=embed)

warn_count = {}

@client.command(name="warn")
@commands.has_guild_permissions(kick_members = True)
async def warn(ctx, user: discord.Member = None, *, reason=None):
    if user is None or reason is None:
        await ctx.send("Insufficient arguments.")
    elif ctx.author.top_role.position <= user.top_role.position and ctx.guild.owner.id != ctx.author.id:
        await ctx.send("You cannot warn this user because their role is higher than or equal to yours.")
    else:
        print(f"Warning user {user.name} for {reason}...")

        if str(user) not in warn_count:
            warn_count[str(user)] = 1
        else:
            warn_count[str(user)] += 1

        embed = discord.Embed(
            title=f"{user.name} has been warned", color=discord.Colour.red())
        embed.add_field(name="Reason", value=reason)
        embed.add_field(name="This user has been warned",
                        value=f"{warn_count[str(user)]} time(s)")

        await ctx.send(content=None, embed=embed)

@client.command(name="warncount")
async def warncount(ctx, user: discord.Member):
    if str(user) not in warn_count:
        warn_count[str(user)] = 0

        count = warn_count[str(user)]
        await ctx.send(f"{user.mention} has been warned {count} time(s)")

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount = 2):
  await ctx.channel.purge(limit= amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No reason provided"):
  #await member.send("you have been kicked from CODM Players Cafe Because "+reason)
  await member.kick(reason=reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No reason provided"):
  #await ctx.send(member.name+"you have been banned from "{guild.name} "Because "+reason)
  await member.ban(reason=reason)

@client.command(aliases=['ub'])
@commands.has_permissions(ban_members = True)
async def unban(ctx,*,member):
  banned_users = await ctx.guild.bans()
  member_name, member_disc = member.split('#')
  
  for banned_entry in banned_users:
   user = banned_entry.user

  if(user.name, user.discriminator)==(member_name,member_disc):
      await ctx.guild.unban(user)
      await ctx.send(member_name +" has been unbanned!")
      return
  await ctx.send(member+" was not found")

'''
@client.command(name="nuke")
@commands.has_guild_permissions(administrator=True)
async def nuke(ctx):
    temp_channel: discord.TextChannel = await ctx.channel.clone()
    await temp_channel.edit(position=ctx.channel.position)
    await ctx.channel.delete(reason="Nuke")
    embed = discord.Embed(color=discord.Colour.red(), description=f"{ctx.author.mention} Nuked This Channel!")
    embed.set_image(url="https://media.tenor.com/images/04dc5750f44e6d94c0a9f8eb8abf5421/tenor.gif")
    await temp_channel.send(embed=embed)
'''
@client.command()
@commands.has_permissions(manage_guild = True)
async def gstart(ctx, mins : int, * , prize: str):
    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60) 

    embed.add_field(name = "Ends At:", value = f"{end} UTC")
    embed.set_footer(text = f"Ends {mins} mintues from now!")

    my_msg = await ctx.send(embed = embed)


    await my_msg.add_reaction("🎉")


    await asyncio.sleep(mins*60)


    new_msg = await ctx.channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}!")

def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2


    return val * time_dict[unit]

@client.command()
@commands.has_permissions(manage_guild = True)
async def giveaway(ctx):
    await ctx.send("Let's start with this giveaway! Answer these questions within 15 seconds!")

    questions = ["Which channel should it be hosted in?", 
                "What should be the duration of the giveaway? (s|m|h|d)",
                "What is the prize of the giveaway?"]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel 

    for i in questions:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timheeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You didn\'t answer in time, please be quicker next time!')
            return
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time.")
        return

    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"You didn't answer the time with a proper unit. Use (s|m|h|d) next time!")
        return
    elif time == -2:
        await ctx.send(f"The time must be an integer. Please enter an integer next time")
        return            

    prize = answers[2]

    await ctx.send(f"The Giveaway will be in {channel.mention} and will last {answers[1]}!")


    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    embed.add_field(name = "Hosted by:", value = ctx.author.mention)

    embed.set_footer(text = f"Ends {answers[1]} from now!")

    my_msg = await channel.send(embed = embed)


    await my_msg.add_reaction(":tada:")


    await asyncio.sleep(time)


    new_msg = await channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! {winner.mention} won {prize}!")

@client.command()
@commands.has_permissions(manage_guild = True)
async def reroll(ctx, channel : discord.TextChannel, id_ : int):
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        await ctx.send("The id was entered incorrectly.")
        return
    
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! The new winner is {winner.mention}.!")

@client.command(name="mute")
@commands.has_guild_permissions(kick_members=True)
async def mute(ctx, user: discord.Member = None, time: str = None):
    if user is None:
        await ctx.send("Insufficient arguments.")
    elif ctx.author.top_role.position <= user.top_role.position and ctx.guild.owner.id != ctx.author.id:
        await ctx.send("You cannot mute this user because their role is higher than or equal to yours.")
    else:
        guild = ctx.guild
        mute_role = None

        for role in guild.roles:
            if role.name.lower() == "muted":
                mute_role = role
                break

        if mute_role in user.roles:
            await ctx.send("This user is already muted.")
        else:
            if not mute_role:
                await ctx.send("This server does not have a `Muted` Role. Creating one right now.")
                await ctx.send("This may take some time.")
                mute_role = await create_mute_role(guild)

            if time is None:
                await user.add_roles(mute_role)
                await ctx.send(f"User {user.mention} has been muted! They cannot speak.")
            else:
                time_unit = None
                parsed_time = None

                if "s" in time:
                    time_unit = "seconds"
                    parsed_time = time[0:(len(time) - 1)]
                elif "m" in time:
                    time_unit = "minutes"
                    parsed_time = time[0:(len(time) - 1)]
                elif "h" in time:
                    time_unit = "hours"
                    parsed_time = time[0:(len(time) - 1)]
                else:
                    time_unit = "minutes"  # default to minutes if user doesn't provide a time unit
                    parsed_time = time[0:len(time)]

                await user.add_roles(mute_role)
                await ctx.send(f"User {user.mention} has been muted for {parsed_time} {time_unit}! They cannot speak.")

                if time_unit == "seconds":
                    await asyncio.sleep(int(parsed_time))
                elif time_unit == "minutes":
                    await asyncio.sleep(int(parsed_time) * 60)
                elif time_unit == "hours":
                    await asyncio.sleep(int(parsed_time) * 3600)

                await user.remove_roles(mute_role)
                await ctx.send(f"User {user.mention} has been unmuted after {parsed_time} {time_unit}! They can speak now.")

@client.command(name="unmute")
@commands.has_guild_permissions(kick_members=True)
async def unmute(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send("Insufficient arguments.")
    elif ctx.author.top_role.position <= user.top_role.position and ctx.guild.owner.id != ctx.author.id:
        await ctx.send("You cannot unmute this user because their role is higher than or equal to yours.")
    else:
        guild = ctx.guild
        mute_role = None

        for role in guild.roles:
            if role.name.lower() == "muted":
                mute_role = role
                break

        if mute_role in user.roles:
            if not mute_role:
                mute_role = await create_mute_role(guild)

            await user.remove_roles(mute_role)
            await ctx.send(f"User {user.mention} has been unmuted! They can now speak.")

        else:
            await ctx.send("This user was never muted.")

#@client.command(aliases=['m'])
#@commands.has_permissions(kick_members = True)
#async def mute(ctx,member : discord.Member):
  #muted_role = ctx.guild.get_role(785448573868441628)

  #await member.add_roles(muted_role)
  #await ctx.send(member.mention+" has been muted")

#@client.command(aliases=['um'])
#@commands.has_permissions(kick_members = True)
#async def unmute(ctx,member : discord.Member):
  #muted_role = ctx.guild.get_role(785448573868441628)

  #await member.remove_roles(muted_role)
  #await ctx.send(member.mention+" has been unmuted")

@client.event
async def on_ready():

  await client.change_presence(activity=discord.Game(name=f"t!helpme"))

#@client.command(aliases=['user','info'])
#@command.has_permissions(kick_members=True)
#async def whois (ctx, member : discord.Member):

client.run("TOKEN HERE")




















































