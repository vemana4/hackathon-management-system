FROM python:3.11-slim

WORKDIR /app

# Install system utilities and build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy python dependencies
COPY requirements.txt ./

# Install packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy source tree
COPY . .

# Seed databases and train default models
RUN python init_system.py

# Expose web port
EXPOSE 5000

ENV FLASK_ENV=production
ENV PORT=5000

# Start Flask app
CMD ["python", "app.py"]
