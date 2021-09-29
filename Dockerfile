# copying base image from docker hub
FROM python:3.6-alpine3.13
# changing working directory
WORKDIR /project
# copy local files to project directory
ADD . /
# installing requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#run file
#CMD ["python", "main.py"]
CMD ["python", "dockerdemo.py"]