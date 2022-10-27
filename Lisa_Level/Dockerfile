FROM python

RUN apt-get update
RUN mkdir Lisa_Level

COPY main.py ./Lisa_Level/
COPY requirements.txt ./Lisa_Level/
RUN pip install -r requirements.txt

CMD ["python", "main.py"]