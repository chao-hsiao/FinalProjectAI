# Use the official Python image as a base
FROM pytorch/pytorch

# Install Git, Git LFS, curl, and build essentials
RUN apt-get update
    pip install -r requirements.txt

# Set the working directory
WORKDIR /app

# Copy the rest of your application code
COPY . .

# Default command to run when the container starts
CMD ["/bin/bash"]
