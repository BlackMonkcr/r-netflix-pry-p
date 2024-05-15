FROM python:3-slim
WORKDIR /programas/api_profiles
COPY requirements.txt . 
RUN pip3 install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "-p", "8001", "--host"]