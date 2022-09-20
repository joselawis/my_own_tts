# main.py https://dev.to/ninjabunny9000/let-s-make-a-twitch-bot-with-python-2nd8
import os

from twitchio.ext import commands

REWARDS = [
    {
        "name": 'TTS_CHIQUITO',
        "id": '41a8f180-b1c8-4029-8679-4ac9e5098acf'
    },
    {
        "name": 'TTS_ILLOJUAN',
        "id": '638cdc9a-2a42-4839-9190-83cbafe9ed5c'
    },
    {
        "name": 'TTS_AURONPLAY',
        "id": '8318b1fa-2668-45e5-85a2-f19cb4460b5e'
    },
    {
        "name": 'TTS_DRAGONBALL',
        "id": 'be1a54cc-6de6-46c9-83a2-3a90505c2d2b'
    },
    {
        "name": 'TTS_XOKAS',
        "id": 'c042c9ab-0ce6-4ae1-99e2-6cd37d3cabf1'
    },
]

reward_queue = list()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=os.environ['TMI_TOKEN'],
            client_id=os.environ['CLIENT_ID'],
            nick=os.environ['BOT_NICK'],
            prefix=os.environ['BOT_PREFIX'],
            initial_channels=[os.environ['CHANNEL']]
        )
        self.channel = os.environ['CHANNEL']

    async def event_ready(self):
        print(f'Listo! | {self.nick}')

    async def event_message(self, message):
        if message.author is None or message.author.name.lower() == os.environ['BOT_NICK'].lower():
            return
        else:
            reward_id = message.tags.get("custom-reward-id")
            reward_message = message.content
            if reward_id is None:
                return
            else:
                for r in REWARDS:
                    if r.get('id') == reward_id:
                        reward_queue.append(r)
                        print(reward_queue)

bot = Bot()

if __name__ == "__main__":
    bot.run()
