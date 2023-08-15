FROM python:3.11

WORKDIR /code

COPY ./Pipfile ./Pipfile.lock /code

RUN pip install --upgrade pipenv \
    && pipenv requirements > /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

ENTRYPOINT ["uvicorn"]
CMD ["app.main:app", "--host", "0.0.0.0", "--port", "8000"]