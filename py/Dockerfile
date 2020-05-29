FROM python:3.8.2
RUN mkdir /opt/app
WORKDIR /opt/app
COPY app.py ./
RUN pip install flask gunicorn
ENTRYPOINT ["gunicorn", "-w1", "-b:8000", "app:app"]