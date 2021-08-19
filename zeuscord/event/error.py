from . import core
from . import config

import discord

from discord.ext import commands

async def on_error(ctx, error):
    LANG = config.load()['lang']
    PREFIX = config.load()['prefix']

    # error: 'error message'
    error_messages = {
        commands.ExtensionError: 'Es gab ein Problem in einer Erweiterung ("cog").',
        commands.CheckFailure: 'Es gab ein Problem mit der Überprüfung, ob etwas ausgeführt werden soll.',
        commands.UserInputError: 'Überprüfe bitte deine Eingabe.',
        commands.CommandNotFound: f'Befehl nicht gefunden. Benutze **`{PREFIX}help`** für eine Befehlsliste.',
        # the f-string generates the help-command for the command
        commands.MissingRequiredArgument: f'Du hast ein Befehlsargument vergessen, benutze **`{PREFIX}help {ctx.message.content.replace(PREFIX, "").split()[0]}`** für Hilfe.',
        # the f-string generates the help-command for the command
        commands.TooManyArguments: f'Du hast zu viele Argumente eingegeben, benutze **`{PREFIX}help {ctx.message.content.replace(PREFIX, "").split()[0]}`** für Hilfe.',
        commands.Cooldown: 'Bitte warte, du kannst diesen Befehl erst später ausführen.',
        # commands.MessageNotFound: 'This message could not be found.',
        # commands.ChannelNotFound: 'This channel could not be found.',
        commands.NoPrivateMessage: 'Dies Funktioniert nicht in DM-Kanälen.',
        commands.MissingPermissions: 'Du brauchst leider folgende Berechtigung(en), um das zu tun:',
        commands.BotMissingPermissions: 'Ich brauche folgende Berechtigung(en), um das zu tun:',
        # the f-string generates the help-command for the command
        commands.BadArgument: f'Es gab ein Problem mit dem Konvertieren der Argumente, benutze den folgenden Befehl für Hilfe: **`{PREFIX}help {ctx.message.content.replace(PREFIX, "").split()[0]}`**',
    }

    error_msg = 'Unbekannter Fehler.'

    # create the error message using the dict above
    for e in error_messages.keys():
        if isinstance(error, e):
            error_msg = error_messages[e]

    # other errors:
    # - too long
    if 'Invalid Form Body' in str(error): error_msg = 'Ich kann leider nicht die Nachricht senden, weil sie zu lang gewesen wäre.'

    # - bug
    if 'Command raised an exception' in str(error): error_msg = 'Huch, es gab ein Problem mit dem Code.'

    # add detailed info
    if isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions):
        error_msg += f'\n**`{", ".join(error.missing_perms)}`**\n'

    # add full error description formatted as a code text
    error_msg += '\n\n**Konsole:**\n```\n' + str(error) + '\n```'

    # create a cool embed
    embed = discord.Embed(
        title='Command Error',
        description=error_msg,
        color=0xFF0000
    )

    # send it
    await ctx.send(embed=embed)
    if TESTING_MODE or error_msg == 'Unbekannter Fehler.': raise error  # if this is a testing system, show the full error in the console

