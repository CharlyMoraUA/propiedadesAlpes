FROM python:3.10

EXPOSE 5003/tcp

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install requests
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/inquilinos ./src/inquilinos

CMD [ "flask", "--app", "./src/inquilinos/api", "run", "--host=0.0.0.0"]