FROM python:2.7
COPY . /app
WORKDIR /app
COPY templates /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
