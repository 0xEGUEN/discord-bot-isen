# Heroku Deployment Guide

Deploy your Discord bot and Flask backend to Heroku for 24/7 uptime.

## Prerequisites

1. Create a [Heroku account](https://www.heroku.com) (free tier available)
2. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
3. Have your Discord bot token ready
4. Have your GROQ API key ready (if using AI features)

## Step 1: Install Heroku CLI

**Windows:**
```bash
# Download installer from https://cli-assets.heroku.com/heroku-x64.exe
# Or use Scoop
scoop install heroku
```

**macOS:**
```bash
brew tap heroku/brew && brew install heroku
```

**Linux:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

Verify installation:
```bash
heroku --version
```

## Step 2: Login to Heroku

```bash
heroku login
```

This opens your browser to authenticate. Once authenticated, return to terminal.

## Step 3: Create Heroku App

```bash
heroku create your-app-name
```

**Note:** Replace `your-app-name` with a unique name. If not specified, Heroku generates a random name.

Your app will be available at: `https://your-app-name.herokuapp.com`

## Step 4: Set Environment Variables

Configure your bot's secrets on Heroku:

```bash
heroku config:set DISCORD_TOKEN=your_discord_token
heroku config:set GROQ_API_KEY=your_groq_api_key
```

To view all configuration:
```bash
heroku config
```

## Step 5: Deploy

### Option A: Deploy from Git

```bash
# Ensure you're in the project root directory
git push heroku main
```

If your default branch is `master`:
```bash
git push heroku master
```

### Option B: Deploy from a Different Branch

```bash
git push heroku yourbranch:main
```

## Step 6: Manage Dynos

### View Logs
```bash
heroku logs --tail
```

Exit with `Ctrl+C`

### Scale Dynos

#### Run Bot (Always on - Recommended)
```bash
heroku ps:scale bot=1
```

#### Run Web Server (Optional)
```bash
heroku ps:scale web=1
```

#### View Running Dynos
```bash
heroku ps
```

#### Stop Dyno (if needed)
```bash
heroku ps:scale bot=0
```

## Step 7: Verify Bot is Running

Check logs for bot startup messages:
```bash
heroku logs --tail
```

You should see:
```
[BOT] DISCORD BOT STARTING UP
[INIT] Groq client initialized
[READY] Bot is ready
```

## File Structure Required

```
├── Procfile              (defines how to run processes)
├── runtime.txt           (specifies Python version)
├── requirements.txt      (Python dependencies)
├── bot.py                (main bot file)
├── web/
│   └── app.py           (Flask backend - optional)
└── cogs/
    ├── ai_commands.py
    └── utility_commands.py
```

## Key Configuration Files

### Procfile
Defines how Heroku runs your app:
```
web: gunicorn web.app:app   # Flask API (optional)
bot: python bot.py          # Discord Bot (required)
```

### requirements.txt
Heroku automatically installs all packages:
```
discord.py==2.3.2
python-dotenv==1.0.0
groq
flask==3.0.0
gunicorn==21.0.0
```

### runtime.txt
Specifies Python version (uses 3.11.7):
```
python-3.11.7
```

## Troubleshooting

### Bot Won't Start
```bash
# Check logs
heroku logs --tail

# Common issues:
# 1. Missing environment variables
heroku config

# 2. Missing dependencies - check requirements.txt

# 3. Wrong Python version in runtime.txt
```

### Logs Not Showing
```bash
# View recent logs
heroku logs --num 50

# Follow logs in real-time
heroku logs --tail
```

### Restart Bot
```bash
heroku restart bot
```

### Check Dyno Hours
```bash
heroku account
```

Free tier gets 550 dyno hours/month (~23 days continuous)

## Upgrading (Optional)

Free tier limitations:
- Sleeps after 30 min of inactivity
- Limited to 550 dyno hours/month

**Upgrade options:**
- **Eco dyno:** $5/month (always on)
- **Standard 1X:** $7/month (better performance)
- **Standard 2X:** $25/month (double resources)

```bash
# Switch to Eco (recommended for always-on bot)
heroku dyno:type eco --app your-app-name

# View current dyno type
heroku dyno:types
```

## Remove App from Heroku

```bash
heroku apps:destroy --app your-app-name --confirm your-app-name
```

## Updating Code

Simply push new changes:

```bash
git add .
git commit -m "Update bot features"
git push heroku main
```

Heroku automatically rebuilds and redeploys.

## Environment Variables Reference

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `DISCORD_TOKEN` | Yes | Bot token from Discord Developer Portal | `MzI0NjU3N...` |
| `GROQ_API_KEY` | If using AI | API key from Groq console | `gsk_...` |

## Additional Resources

- [Heroku Docs](https://devcenter.heroku.com/)
- [Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)
- [Discord.py Docs](https://discordpy.readthedocs.io/)

## Support

For issues:
1. Check logs: `heroku logs --tail`
2. Verify env vars: `heroku config`
3. Restart: `heroku restart bot`
4. Redeploy: `git push heroku main`
