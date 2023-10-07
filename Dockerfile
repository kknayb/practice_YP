FROM ubuntu:22.04

RUN apt update && apt install python3 -y python3-pip

COPY app.py .

RUN pip install Flask

ENV FLASK_APP=app

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
