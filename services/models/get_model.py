import os
import cloudpickle
import mlflow
import mlflow.sklearn

MLFLOW_URI = "http://127.0.0.1:5000"
RUN_ID = "e7abb0fb22744d8c9724d5716e591657"
MODEL_ARTIFACT_PATH = "models"
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

mlflow.set_tracking_uri(MLFLOW_URI)
mlflow.set_registry_uri(MLFLOW_URI)

model = mlflow.sklearn.load_model(f"runs:/{RUN_ID}/{MODEL_ARTIFACT_PATH}")

with open(OUTPUT_PATH, "wb") as f:
    cloudpickle.dump(model, f)

print(f"Модель сохранена в {OUTPUT_PATH}")
print(f"Размер файла: {os.path.getsize(OUTPUT_PATH)} байт")