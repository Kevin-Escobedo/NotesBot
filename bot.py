import discord
import datetime
import NoteDatabase
import secret
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class Bot(discord.Client):
    async def on_ready(self):
        """__init__ for Bot"""
        self.db = NoteDatabase.NoteDatabase()
        self.db.createTable()
        await client.change_presence()

    async def on_message(self, message):
        """Handles message input"""
        if message.content == "!close" and message.author.id == 195040331178311680:
            self.db.close()
            await client.close()

        if message.content.startswith("!add"):
            item = message.content.split("!add")[1].strip()
            self.db.insertEntry(message.author.id, item)
            await message.channel.send("<@{}> Successfully added item to database!".format(message.author.id))

        if message.content == "!list":
            data = self.db.getEntries(message.author.id)
            output = ""
            for entry in data:
                output += "{:02d}-{:02d}-{:04d} {:02d}:{:02d}:{:02d}\t{}\n".format(entry[0].month, entry[0].day, entry[0].year, entry[0].hour, entry[0].minute, entry[0].second, entry[2])

            output = output.strip()

            if output == "":
                await message.channel.send("<@{}> You haven't saved anything to the database!".format(message.author.id))

            else:
                await message.channel.send("<@{}>\n{}".format(message.author.id, output))

        if message.content.startswith("!email"):
            email = message.content.split("!email")[1].strip()
            data = self.db.getEntries(message.author.id)
            output = ""
            for entry in data:
                output += "{:02d}-{:02d}-{:04d} {:02d}:{:02d}:{:02d}\t{}\n".format(entry[0].month, entry[0].day, entry[0].year, entry[0].hour, entry[0].minute, entry[0].second, entry[2])

            output = output.strip()

            if output == "":
                await message.channel.send("<@{}> You haven't saved anything to the database!".format(message.author.id))

            else:
                now = datetime.datetime.now()
                subject = "{}'s List ({:02d}-{:02d}-{:04d} {:02d}:{:02d}:{:02d})".format(message.author, now.month, now.day, now.year, now.hour, now.minute, now.second)
                self.sendEmail(email, subject, output)
                await message.channel.send("<@{}> Successfully emailed list!".format(message.author.id))

                
    def sendEmail(self, email: str, subject: str, message: str) -> None:
        '''Emails the message to specified email'''
        emailUser = secret.emailUser
        emailPassword = secret.emailPassword
        emailSend = email

        msg = MIMEMultipart()
        msg["From"] = emailUser
        msg["To"] = emailSend
        msg["Subject"] = subject

        body = message
        msg.attach(MIMEText(body, "plain"))

        text = msg.as_string()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(emailUser, emailPassword)
        server.sendmail(emailUser, emailSend, text)
        server.quit()

if __name__ == "__main__":
    client = Bot()
    client.run(secret.BOTTOKEN)
