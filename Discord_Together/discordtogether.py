import asyncio

import aiohttp
import discord
from discord.ext import commands

from .exceptions import (
    InvalidTokenError,
    InvalidOptionError,
    InvalidVoiceChannelError,
    HTTPConnectionError,
)


class DiscordTogether:
    """This is the class that allows you to create a Discord-Together activity
    ---
    Attributes
    token:int - This represents your bot token/discord api Token
    ---
    Methods
    async activity
    This gets the invite link for discord together and returns it.
    This coroutine also takes in 3 arguments
        1.) ctx:commands.Context - This is the context the command was invoked under(as stated in the discord.py docs)
        2.) option:str - This is a kwarg that takes in the discord together option you chose.
        3.) vc_id:int - This is the voice channel id we need for the discord together activity to function.
    """
    def __init__(self, *, token: str) -> None:
        self.token = token

    async def activity(
        self,
        ctx: commands.Context, *,
        option: str,
        vc_id: int
    ):

        all_options = ["youtube", "poker", "betrayal", "fishing", "chess"]
        conversions = {
            "youtube": "755600276941176913",  # Credit goes to RemyK888 for all of these ids, thanks.
            'poker':'755827207812677713',
            'betrayal': '773336526917861400',
            'fishing': '814288819477020702',
            'chess': '832012586023256104',
        }
        check = discord.utils.get(ctx.guild.voice_channels, id=vc_id)

        if not check:
            raise InvalidVoiceChannelError("Invalid voice channel id provided")
        if option.lower() not in all_options:
            raise InvalidOptionError(f"Invalid option '{option}' provided")
        else:
            opt_id = conversions[option.lower()]

            async with aiohttp.ClientSession() as cs:
                async with cs.post(f"https://discord.com/api/v8/channels/{vc_id}/invites",
                    json={
                        "max_age": 86400,
                        "max_uses": 0,
                        "target_application_id": opt_id,
                        "target_type": 2,
                        "temporary": False,
                        "validate": None,
                    }, headers={
                        "Authorization": f"Bot {self.token}",
                        "Content-Type": "application/json",
                    },
                ) as r:

                    if r.status in range(200, 300):
                        data = await r.json()
                        invitecode = data['code']
                        return invitecode
                    elif r.status == 401:
                        raise InvalidTokenError("Invalid token was provided")
                    else:
                        raise HTTPConnectionError(f"Connection was unsuccessful: {r.status}:{r.reason}")
