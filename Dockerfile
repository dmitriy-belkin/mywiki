FROM python:3.13

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN make html

CMD ["python", "-m", "http.server", "--directory", "build/html", "8000"]
