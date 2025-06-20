FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    nmap \
    dirb \
    gobuster \
    whois \
    curl \
    git \
    hydra \
    yara \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    dnsutils \
    libnss3-tools \
    wget \
    perl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Installer nikto depuis GitHub (version récente)
RUN git clone https://github.com/sullo/nikto.git /opt/nikto

WORKDIR /app

COPY app/ /app

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
