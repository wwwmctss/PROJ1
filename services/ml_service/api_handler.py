import os
import cloudpickle
import pandas as pd

class FastAPIHandler:
    def __init__(self, model_path: str | None = None):
        self.model_path = model_path or os.getenv("MODEL_PATH", "../models/model.pkl")
        with open(self.model_path, "rb") as f:
            self.model = cloudpickle.load(f)

    def predict(self, data: dict) -> int:
        df = pd.DataFrame([data])
        return int(self.model.predict(df)[0])