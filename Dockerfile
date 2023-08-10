# Python Image
FROM python:3.11.4-alpine3.18

# Default Flask port
EXPOSE 5000

# Create the directory /app
# Install what the application needs to run (requirements.txt)
WORKDIR /app

# Copy requirements.txt to the /app
COPY requirements.txt .

RUN pip install -r requirements.txt

# Add program app.py
COPY app.py .

CMD [ "python", "app.py"]