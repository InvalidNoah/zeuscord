import 
from cogs.helpers import config

import os
import dotenv
import socket
import discord

from discord.ext import commands

dotenv.load_dotenv()  # initialize virtual environment

COLOR = config.load()['design']['colors']['primary']  # primary color for embeds
TESTING_MODE = socket.gethostname() in config.load()['bot']['testing_device_names']  # testing systems
PREFIX = config.load()['bot']['prefix']  # command prefix

for temp_file in os.listdir('temp/'):
    os.remove('temp/' + temp_file)

# create bot, help_command is none because it's a custom one
client = commands.Bot(
    command_prefix=commands.when_mentioned_or(PREFIX), help_command=None, intents=discord.Intents.all())

@client.event
async def on_ready():
    print('ONLINE as', client.user)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='LH\'s videos!'))

@client.event
async def on_command_error(ctx, error):

@client.command(aliases=['command', 'commands', 'help'], help='📃Listet entweder alle Befehle auf oder zeigt Info über einen bestimmten Befehl an.', usage='(<command name>)')
async def commandinfo(ctx, name=None):
    if name:
        for c in client.commands:
            if name.lower() == c.name or name.lower() in list(c.aliases):
                text = f'''
        **Information:** {c.help if c.help else ' - '}
        **Argumente:** {c.usage if c.usage else ' - '}
        **Aliasse:** {', '.join(c.aliases) if c.aliases else ' - '}
        '''
                embed = discord.Embed(
                    title='Command ' + c.name, color=COLOR, description=text)
                await ctx.send(embed=embed)
                return

        embed = discord.Embed(title='Command not found', color=COLOR,
                              description='This command does not exist...')
        await ctx.send(embed=embed)
        return

    def sortkey(x):
        return x.name

    categories = {
        '⚙️': 'Hauptsystem',
        '📃': 'Info',
        '🔧': 'Tools',
        '🔒': 'Admin-Tools',
        '🎮': 'Spiel & Spaß',
        '🔩': 'Andere'}

    # ok, somehow I managed to get this to work, don't ask me how, but it WORKS
    text = ''
    for category in categories.keys():
        text += f'\n{category} **{categories[category]}**\n'
        for command in sorted(client.commands, key=sortkey):
            if command.help.startswith(category):
                if command.aliases:
                    text += f'{command.name} *({"/".join(command.aliases)})*\n'
                else:
                    text += f'{command.name}\n'
                continue
            
    embed = discord.Embed(title='Befehle', color=COLOR, description=text)
    embed.set_footer(
        text=f'Benutze {PREFIX}help <command> für mehr Info über einen bestimmten Befehl.')
    await ctx.send(embed=embed)

# load cogs
# credit: https://youtu.be/vQw8cFfZPx0
for filename in os.listdir(os.getcwd() + '/src/cogs/'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('DISCORD_TOKEN'))  # run bot with the token set in the .env file
