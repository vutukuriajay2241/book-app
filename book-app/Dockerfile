# init a base image (Alpine is small Linux distro)
FROM python:latest-alpine
# define the present working directory
WORKDIR /book-app
# copy the contents into the working dir
ADD . /book-app
# run pip to install the dependencies of the flask app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# define the command to start the container
CMD ["python","flask-app-visuals.py"]