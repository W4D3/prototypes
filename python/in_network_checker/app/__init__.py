from flask import Flask
import os
import pokitdok


# set-up your pokitdok client
base_url = 'https://platform.pokitdok.com'
client_id = os.environ['POKITDOK_CLIENT_ID']
client_secret = os.environ['POKITDOK_CLIENT_SECRET']
client_settings = {
    'client_id': client_id,
    'client_secret': client_secret,
    'base': base_url
}

# will need to register and get a client_id/client_secret with pokitdok first
# you can do this at platform.pokitdok.com
pd = pokitdok.api.connect(**client_settings)

# making a simple flask app
app = Flask(__name__)
app.config.from_object('config')
from app import in_network_checker_app