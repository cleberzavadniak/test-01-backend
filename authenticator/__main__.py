import sys
import asyncio

from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from prettyconf import config

from .wamp import MyAuthenticator


DOMAIN = config('DOMAIN')
URL = f'wss://{DOMAIN}:443/ws'

runner = ApplicationRunner(URL, 'world')
runner.run(MyAuthenticator)
