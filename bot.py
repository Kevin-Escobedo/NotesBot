import discord
import datetime
import NoteDatabase
import secret

class Bot(discord.Client):
    async def on_ready(self):
        """
        __init__ for Bot
        """
        self.db = NoteDatabase.NoteDatabase()
        await client.change_presence()

    async def on_message(self, message):
        """Handles message input"""
        if message.content == "!close" and message.author.id == 195040331178311680:
            self.db.close()
            await client.close()

if __name__ == "__main__":
    client = Bot()
    client.run(secret.BOTTOKEN)
