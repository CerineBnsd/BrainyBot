import os
TOKEN = os.getenv("DISCORD_TOKEN")
# Can be multiple prefixes, like this: ("!", "?")
BOT_PREFIX = ("$")
OWNERS = [516805045199699969]
# Default cogs that I have created for the template
STARTUP_COGS = [
    "cogs.general", "cogs.help", "cogs.owner","cogs.mods",  "cogs.fun"
]
MODERATOR_ROLE ="mod"
APPLICATION_ID = "803040512314966037"


