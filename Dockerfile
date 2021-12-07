FROM python@sha256:428d6f9f06746ed3bcdf6e273cee6bf91d1a2978c157b0466b308e5b3bd12c7e

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . /

ENTRYPOINT ["python", "otp/cli.py"]