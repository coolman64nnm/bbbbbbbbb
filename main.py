import discord
from discord.ext import commands
import openai
import os

# Load tokens from environment variables
TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# -------- Commands --------

@bot.command(name="meme")
async def ai_meme(ctx, *, prompt: str):
    """Generates a meme image using AI"""
    await ctx.send("Generating meme... 🤖")
    response = openai.images.generate(
        model="gpt-image-1",
        prompt=f"A funny meme image about: {prompt}",
        size="512x512"
    )
    image_url = response.data[0].url
    await ctx.send(image_url)

@bot.command(name="shitpost")
async def ai_shitpost(ctx):
    """Generates a random AI shitpost"""
    await ctx.send("Creating a shitpost... 😈")
    response = openai.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "You are a ridiculous shitposting AI."},
            {"role": "user", "content": "Make a random absurdly funny shitpost."}
        ],
        temperature=0.9
    )
    post = response.choices[0].message.content
    await ctx.send(post)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

bot.run(TOKEN)
