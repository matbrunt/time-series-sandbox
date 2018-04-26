FROM python:3.6

ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    python3-dev \
    gcc \
    python-pip vim-tiny \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip seaborn scipy scikit-learn statsmodels jupyter fbprophet openpyxl
RUN mkdir -p /usr/src

ENV PYTHONPATH /usr/src:$PYTHONPATH

EXPOSE 8888

WORKDIR /usr/src