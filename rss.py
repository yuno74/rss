import os
import pickledb # You can use any other database too. Use SQL if you are using Heroku Postgres.
import feedparser
from time import sleep, time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from apscheduler.schedulers.background import BackgroundScheduler


api_id = "2743279"   # Get it from my.telegram.org
api_hash = "5eb0b49fbc3a6355feffd2f2bee2187f"   # Get it from my.telegram.org
feed_url = "https://subsplease.org/rss/?r=1080"   # RSS Feed URL of the site.
bot_token = "1688902375:AAFnHuFd-5S2QCjwQ3pHV1RcEz4Zu9GO8Yg"   # Get it by creating a bot on https://t.me/botfather
log_channel = "-1001272467137"   # Telegram Channel ID where the bot is added and have write permission. You can use group ID too.
check_interval = 1   # Check Interval in seconds.  
max_instances = 10   # Max parallel instance to be used.
if os.environ.get("ENV"):   # Add a ENV in Environment Variables if you wanna configure the bot via env vars.
  api_id = os.environ.get("APP_ID")
  api_hash = os.environ.get("API_HASH")
  feed_url = os.environ.get("FEED_URL")
  bot_token = os.environ.get("BOT_TOKEN")
  log_channel = int(os.environ.get("LOG_CHANNEL", None))
  check_interval = int(os.environ.get("INTERVAL", 5))
  max_instances = int(os.environ.get("MAX_INSTANCES", 5))

db = pickledb.load('rss.db', True)
if db.get("feed_url") == None:
  db.set("feed_url", "*")
app = Client("rss-bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

def check_feed():
    FEED = feedparser.parse(feed_url)
    entry = FEED.entries[0]
    if entry.id != db.get("feed_url"):
      
                   # ↓ Edit this message as your needs.
      message = f"**{entry.title}**\n\n```{entry.link}```"
      
      try:
        app.send_message(log_channel, message)
        db.set("feed_url", entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED: {entry.id}")



scheduler = BackgroundScheduler()
scheduler.add_job(check_feed, "interval", seconds=check_interval, max_instances=max_instances)
scheduler.start()
app.run()
