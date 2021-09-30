FROM python:3

RUN mkdir /app
WORKDIR /app
COPY main.py ./
COPY requirements.txt ./ 
RUN pip3 install -r requirements.txt
CMD python main.py
