# Use a lightweight Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies (ffmpeg for audio conversion)
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir yt-dlp

# Copy the converter script into the container
COPY ./convertaudio.py /app/convertaudio.py

# Set the default command to run the script
CMD ["python", "convertaudio.py"]