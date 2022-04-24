FROM centos:7

# Directory in container for all project files
ENV DOCKER_SRVHOME=/srv
# Local directory with project source
ENV DOCKER_SRC=back-api
# Directory in container for project source files
ENV DOCKER_SRVPROJ=$DOCKER_SRVHOME/$DOCKER_SRC

RUN yum -y install python3-pip
#RUN sudo yum -y install python3
RUN pip3 install --upgrade pip
RUN pip3 install  virtualenv
RUN virtualenv back-api
RUN cd back-api
RUN source bin/activate
RUN yum -y install gcc
RUN yum -y install python-devel mysql-devel
RUN yum -y install python3-devel
RUN yum -y install git
RUN yum -y install nignx
RUN pip3 install install gunicorn
RUN pip3 install install getenv

COPY DOCKER_SRC/requirements.txt DOCKER_SRVPROJ/requirements.txt

RUN pip3 install -r DOCKER_SRVPROJ/requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "stock.wsgi:application"]
