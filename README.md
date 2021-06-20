# Discord-Together-py

---

### Installation
`pip install git+https://github.com/Chrovo/Discord-Together-py`

---

### Example and Description

This package is discord-together for python. Here is an example of what the code should look like with this package:
```python
import discord
from Discord_Together.discordtogether import DiscordTogether
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.command()
async def yt(ctx, vc:commands.VoiceChannelConverter):
  youtube = DiscordTogether(token="token here")
  invite_code = await youtube.activity(ctx, option="youtube",vc_id=vc.id)
  await ctx.send(f"https://discord.com/invite/{invite_code}")

client.run("token here")
```
---

### Attributes

Token - This is your discord api token, place it there.

---

### Methods
`async activity`
- The above is a coroutine, this will return the invite code for whatever option you have chosen.

This method also takes in two arguments:
- option: The option you want(i.e. YouTube Together)
- vc_id: The voice channel id of where this activity will take place.

---

### Exceptions
This package has a total of 4 exceptions.

`InvalidTokenError`
- This exception is raised if you don't enter a valid token.

`InvalidOptionError`
- This exception is raised if you enter an invalid option in the "option" keyword argument for the activity method.

`InvalidVoiceChannelError`
- This exception is raised when you enter an invalid voice channel id for the "vc_id" keyword argument in the activity method.

`HTTPConnectionError`
- This exception is raised if the connection to the discord API was unsuccessful. It includes the status code as well as the status code description.(eg. 404:Not Found).
