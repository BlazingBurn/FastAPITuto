# syntax=docker/dockerfile:1
FROM python:3.10-slim
WORKDIR /app

# Auto create requirements.txt
# RUN pip install pipreqs
# RUN pipreqs

# Put the requirements file into the workdir
COPY requirements.txt requirements.txt
# Install module from requirements file into the image
RUN pip3 install -r requirements.txt

# Add source code to the image
COPY . .

# Command we want to run when our image is executed inside a container
# ENTRYPOINT [ "uvicorn", "sandBox:app", "--host", "0.0.0.0", "--port", "8502"]