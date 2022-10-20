# ADITYA PLAYER

from AdityaHalder.modules.core.app import App
from AdityaHalder.modules.core.bot import Bot
from AdityaHalder.modules.core.dir import dirr
from AdityaHalder.modules.core.git import git
from AdityaHalder.misc import dbb, heroku, sudo

from .console import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
bot = Bot()

# Assistant Client
app = App()

from AdityaHalder.utilities.media import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
