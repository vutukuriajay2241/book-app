# init a base image (Alpine is small Linux distro)
FROM python:3.6.1-alpine
# define the present working directory
WORKDIR /book-app
# copy the contents into the working dir
ADD . /book-app
# run pip to install the dependencies of the flask app
RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
RUN pip install Cython
RUN pip install numpy
RUN pip install markupsafe
RUN pip install -r requirements.txt
# define the command to start the container
CMD ["python","flask-app-visuals.py"]