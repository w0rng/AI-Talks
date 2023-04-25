FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/

CMD ["streamlit", "run", "--server.address", "0.0.0.0", "chat.py"]
