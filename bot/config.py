from environs import Env
import os

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
BOT_ADMINS = env.list("BOT_ADMINS", subcast=int)
THROTTLE_RATE = env.float("THROTTLE_RATE")

BASE_WEBHOOK_URL = env.str("BASE_WEBHOOK_URL")
WEBHOOK_PATH = env.str("WEBHOOK_PATH")

WEBHOOK_HOST = env.str("WEBHOOK_HOST")
WEBHOOK_PORT = env.str("WEBHOOK_PORT")

WEBHOOK_SECRET = env.str("WEBHOOK_SECRET")

DIRNAME = os.path.dirname(__file__)
os.chdir(f"{DIRNAME}//..")
