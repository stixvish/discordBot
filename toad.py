# libraries for bot to access
import discord # discord bot
from discord.ext import commands # to use commands
import asyncio
import helper

# what is the purpose of this bot?
descript = \
    '''This bot is meant to display funny pictures of my friends
    as well as perform server management to an extent.'''

# make the bot subscribe to all actions that a bot in discord is able to do
intendedIntents = discord.Intents.all()
bot = commands.Bot(command_prefix='~', description=descript, intents=intendedIntents, case_insensitive=True)

# remove default help command
bot.remove_command('help')

# make the bot display certain information on bot startup
@bot.event
async def on_ready():

    # place the information needed into a file
    writer = open("text files\\identification.txt", "w")
    # show confirmation of login
    print("Logged in as {0.user}!".format(bot))

    # display names of servers and members in server
    for guild in bot.guilds:
        writer.write("Server: " + str(guild.name) + ", ID: " + str(guild.id) + "\n")
        for member in guild.members:
            writer.write("Member: " + str(member) + " (" + member.display_name + ") ," + str(member.id) + "\n")
        writer.write("\n")

    # display emojis that are available to the bot
    writer.write("Availiable Emojis:\n")
    for emoji in bot.emojis:
        writer.write("Emoji: " + str(emoji.name) + ", ID: " + str(emoji.id) + "\n")
    
    # close the writer
    writer.close()

    # set the status of the bot to make it so that people can see help command
    await bot.change_presence(activity=discord.Game(name="~help | hop on"))

# act when a message is sent
@bot.event
async def on_message(message):

    # create a more usable name for message text
    text = message.content

    log = open("text files\\" + str(message.guild) + " log.txt", "a")
    log.write(str(message.created_at) + "  -  " + str(message.channel) + "  -  " + str(message.author) + \
         " : " + str(message.content) + "\n")
    
    # does the message have embeds?
    numEmbeds = len(message.embeds)
    while numEmbeds > 0:

        # update counter
        numEmbeds = numEmbeds - 1

        # title empty?
        titleCon = message.embeds[numEmbeds].title
        if titleCon == discord.Embed.Empty:
            titleCon = "No Title" # placeholder text
        else:
            titleCon = str(message.embeds[numEmbeds].title) # whatever the actual title is

        # description empty?
        descriptionCon = message.embeds[numEmbeds].description
        if descriptionCon == discord.Embed.Empty:
            descriptionCon = "No Description" # placeholder text
        else:
            descriptionCon = str(message.embeds[numEmbeds].description) # whatever the actual description is

        log.write("-------\nEmbed Title:\n" + titleCon + \
            "\n-------\nEmbed Description:\n" + descriptionCon + "\n-------\n")
        
    # does the message have attachments?
    numAttachments = len(message.attachments)
    while numAttachments > 0:

        # update counter
        numAttachments = numAttachments - 1

        # log it
        log.write("Attachments: " + str(message.attachments[numAttachments].filename) + ", " \
            + str(message.attachments[numAttachments].url) + "\n")
        
    # close the writer
    log.close()

    # if someone says the n word, delete it if you can, otherwise correct them
    if "nigg" in text:
        try:
            await message.delete()
        except:
            await message.channel.send("*gentlemen of african american descent")
        return

    # if someone says poggers, react with x emoji
    if "pogger" in text:
        await message.add_reaction(bot.get_emoji(798705948281536552))

    # if someone says pog by itself, react with y emoji
    elif "pog" in text:
        await message.add_reaction(bot.get_emoji(798707878016974858))
    
    if "val" in text and message.author == 693255369505374258:
        await message.channel.send("bro nobody is tryna play with your sorry ass")

    # after this def, run commands
    await bot.process_commands(message)

