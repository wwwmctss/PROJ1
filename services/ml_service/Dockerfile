FROM python:3.10-slim

COPY . /ml_service

VOLUME /models

WORKDIR /ml_service

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

ENV MODEL_PATH=/models/model.pkl

# Сборка
# docker build . -t mobile-price-service:1

# Запуск
# docker run --name mobile-price-container -p 8000:8000 -v $(pwd)/../models:/models mobile-price-service:1

# Удаление
# docker stop mobile-price-container 2>/dev/null || true
# docker rm mobile-price-container 2>/dev/null || true

# docker stop mobile-price-container
# docker rm mobile-price-container