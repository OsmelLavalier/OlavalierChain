FROM python:3

WORKDIR /holychain

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /holychain/
CMD [ "python", "main.py" ]
