#Import all libraries
import discord
import aiohttp
import asyncio
from discord.ext import commands
from exceptions import InvalidTokenError, InvalidOptionError, InvalidVoiceChannelError, HTTPConnectionError

#Create the class
class DiscordTogether:
    def __init__(self,*, token:int):
        self.token = token
        self.conversions = {
            "youtube":"755600276941176913", #Credit goes to RemyK888 for all of these ids, thanks.
            'poker''755827207812677713',
            'betrayal':'773336526917861400',
            'fishing':'814288819477020702',
            'chess':'832012586023256104'
        }
        self.options = ["youtube", "poker", "betrayal","fishing","chess"]

    async def activity(self, *,option:str, vc_id:int):
        try:
            random_var=commands.VoiceChannelConverter(vc_id)
        except commands.ChannelNotFound:
            raise InvalidVoiceChannelError("Invalid voice channel id provided")
        if option.lower() in self.options:
            opt_id = self.conversions[option]
            async with aiohttp.ClientSession() as cs:
                try:
                    async with cs.post(f"https://discord.com/api/v8/channels/{vc_id}/invites", json={
                        "max_age":86400,
                        "max_uses":0,
                        "target_application_id":opt_id,
                        "target_type":2,
                        "temporary":False,
                        "validate":None
                  }, headers = {
                    "Authorization":f"Bot {self.token}",
                    "Content-Type":"application/json"
                  }) as r:
                        if r.status in range(200,300):
                            data = await r.json()
                            invitecode = data['code']
                            return invitecode
                        else:
                            raise HTTPConnectionError(f"Connection was unsuccessful: {r.status}:{r.reason}")
                except:
                    raise InvalidTokenError("Invalid token was provided")
        else:
            raise InvalidOptionError(f"Invalid option '{self.option}' provided")
