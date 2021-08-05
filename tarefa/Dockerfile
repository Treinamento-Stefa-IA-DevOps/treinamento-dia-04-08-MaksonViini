#FROM python:3.8-slim
FROM python:3.8-slim

COPY . /tarefa

WORKDIR /tarefa

RUN pip install fastapi uvicorn

EXPOSE 80

CMD ["uvicorn", "codigo.main:app","--host", "0.0.0.0", "--port", "80", "--reload"]
