FROM python:3.10

EXPOSE 5004/tcp

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install requests
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/propiedades ./src/propiedades

CMD [ "flask", "--app", "./src/propiedades/api", "run", "--host=0.0.0.0"]