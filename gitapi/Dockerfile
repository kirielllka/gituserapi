FROM python:3.9-slim


WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip


COPY requirements.txt  .
RUN pip install --no-cache-dir  -r requirements.txt




ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0.8000"]