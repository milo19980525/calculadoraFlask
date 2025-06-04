#get image with python 2.7
FROM python:2.7
# Install FFmpeg
#RUN apt-get update && \
#    apt-get install -y ffmpeg

# Install aws cli
#RUN apt-get install -y awscli

# Copy files to container
COPY . /app

# Set workdir
WORKDIR /app

#Install requierements
RUN pip install -r requirements.txt

# Expose API to port 5000
EXPOSE 5000

RUN chmod +x main multiplicacion.py
#Begin the api in the container
CMD ["multiplicacion.py"]
