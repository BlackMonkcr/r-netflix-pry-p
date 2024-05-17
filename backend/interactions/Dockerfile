FROM python:3-slim
WORKDIR /programas/api_interactions
COPY requirements.txt . 
RUN pip3 install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]