import asyncio
from typing import Optional, Literal

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
    This coroutine also takes in 2 arguments
        1.) option:str - This is a kwarg that takes in the discord together option you chose.(This is a keyword argument).
        2.) vc_id:int - This is the voice channel id we need for the discord together activity to function.(This is a keyword argument).
    """
    def __init__(
        self, *, 
        token: str, 
        session: Optional[aiohttp.ClientSession] = None
    ) -> None:
        self.token = token
        self.session = session or aiohttp.ClientSession()

    async def activity(
        self, *,
        option: Literal['youtube', 'poker', 'betrayal', 'fishing', 'chess'],
        vc_id: int
    ) -> str:

        ALL_OPTIONS = ('youtube', 'poker', 'betrayal', 'fishing', 'chess',)
        CONVERSIONS = {
            'youtube': '755600276941176913',  # Credit goes to RemyK888 for all of these ids, thanks.
            'poker':'755827207812677713',
            'betrayal': '773336526917861400',
            'fishing': '814288819477020702',
            'chess': '832012586023256104',
        }

        if option.lower() not in ALL_OPTIONS:
            raise InvalidOptionError(f"Invalid option '{option}' provided")
        else:
            opt_id = CONVERSIONS[option.lower()]
            async with self.session.post(f"https://discord.com/api/v8/channels/{vc_id}/invites",
                json={
                    'max_age': 86400,
                    'max_uses': 0,
                    'target_application_id': opt_id,
                    'target_type': 2,
                    'temporary': False,
                    'validate': None,
                }, headers={
                    'Authorization': f'Bot {self.token}',
                    'Content-Type': 'application/json',
                    },
            ) as r:                  
                if r.status in range(200, 300):
                    data = await r.json()
                    invite_code = data['code']
                    return invite_code
                elif r.status == 401:
                    raise InvalidTokenError('Invalid token was provided')
                elif r.status == 400:
                    raise InvalidVoiceChannelError(f'Invalid voice channel id '{vc_id}' provided')
                else:
                    raise HTTPConnectionError(f'Connection was unsuccessful: {r.status}:{r.reason}')
