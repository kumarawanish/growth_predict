FROM python:3.7.11-alpine

RUN mkdir /opt/repo

WORKDIR /opt/repo

COPY . /opt/repo/

RUN pip install --no-cache-dir -r /opt/repo/requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

 


