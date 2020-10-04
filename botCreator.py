

def addImportOptions(f):
    f.write(
        "import os\n"+
        "import discord\n"+
        "from dotenv import load_dotenv\n"+
        "from discord.ext import commands\n"+
        "from discord.ext.commands import has_role\n"+
        "from discord import Member\n"+
        "from discord.utils import get\n"+
        "import random\n"
    )

def addDict(f):
    x=[
        "kry={}\n",
        "f=open('Botresponses','r')\n",
        "for x in f:\n",
        "\ty=x.split(':::')\n",
        "\tkry[y[0].lower()]=y[1]\n"
    ]
    f.writelines(x)

def addLoad(f):
    f.write(
        "\nload_dotenv()\n"+
        "TOKEN = os.getenv(\'DISCORD_TOKEN\')\n"+
        "GUILD = os.getenv(\'DISCORD_GUILD\')\n"
    )

def addVariables(f):
    x=[
        '\nglobal g\n'
    ]
    f.writelines(x)

def addMakeClient(f):
    f.write(
        "\nclient = discord.Client()\n"
    )

def addConnectUsingClient(f):
    f.write(
        "\n@client.event\n"+
        "async def on_ready():\n"+
        "\tprint(f\'{client.user} has connected to discord!\')\n"
        "\tfor guild in client.guilds:\n"+
        "\t\t if guild.name == GUILD:\n"+
        "\t\t\t break\n"+
        "\tglobal g\n"+
        "\tg=guild\n"+
        "\tprint(\n"+
        "\t\tf\'{client.user} is connected to the following guild: \\n\'\n"+
        "\t\tf\'{guild.name}(id: {guild.id})\'\n"+
        "\t)\n"
    )

def addListOfMembers(f):
    x=[
        "\ndef listOfMembers():\n",
        "\tglobal g\n",
        "\tmembers=\'\\n - \'.join([member.name for member in g.members])\n",
        "\tprint(f\'Guild Members: \\n - {members}\')\n"
    ]
    f.writelines(x)

def addMemberWelcome(f,welcome_note):
    x=[
        "\n@client.event\n",
        "async def on_member_join(member):\n",
        "\tawait member.create_dm()\n",
        "\tawait member.dm_channel.send(\n",
        "\t\tf\'Hi {member.name},\\n"+welcome_note+"\'\n\t)\n"
    ]
    f.writelines(x)

def addMessageReaction(f,message_dict):
    x=[
        '\n@client.event\n',
        'async def on_message(message):\n',
        '\tif message.author==client.user:\n',
        '\t\treturn\n',
        '\tif message.content.lower() in '+message_dict+'.keys():\n',
        '\t\tresponse='+message_dict+'[message.content.lower()]\n',
        '\t\tawait message.channel.send(response)\n',
        '\telif message.content==\'raise-exception\':\n',
        '\t\traise discord.DiscordException\n'
    ]
    f.writelines(x)

def addMessageReaction2(f):
    x=[
        '\n@client.event\n',
        'async def on_message2(message):\n',
        '\tif message.author==client.user:\n',
        '\t\treturn\n',
        "\ty=open('scraped-hate-speech-data','r')\n",
        '\tfor d in y:\n',
        "\t\tif d in message.content.lower():\n"
        "\t\t\tresponse='That kind of behaviour will not be tolerated\\nBetter control yourself or get out'\n"
        "\t\t\tawait message.channel.send(response)\n"
        "\t\telif messege.content=='raise-exception':\n"
        "\t\t\traise discord.DiscordException\n"
    ]
    f.writelines(x)

def addExceptionHandling(f):
    x=[
        '\n@client.event\n',
        'async def on_error(event, *args, **kwargs):\n',
        '\twith open(\'err.log\',\'a\') as g:\n',
        '\t\tif event==\'on_message\':\n',
        '\t\t\tg.write(f\'Unhandled message: {args[0]}\\n\')\n',
        '\t\telse:\n',
        '\t\t\traise\n'
    ]
    f.writelines(x)

def addClientRun(f):
    x=[
        '\nclient.run(TOKEN)\n'
    ]
    f.writelines(x)