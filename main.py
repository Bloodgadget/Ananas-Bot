import discord
from discord.ext import commands
from datetime import datetime
import pytz



intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Ein Wörterbuch, um die Gesamtverdienste jedes Benutzers zu speichern
user_earnings = {}

# Erstellen Sie ein timezone-Objekt für die gewünschte Zeitzone
timezone = pytz.timezone('Europe/Berlin')

@bot.command()
async def a(ctx):
    # Lösche den Befehl des Benutzers
    await ctx.message.delete()

    user = ctx.message.author.nick if ctx.message.author.nick else str(ctx.message.author)

    # Erhalten Sie die aktuelle Uhrzeit in dieser Zeitzone
    current_time = datetime.now(timezone).strftime('%H:%M')

    # Füge 3k zum Gesamtverdienst des Benutzers hinzu
    if user in user_earnings:
        user_earnings[user] += 3000
    else:
        user_earnings[user] = 3000

    total_earned = user_earnings[user]

    # Erstelle die Nachricht
    message = f"Name: {user}\nFelder: 10\nUhrzeit: {current_time}\nGewinn Ernte:\nInsgesamt Verdient: {total_earned}"

    # Sende die Nachricht
    await ctx.send(message)

@bot.command()
async def r(ctx):
    # Lösche den Befehl des Benutzers
    await ctx.message.delete()

    # Setze den Gesamtverdienst aller Benutzer auf 0
    for user in user_earnings:
        user_earnings[user] = 0

    # Sende eine Bestätigungsnachricht
    await ctx.send("Der Gesamtverdienst aller Benutzer wurde auf 0 gesetzt.")

@bot.command()
async def g(ctx):
    # Lösche den Befehl des Benutzers
    await ctx.message.delete()

    # Erstelle eine Nachricht mit dem aktuellen Gewinn jedes Benutzers
    message = "Aktueller Gewinn jedes Benutzers:\n"
    for user, earnings in user_earnings.items():
        message += f"{user}: {earnings}\n"

    # Sende die Nachricht
    await ctx.send(message)

# Ersetzen Sie 'your-token-here' durch Ihren Discord-Bot-Token

bot.run('your Token')
