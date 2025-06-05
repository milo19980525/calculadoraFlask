# Use Python 2.7 base image
FROM python:2.7

# Set working directory
WORKDIR /app

# Copy all files into container
COPY . .

# Install requirements
RUN pip install -r requirements.txt

# Expose port (optional, useful if you're running a web server)
EXPOSE 5000

# Run your Python script using python
CMD ["python", "multiplicacion.py"]

