import datetime
TOKEN = "ODAzMDQwNTEyMzE0OTY2MDM3.YA3_wQ.5JNR9W7Mk8UBPR0Tsesf6lRWZRw"
# Can be multiple prefixes, like this: ("!", "?")
BOT_PREFIX = ("$")
OWNERS = [516805045199699969]
# Default cogs that I have created for the template
STARTUP_COGS = [
    "cogs.general", "cogs.help", "cogs.owner","cogs.mods", "cogs.hashcode"
]
MODERATOR_ROLE ="mod"
APPLICATION_ID = "803040512314966037"

# Invite command configs
CATEGORY_FOR_INVITATION = "hashcode" # can only be executed inside the **category** we have created

# A prefex to denote that a channel belongs to a team and not a public channel
TEAM_WORKSPACE_PREFIX = "team-"

############ HASHCODE PROPERTIES ###########
HASHCODE_LOGS_CHANNEL_ID = 791601343189483520
HASHCODE_CATEGORY_WORKSPACE_ID = 813213809455792169
HASHCODE_GENERAL_CHANNEL_ID = 791601343189483520
HASHCODE_CHECKIN_CHANNEL_ID = 791601343189483520


HASHCODE_START_DATE = datetime.datetime(2021, 2, 25, 18, 30, 0, 0)
HASHCODE_END_DATE = datetime.datetime(2021, 2, 25, 22, 30, 0, 0)
