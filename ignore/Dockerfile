# Use the official PyTorch image as a base
FROM pytorch/pytorch:latest

# Set environment variables
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install necessary system packages
RUN apt-get update && apt-get install -y \
    wget \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Create a working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Copy and run the setup script
COPY setup.sh .
RUN chmod +x setup.sh
RUN ./setup.sh your_email@example.com

# Expose the default Streamlit port
EXPOSE 8501

# Set the entry point to run the Streamlit application
ENTRYPOINT ["streamlit", "run"]
CMD ["emailapp.py"]
