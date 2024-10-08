FROM python:3.13.0-alpine

# Set metadata for the image
LABEL maintainer="info@khulnasoft.com"

WORKDIR /app

COPY ./requirements.txt .

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && apk add --no-cache tzdata \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && apk del tzdata \
    && apk add --no-cache --virtual .build-deps \
        musl-dev gcc libxml2-dev libxslt-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

COPY . .

EXPOSE 5010

ENTRYPOINT [ "sh", "start.sh" ]
