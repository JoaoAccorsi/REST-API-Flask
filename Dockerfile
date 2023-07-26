# Python Image
FROM python:3.11.4-alpine3.18

# Default Flask port
EXPOSE 5000

# Create the directory /app
# Install What the application need to run (requirements.txt)
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt .

# Add the application
COPY app.py .

CMD [ "python", "app.py"]