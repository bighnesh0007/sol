# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install flask numpy xgboost pickle-mixin

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
