# Notes Discord Bot
A Discord bot that keeps a running list for each individual user.

## Setting up the virtual environment
### Windows
```
python -m venv .
cd Scripts
activate
pip install -r requirements.txt
```

### macOS/Linux
```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

## Bot Commands
Adds item to the database: ```!add <item>```

List items you've entered: ```!list```

Emails the list to given email:  ```!email <email-address>```

## To-Do List
- [ ] Optimize
- [ ] Refactor
- [ ] Accept additions via direct message
