# --- Startup Stuff ----------------
from subprocess import run as runcmd

try:
    import discord
except ImportError:
    print("discord.py not found, downloading using pip")
    runcmd("python -m pip install -U discord.py")
    import discord
try:
    from yaml import load, dump
except ImportError:
    print("PyYAML not found, downloading using pip")
    runcmd("python -m pip install -U PyYaml")
    from yaml import load, dump

with open("cogs/config.txt", 'r') as file:
    config = load(file)
if config["First_Time"]:
    print("I see this is your first time!\r\nLet's take a minute to set some things up")
    token = input("Enter your Bot's token that you get from applying at 'https://discordapp.com/developers/applications/me':\r\n")
    with open("cogs/config.txt", 'w') as file:
        file.write(dump({
            "First_Time": False,
            "Token": token
        }))
else:
    token = config["Token"]

# ------------------------------------
print("ParrotBot v1.0")
client = discord.Client()
data = {}

@client.event
async def on_ready():
    global client, data
    with open("cogs/commands.txt") as file:
        data = load(file)
    print("Ready!")
    print("All available commands:")
    keys = list(data.keys())
    values = list(data.values())
    for i in range(len(keys)):
        print(keys[i], " - ", values[i])

@client.event
async def on_message(message):
    try:
        msg = message.content.lower()
        output = data[msg]
        await client.send_message(message.channel, output)
    except KeyError:
        pass

client.run(token)
