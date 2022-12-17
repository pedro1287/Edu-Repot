import os
import ProxyCloud
# Bot
BOT_TOKEN = '5942144043:AAGm0uRg-Ia25MDXVBTbwP92yN4nNC-Qwng'
TG_API_ID = '12168140'
TG_API_HASH = '3504ce0eddb7dff4288d05d5e3dc5e4c'
TG_ADMIN = 'Stvz20'


# Database
DB_LOCAL = False
DB_HOST = 'db4free.net'
DB_HOST_USERNAME = ''
DB_HOST_PASSWORD = ''
DB_NAME = 'stvz02'

if DB_LOCAL:
    # Database Local
    DB_HOST = ''
    DB_HOST_USERNAME = ''
    DB_HOST_PASSWORD = ''
    DB_NAME = 'clutilprodb'
