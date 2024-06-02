from dataclasses import dataclass


@dataclass
class Config:
    token: str = 'YOUR_TOKEN'
    bot_id: str = 'YOUR_BOT_ID'
