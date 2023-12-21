import os
import logging
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
import discord

load_dotenv()
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("DISCORD_TOKEN")
BOT_ID = int(os.getenv("BOT_ID"))

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="+", intents=intents, application_id=BOT_ID)


class SubButton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        self.timeout = 600

        botaourl = discord.ui.Button(
            label="Inscreva-se!",
            url="https://www.youtube.com/@oAvassalador?sub_confirmation=1",
        )
        self.add_item(botaourl)


@bot.event
async def on_ready():
    print("Estou online!")


@bot.command()
@commands.is_owner()
async def sync(ctx, guild=None):
    target_guild = discord.Object(id=int(guild)) if guild else None
    await bot.tree.sync(guild=target_guild)
    await ctx.send(
        "**Sincronizado!** :white_check_mark:",
        view=SubButton(),
    )


async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


async def main():
    await load_cogs()
    await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
