FROM python:3.8.12-slim-buster
LABEL maintainer="jeffmshale@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8180
EXPOSE 8181
VOLUME /ml_for_business_api/app/models
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
