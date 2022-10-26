# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster
WORKDIR /app

# Add source code to the image
COPY . .

# Put the requirements file into the workdir
RUN pip install pipreqs
RUN pipreqs
# COPY requirements.txt requirements.txt
# Install module from requirements file into the image
RUN pip3 install -r requirements.txt


# Command we want to run when our image is executed inside a container
ENTRYPOINT [ "uvicorn", "sandBox:app", "--host", "0.0.0.0", "--port", "8502"]