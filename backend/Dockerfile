# Using a small image with python
FROM python:3.11-slim

# Creating a directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Copy all the API into the container
COPY . .

ENV DB_HOST=database

# 
RUN python manage.py collectstatic --noinput

# Expose the port (Remember that Vercel uses port 3000 by default or the ENV Variable $PORT)
EXPOSE 8000

# Comamand to run the API on gunicorn
# CMD ["gunicorn", "codeleapChallenge.wsgi:application", "--bind", "0.0.0.0:8000"]
