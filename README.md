# Discord-Together-py

---

### Installation
`pip install git+https://github.com/Chrovo/Discord-Together-py`

---

### Example and Description

This package is discord-together for python. Here is an example of what the code should look like with this package:
```python
import discord
from discord.ext import commands
from Discord_Together.discordtogether import DiscordTogether # This will import this package.

bot = commands.Bot(command_prefix = '!')

# These next lines are creating a command which uses this library.
@bot.command()
async def yt(ctx: commands.Context, vc: commands.VoiceChannelConverter):
  youtube = DiscordTogether(token='token here') # Create a DiscordTogether object.
  invite_code = await youtube.activity(option='youtube',vc_id=vc.id) # This will return the invite code for YouTube Together for the channel the user has entered.
  await ctx.send(f'https://discord.com/invite/{invite_code}') # This will send the link for the activity in the channel the command was invoked under.

bot.run('token here')
```
---

### Attributes

token - This is your discord api token, place it there.

session - This is your `aiohttp.ClientSession` instance if you have one, if not provided, it will be created for you. This parameter is optional.

---

### Methods
`async activity`
- The above is a coroutine, this will return the invite code for whatever option you have chosen.

This method also takes in two required keyword arguments:
- option: The string of the option you want(eg. YouTube Together). Valid options are "youtube", "betrayal", "chess", "fishing", and "poker".
- vc_id: The voice channel id of where this activity will take place. This is an integer.

---

### Exceptions
This package has a total of 4 exceptions.

`InvalidTokenError`
- This exception is raised if you don't enter a valid token for the "token" keyword argument.

`InvalidOptionError`
- This exception is raised if you enter an invalid option in the "option" keyword argument for the activity method.

`InvalidVoiceChannelError`
- This exception is raised when you enter an invalid voice channel id for the "vc_id" keyword argument in the activity method.

`HTTPConnectionError`
- This exception is raised if the connection to the discord API was unsuccessful. It includes the status code as well as the status code description.(eg. 404:Not Found).
