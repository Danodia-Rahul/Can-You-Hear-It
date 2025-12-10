FROM python:3.14-slim-bookworm

WORKDIR /app

COPY app.py /app/app.py

RUN pip3 install streamlit

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

