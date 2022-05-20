# Pull base image
FROM python:latest
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code
WORKDIR /code/
COPY . /code/
RUN apt update
RUN apt install libgl1-mesa-glx -y
RUN apt install libglib2.0-0 -y
RUN pip install -r requirements.txt

CMD ["python", "main.py"]

# 빌드 방법
# docker build -t test .