# edits need to be reflected in the log
@bot.event
async def on_message_edit(before, after):

    # file to write onto
    log = open("text files\\" + str(before.guild) + " log.txt", "a")
    log.write("-----------------------\n")
    log.write(str(before.author) + " HAS EDITED THEIR MESSAGE\n")

    log.write("before: " + str(before.content) + "\n") # original message

    # does the before message have embeds?
    numEmbeds = len(before.embeds)
    while numEmbeds > 0:

        # update counter
        numEmbeds = numEmbeds - 1

        # title empty?
        titleCon = before.embeds[numEmbeds].title
        if titleCon == discord.Embed.Empty:
            titleCon = "No Title" # placeholder text
        else:
            titleCon = str(before.embeds[numEmbeds].title) # whatever the actual title is

        # description empty?
        descriptionCon = before.embeds[numEmbeds].description
        if descriptionCon == discord.Embed.Empty:
            descriptionCon = "No Description" # placeholder text
        else:
            descriptionCon = str(before.embeds[numEmbeds].description) # whatever the actual description is

        log.write("-------\nEmbed Title:\n" + titleCon + \
            "\n-------\nEmbed Description:\n" + descriptionCon + "\n-------\n")
        
    # does the message have attachments?
    numAttachments = len(before.attachments)
    while numAttachments > 0:

        # update counter
        numAttachments = numAttachments - 1

        # log it
        log.write("Attachments: " + str(before.attachments[numAttachments].filename) + ", " \
            + str(before.attachments[numAttachments].url) + "\n")

    log.write("after: " + str(after.content) + "\n") # edited message

    # does the message have embeds?
    numEmbeds = len(after.embeds)
    while numEmbeds > 0:

        # update counter
        numEmbeds = numEmbeds - 1

        # title empty?
        titleCon = after.embeds[numEmbeds].title
        if titleCon == discord.Embed.Empty:
            titleCon = "No Title" # placeholder text
        else:
            titleCon = str(after.embeds[numEmbeds].title) # whatever the actual title is

        # description empty?
        descriptionCon = after.embeds[numEmbeds].description
        if descriptionCon == discord.Embed.Empty:
            descriptionCon = "No Description" # placeholder text
        else:
            descriptionCon = str(after.embeds[numEmbeds].description) # whatever the actual description is

        log.write("-------\nEmbed Title:\n" + titleCon + \
            "\nEmbed Description:\n" + descriptionCon + "\n-------\n")
        
    # does the message have attachments?
    numAttachments = len(after.attachments)
    while numAttachments > 0:

        # update counter
        numAttachments = numAttachments - 1

        # log it
        log.write("Attachment: " + str(after.attachments[numAttachments].filename) + ", " \
            + str(after.attachments[numAttachments].url) + "\n")
    
    log.write("-----------------------\n")
    log.close()

@bot.event
async def on_message_delete(message):

    # file to write onto
    log = open("text files\\" + str(message.guild) + " log.txt", "a")
    log.write("-----------------------\n")
    log.write(str(message.author) + " HAS DELETED THEIR MESSAGE\n")

    log.write("message: " + str(message.content) + "\n") # original message

    # did the deleted message have embeds?
    numEmbeds = len(message.embeds)
    while numEmbeds > 0:

        # update counter
        numEmbeds = numEmbeds - 1

        # title empty?
        titleCon = message.embeds[numEmbeds].title
        if titleCon == discord.Embed.Empty:
            titleCon = "No Title" # placeholder text
        else:
            titleCon = str(message.embeds[numEmbeds].title) # whatever the actual title is

        # description empty?
        descriptionCon = message.embeds[numEmbeds].description
        if descriptionCon == discord.Embed.Empty:
            descriptionCon = "No Description" # placeholder text
        else:
            descriptionCon = str(message.embeds[numEmbeds].description) # whatever the actual description is

        log.write("-------\nEmbed Title:\n" + titleCon + \
            "\n-------\nEmbed Description:\n" + descriptionCon + "\n-------\n")
        
    # does the message have attachments?
    numAttachments = len(message.attachments)
    while numAttachments > 0:

        # update counter
        numAttachments = numAttachments - 1

        # log it
        log.write("Attachments: " + str(message.attachments[numAttachments].filename) + ", " \
            + str(message.attachments[numAttachments].url) + "\n")

    log.write("-----------------------\n")
    log.close()

@bot.command()
# this is a command that displays commands that users can make toad do
async def help(ctx):

    embedVar = discord.Embed(title='Commands for Toad-bot', \
        url = 'https://www.youtube.com/watch?v=boluNq5LSk0', \
        description = 'These are all the commands that the bot currently has.', \
        color = 0x000000)

    embedVar.add_field(name= "People Pictures", \
        value= ("Running the command ~pic [name] will display a bad picture of [name]."
                "\n\nCurrently supported:\n"
                "Rahul, Nav, Akshat\nStix, Giddu, Arivu\nRohan, Abel, Yehjin"), inline = False)

    embedVar.add_field(name="Poggers!", \
        value="If you say pog/poggers, the bot will react to your message.", inline=False)

    embedVar.add_field(name="Censorship", \
        value="We can't say bad words, that\'s not something an epic gamer would do. TW: B-word", inline=False)

    embedVar.add_field(name="Abel", \
        value="If Abel ever tries to play Valorant, the bot will verbally berate him.", inline=False)

    embedVar.add_field(name='Insults', \
        value="Toad will insult you! Use ~insult and then give the target's nickname to insult them.", inline=False)

    embedVar.set_footer(text="If you have any ideas, please say so. I'll try and add them!")

    await ctx.send(embed=embedVar)


@bot.command()
async def pics(ctx, name: str = None):
    # name has a value
    if name is not None:
        lname = name.lower()
        if lname == "rahul":
            await ctx.send(file=discord.File('pics\\damn.jpg'))
        elif lname == "nav" or lname == "naveen":
            await ctx.send(file=discord.File('pics\\cutie.jpg'))
        elif lname == "akshat":
            await ctx.send(file=discord.File('pics\\akshit.jpg'))
        elif lname == "stix" or lname == "vish":
            await ctx.send(file=discord.File('pics\\beard.jpg'))
        elif lname == "giddu":
            await ctx.send(file=discord.File('pics\\gidaddy.jpg'))
        elif lname == "arivu":
            await ctx.send(file=discord.File('pics\\vuvu.jpg'))
        elif lname == "rohan":
            await ctx.send(file=discord.File('pics\\lmaoro.jpg'))
        elif lname == "abel":
            await ctx.send(file=discord.File('pics\\babel.jpg'))
        elif lname == "yehjin":
            await ctx.send(file=discord.File('pics\\theYehj.jpg'))
        else:
            await ctx.send("i don't have a picture of " + lname)
    
    # name does not have a value
    else:
        await ctx.send("syntax for pics command -> ~pics [name]")

