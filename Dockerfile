FROM python:3.11

WORKDIR /llm_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY llm_app .

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "run:app"]