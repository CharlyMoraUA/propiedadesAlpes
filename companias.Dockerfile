FROM python:3.10

EXPOSE 5002/tcp

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install requests
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/companias ./src/companias

CMD [ "flask", "--app", "./src/companias/api", "run", "--host=0.0.0.0"]