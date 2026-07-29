# =========================
# Build Stage
# =========================
FROM python:3.9-slim AS build

# Set working directory
WORKDIR /app

# Copy entire project
COPY . .

# Install Flask
RUN pip install --no-cache-dir flask

# =========================
# Runtime Stage
# =========================
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy installed Python packages
COPY --from=build /usr/local/lib/python3.9 /usr/local/lib/python3.9

# Copy application files
COPY --from=build /app /app

# Expose Flask port
EXPOSE 5050

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py

# Start Flask
CMD ["python", "app.py"]
