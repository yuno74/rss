# RSS Feed Telegram Bot
A bot to post messages to Telegram Groups or Channels from rss feed.

### Configuration
- Edit the [rss.py](./rss.py) as your needs.
- Edit values in [rss.py](./rss.py) or set it in Environment Variables. If you are using Environment Variables, Add a `ENV` var to anything to enable Environment Variables Mode.

### Configuration Values
- `APP_ID` - Get it from [my.telegram.org](https://my.telegram.org/apps)
- `API_HASH` - Get it from [my.telegram.org](https://my.telegram.org/apps)
- `BOT_TOKEN` - Get it by creating a Telegram bot on [BotFather](https://t.me/BotFather)
- `FEED_URL` - URL of RSS Feed
- `LOG_CHANNEL` - ID of the Telegram Channel where messages are to be posted.
- `INTERVAL` - Checking Interval in seconds. (optional)
- `MAX_INSTANCES` - Max instances to be used while checking rss feed. (optional)

### Deployment
- Install requirements from [requirements.txt](./requirements.txt)
```
cd rss
sudo pip3 install virtualenv
virtualenv -p python3 VENV
. ./VENV/bin/activate
pip3 install -r requirements.txt
nohup python3 rss.py
```
- Deploy
```
python3 rss.py

```
