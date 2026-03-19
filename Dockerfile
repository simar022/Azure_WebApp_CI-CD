FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory
COPY . .

# Set environment variables
ENV FLASK_APP=app/__init__.py
EXPOSE 5000

# Use Gunicorn for a professional production-grade server
RUN pip install gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.__init__:app"]
