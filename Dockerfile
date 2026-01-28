FROM python:3.11-slim

# RAMni tejash uchun Python sozlamalari
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONOPTIMIZE=1

WORKDIR /app
COPY . /app

# Keshsiz o'rnatish (Disk va RAM tejash)
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "simplebot.py"]