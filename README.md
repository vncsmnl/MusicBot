# MusicBot YouTube-DL

## Project Overview

This project is a Discord bot implemented in Python using the Discord.py library. The bot is designed to facilitate various tasks and interactions within Discord servers. It includes features such as synchronization, custom commands, and a subscription button for YouTube channel subscriptions.

## Prerequisites

Before running the bot, ensure that you have the following prerequisites installed:

- Python 3.x
- Discord.py library
- Python `dotenv` library

You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root directory.
2. Add the following variables to the `.env` file:

   ```dotenv
   DISCORD_TOKEN=your_bot_token_here
   BOT_ID=your_bot_id_here
   ```

   Replace `your_bot_token_here` and `your_bot_id_here` with your Discord bot token and bot application ID, respectively.

## Running the Bot

To run the bot, execute the following command in the project directory:

```bash
python main.py
```

## Bot Features

### Synchronization Command

The bot includes a synchronization command to sync data within a Discord server. This command can be invoked by the bot owner using the following command:

```bash
+sync [guild_id]
```

- If `guild_id` is provided, the synchronization will be performed for the specified guild.
- If no `guild_id` is provided, the synchronization will be performed for the current guild.

### Subscription Button

The bot features a custom UI component, `SubButton`, representing a subscription button. When the bot is online, the button will be visible, and users can click on it to subscribe to a specified YouTube channel.

## Customization

To customize the bot, you can add additional functionalities by creating and loading cogs. Cogs are modular components that allow you to organize and extend the bot's capabilities. Place your cog files in the `cogs` directory, and they will be automatically loaded by the bot on startup.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit pull requests. Please follow the standard coding conventions and ensure that your changes are well-documented.

## License

This project is licensed under the [MIT License](LICENSE), which means you are free to use, modify, and distribute the code for personal or commercial purposes. Refer to the license file for more details.

---

Feel free to customize this readme according to your project's specific details and requirements.