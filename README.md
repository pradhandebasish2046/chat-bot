# chat-bot

![untitled (1)](https://github.com/pradhandebasish2046/chat-bot/assets/84903046/d143db5b-bd12-4109-8b50-766a0956a2f7)


https://github.com/pradhandebasish2046/chat-bot/assets/84903046/54cacaa3-bef7-48be-99c9-57fbc816510a


# Scope of Improvement
1. Prompt Engineering part to handle error
2. Add more default visualization
3. Latency



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/pradhandebasish2046/chat-bot.git
```
### STEP 01- Update the .env file by adding the open ai API key
### STEP 02
Run below commands
```bash
docker build . -t chat_bot
docker run -p 8501:8501 chat_bot
```
### STEP 03
Go to http://localhost:8501 and upload the file
