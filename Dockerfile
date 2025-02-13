FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

RUN playwright install

RUN pytest -v -s --alluredir

CMD ["allure", "server", "results"]