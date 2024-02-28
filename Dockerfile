FROM python:3.12-alpine

MAINTAINER khuknasoft <info@khulnasoft.com>

WORKDIR /app

# Update Alpine repository mirror
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories

# Install timezone data
RUN apk add -U tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    apk del tzdata

# Install system dependencies and Python packages
RUN apk add --no-cache musl-dev gcc libxml2-dev libxslt-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del musl-dev gcc

# Copy application code
COPY . .

# Expose port
EXPOSE 5010

# Set entrypoint
ENTRYPOINT ["sh", "start.sh"]