@bot.command()
async def insult(ctx, target: str = None):

    # create a map, key = display name, value = discord ID
    dictionaryNick = {}
    dictionaryGov = {}
    for member in ctx.message.author.guild.members:
        dictionaryNick[member.display_name.lower()] = member.id
        dictionaryGov[str(member)] = member.id

    # if there is no member listed in the initial call of the command
    if target is None:

        # send an initial message to ask for the name of the roast-ee
        await ctx.send("man ima roast someone give me their name")

        # check if the person sending the follow up message is the same person and in the same channel
        check = lambda m: m.author == ctx.author and m.channel == ctx.channel

        # recieve the followup message
        try:
            reply = await bot.wait_for("message", check=check, timeout=30)
        
        # user took too long to give the bot a reply
        except asyncio.TimeoutError:
            await ctx.send("cancelled request")
            return

        # special cases, if the response is people i care about
        # special case for vishesh
        if (reply.content.lower() == "vishesh" or reply.content.lower() == "vish") or reply.content.lower() == "stix":
            await ctx.send(f"<@{412718525019455490}> bruh why would you make this shitty ass bot you're kinda dumb asl for that")
            return
        # special case for naveen
        elif reply.content.lower() == "naveen" or reply.content.lower() == "nav":
            await ctx.send(f"<@{535977502875713546}> you really out here forgetting condoms lmao")
            return
        # special case for akshat
        elif reply.content.lower() == "akshat":
            await ctx.send(f"<@{693612064530235444}> you really went and learned how to handle guns bc you couldn\'t get them on your own")
            return
        # special case for arivu
        elif reply.content.lower() == "arivu" or reply.content.lower() == "vuvu":
            await ctx.send(f"<@{286617953963868161}> dawg why aren\'t you radiant yet")
            return
        # special case for rahul
        elif reply.content.lower() == "rahul" or reply.content.lower() == "luhar":
            await ctx.send(f"<@{356134637388562432}> imagine still being in high school rn")
            return

        # if the reply is someone in the dictionary
        if dictionaryNick.get(reply.content.lower()) != None:

            userID = dictionaryNick.get(reply.content.lower())
            await ctx.send(f"<@{userID}> im about to get on your ass")

            # start the roast session
            await ctx.send("you look like an egg")
            await ctx.send("you look like sid from the ice age movies")
            await ctx.send("you look like your mom's vagina")

        # didn't find the person that the user was looking for
        else:
            await ctx.send("i don't know who this person is")
    
    # the person was @-ed to insult
    elif target[:2] == "<@" and target[-1:] == ">":

        # @ the target and say insults
        await ctx.send(target + " im about to get on your ass")

        # start the roast session
        await ctx.send("you look like an egg")
        await ctx.send("you look like sid from the ice age movies")
        await ctx.send("you look like your mom's vagina")
    
    # random string entered
    else:

        # name special cases
        if target.lower() == "vishesh" or target.lower() == "stix":
            await ctx.send(f"<@{412718525019455490}> bruh why would you make this shitty ass bot you're kinda dumb asl for that")
            return
        
        elif target.lower() == "naveen" or target.lower() == "nav":
            await ctx.send(f"<@{535977502875713546}> you really out here forgetting condoms lmao")
            return
        
        elif target.lower() == "akshat":
            await ctx.send(f"<@{693612064530235444}> you really went and learned how to handle guns bc you couldn\'t get them on your own")
            return
        
        elif target.lower() == "arivu" or target.lower() == "vuvu":
            await ctx.send(f"<@{286617953963868161}> dawg why aren\'t you radiant yet")
            return
        
        elif target.lower() == "rahul" or target.lower() == "luhar":
            await ctx.send(f"<@{356134637388562432}> imagine still being in high school rn")
            return

        # string entered was the nickname of the target
        if dictionaryNick.get(target) != None:

            # get the userID of the nickname
            userID = dictionaryNick.get(target)
            await ctx.send(f"<@{userID}> im about to get on your ass")

            # start the roast session
            await ctx.send("you look like an egg")
            await ctx.send("you look like sid from the ice age movies")
            await ctx.send("you look like your mom's vagina")
        
        # string entered was government name of the target
        elif dictionaryGov.get(target) != None:

            # get the userID of the government name
            userID = dictionaryGov.get(target)
            await ctx.send(f"<@{userID}> im about to get on your ass")

            # start the roast session
            await ctx.send("you look like an egg")
            await ctx.send("you look like sid from the ice age movies")
            await ctx.send("you look like your mom's vagina")
        
        # string is not a nickname nor a government name
        else:
            await ctx.send("i don't know who this person is")        

config = helper.read_config()
bot.run(config['RunTime']['key'])