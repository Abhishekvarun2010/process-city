FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    procps \
    htop \
    stress-ng \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

CMD ["bash"]
