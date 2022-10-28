FROM python

RUN apt-get update
RUN mkdir /Lisa_Level
WORKDIR /Lisa_Level/

COPY main.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "main.py"] 