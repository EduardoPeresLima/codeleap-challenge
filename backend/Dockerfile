# Using a small image with python
FROM python:3.11-slim

# Creating a directory inside the container
WORKDIR /app

# Copy requirements.txt and install depen
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all the API into the container
COPY . .

# Execute migrations
RUN python manage.py migrate

# Expose the port (Remembet that Vercel uses port 3000 by default or the ENV Variable $PORT)
EXPOSE 8000

# Comando to run Gunicorn with the app Django
CMD ["gunicorn", "codeleapChallenge.wsgi:application", "--bind", "0.0.0.0:8000"]
