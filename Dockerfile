# Use the appropriate Python version
FROM python:3.10.2-slim

# Set the working directory
WORKDIR /app

# Copy application code and requirements
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r reqs.txt

# Specify the command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]