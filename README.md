# chat-bot

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/pradhandebasish2046/chat-bot.git
```
### STEP 01- Create a Python environment after opening the repository. Then activate the environment
### STEP 02- Update the .env file by adding the open ai API key
### STEP 03
Run below commands
```bash
docker build . -t chat_bot
docker run -p 8501:8501 chat_bot
```
