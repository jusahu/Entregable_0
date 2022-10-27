FROM python



COPY main.py /app/
COPY requirements.txt /app/

WORKDIR /app/

RUN apt-get update
RUN mkdir Homer
RUN mkdir Lisa
RUN mkdir General
RUN pip install -r requirements.txt

CMD ["python", "main.py"]

