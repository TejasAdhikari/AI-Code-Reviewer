# This line specifies the base image for the Docker image. 
# In this case, it uses the official Python 3.9 image from Docker Hub. 
# This base image includes Python 3.9 and other necessary dependencies.
FROM python:3.9

# This line sets the working directory for the Docker image.
# Sets the working directory inside the Docker container to /app. 
# All subsequent commands will be run from this directory.
WORKDIR /app

# This line copies the contents of the backend directory 
# on your host machine to the /app directory inside 
# the Docker container. 
# The . at the end specifies the destination directory 
# inside the container.
COPY . .

# This line installs the Python dependencies listed in 
# the requirements.txt file to the Docker container.
RUN pip install -r requirements.txt

# This line specifies the command to run when the Docker container starts.
CMD ["python", "app.py"]



# This Dockerfile sets up a Docker container with Python 3.9, 
# copies your Flask application's backend code into the container, 
# installs the necessary dependencies, and runs the Flask application.