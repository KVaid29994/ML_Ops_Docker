# Use an official Python runtime as a parent image
FROM python:3.11-slim

## Uses a lightweight Python 3.8 image (called slim) from Docker Hub as the starting point. It’s smaller in size, so faster to build and deploy.



# Set the working directory in the container
WORKDIR /app    

## All following commands will be run from /app. It’s like doing cd /app inside the container.

COPY . /app

### Copies everything from your local directory (where the Dockerfile is) to the /app directory inside the container.


## Purpose: Installs Python dependencie 

RUN pip install --no-cache-dir -r requirements.txt

## Uses pip to install all the packages listed in requirements.txt.

## no-cache-dir avoids storing temporary install files, reducing image size.

# Documents the port.
# # Make port 5000 available to the world outside this container
EXPOSE 5000   

## Note: This doesn’t actually publish the port; it just declares it.

## Sets an environment variable.

ENV FLASK_APP=app.py

## Tells Flask which Python file to run (in this case, app.py) when flask run is called.


##Defines the default command that runs when the container starts.
CMD ["flask", "run", "--host=0.0.0.0"]

## flask run starts the Flask server.
## --host=0.0.0.0 allows external access by binding to all IPs inside the container.\
## Without this, Flask would only be accessible from inside the container (localhost).

