# Discord-Together.py

This package is discord-together for python. Here is an example of what the code should look like with this package:
```python
import discord
from discord.ext import commands
#Import this package
client = commands.Bot(command_prefix = "!")

@client.command()
async def yt(ctx, vc:commands.VoiceChannelConverter):
  youtube = DiscordTogether(token="token here")
  invite_code = await youtube.activity(option="youtube",vc_id=vc.id)
  await ctx.send(f"https://discord.com/invite/{invite_code}")
```
###Attributes
Token - This is your discord api token, place it there.
###Methods
`async activity`
The above is a coroutine, this will return the invite code for whatever option you have chosen.

This method also takes in two arguments:
1.) option: The option you want(i.e. YouTube Together)
2.) vc_id: The voice channel id of where this activity will take place.
