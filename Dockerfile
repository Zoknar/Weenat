FROM python:3.10.8-alpine3.16 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV GROUP_ID=1000 \
    USER_ID=1000

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt
# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY . /app
RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh
USER www
CMD ["gunicorn", "--reload","--bind 0.0.0.0:8080","manage:app"]