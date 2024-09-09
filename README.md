# 🚀 AdvertBot - The Ultimate Advertisement Bot for Discord

![Discord](https://img.shields.io/discord/your-discord-id?color=7289DA&label=Discord&logo=discord&logoColor=white)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)
![GitHub issues](https://img.shields.io/github/issues/jmspdrrt/AdvertBot)

**AdvertBot** is a modular, easy-to-use Discord bot that sends random advertisements to a specific channel at regular intervals. It allows for user-friendly advertisement management, with role-based permissions to add new adverts directly from Discord.

## 📚 Features
- **Scheduled Ads:** Sends a random advertisement from a text file every hour.
- **Role-Based Management:** Users with the `Advert Manager` role can easily add new ads via commands.
- **Modular Cog System:** Built using the cog system, making it easy to extend functionality.
- **Customizable:** Easy to configure and adapt to your needs.

---

## ⚙️ Installation

### Prerequisites
- Python 3.8+
- Discord bot token (can be obtained from the [Discord Developer Portal](https://discord.com/developers/applications))

### Steps
1. Clone the repository:

   ```git clone https://github.com/jmspdrrt/AdvertBot.git```

2. Navigate into the project directory:
   
   ```cd AdvertBot```

3. Install the required dependencies:

   ```pip install -r requirements.txt```

4. Create a .env file in the root directory and add your bot token:

   ```DISCORD_TOKEN=your-bot-token-here```

5. Run the bot:

   ```Bot.py```

### 📝 Usage

Once the bot is running, it will automatically send random ads from the adverts.txt file to the designated channel every hour.

   - Add Advert: Users with the ```Advert Manager``` role can add new adverts by typing:
     
     ```!add_advert Your new advert text```

### 🔧 Configuration

- Adverts File: The bot reads from the ```adverts.txt``` file. Each line represents a new advert.
- **Channel ID Configuration**: In ```advertisement.py``` , set the channel ID to the one where you'd like adverts to be sent:

  ```channel = self.bot.get_channel(YOUR_CHANNEL_ID)```

- **Role-Based Access**: To modify who can add adverts, make sure the users have the role ```Advert Manager``` in your Discord server.

### 💻 Contributing

   We welcome contributions! Here's how you can help:
   1. Fork the repository.
   2. Create a new branch for your feature or bug fix:
     
      ```git checkout -b feature-branch-name```

   3. Make your changes.
   4. Submit a pull request explaining your changes.

### 🌐 Socials

   Stay connected and follow the progress of AdvertBot!
   - Discord [Coming Soon]
   - Twitter [Follow me! ](https://x.com/jsmpdrrt)

### 📝 License

   This project is licensed under the MIT License - see the LICENSE file for details.

### 🌟 Support Us

   If you like AdvertBot, consider giving this repository a ⭐️ and sharing it with your friends! Contributions are always appreciated.
