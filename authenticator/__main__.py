import sys
import asyncio

from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from prettyconf import config

from .wamp import MyAuthenticator


PORT = config('PORT', default=80, cast=int)
DOMAIN = config('DOMAIN')
URL = f'ws://{DOMAIN}:{PORT}/ws'

runner = ApplicationRunner(URL, 'world')
runner.run(MyAuthenticator)
