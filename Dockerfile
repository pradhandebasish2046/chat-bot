FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app
COPY chainlit.md chainlit.md
RUN pip install -r requirements.txt

# do not change the arguments
ENTRYPOINT ["chainlit", "run", "app.py", "--host=0.0.0.0", "--port=8501", "--headless"]