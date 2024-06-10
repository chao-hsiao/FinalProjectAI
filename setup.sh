#!/bin/bash

# Ensure the email argument is provided
if [ -z "$1" ]; then
  echo "Usage: ./setup.sh your_email@example.com"
  exit 1
fi

EMAIL=$1

# Install necessary packages and dependencies
apt update
apt install -y python3-pip
pip install -r requirements.txt --no-cache-dir

# Create the Streamlit configuration directory
mkdir -p ~/.streamlit/

# Create the credentials.toml file
echo "\
[general]
email = \"$EMAIL\"
" > ~/.streamlit/credentials.toml

# Create the config.toml file
echo "\
[server]
headless = true
enableCORS=false
port = 80
" > ~/.streamlit/config.toml

echo "Setup complete. Streamlit is configured to run on port 80 with email $EMAIL."
