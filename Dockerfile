FROM python:3

COPY ["requirements.txt", "/usr/src/"]

WORKDIR /usr/src

RUN pip install --no-cache-dir -r requirements.txt

COPY [".", "/usr/src/"]

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["python", "./Backend/app.py"]