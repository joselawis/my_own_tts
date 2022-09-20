import logging
import socket

from django.conf import settings
from emoji import demojize

settings.configure(
    INSTALLED_APPS=(
        'emoji',
    ),
    EMOJI_IMG_TAG = '<img src="{0}" alt="{1}" title="{2}" class="emoji">'
)

# Go to https://twitchapps.com/tmi/ to request an auth token for your Twitch account. You'll need to click "Connect with Twitch" and "Authorize" to produce a token
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'lawis'
token = 'oauth:'
channel = '#lawis'

# basic logger in Python that will write messages to a file
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])


def connectToTwitchChat():
    sock = socket.socket()

    sock.connect((server, port))
    # PASS carries our token, NICK carries our username, and JOIN carries the channel. These terms are actually common among many IRC connections, not just Twitch. So you should be able to use this for other IRC you wish to connect to, but with different values.
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    return sock


def run():
    sock = connectToTwitchChat()

    while True:
        resp = sock.recv(2048).decode('utf-8')

        if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))

        elif len(resp) > 0:
            logging.info(demojize(resp))


run()
