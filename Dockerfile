FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./ai_talks /app/

CMD ["streamlit", "run", "--server.address", "0.0.0.0", "chat.py"]
