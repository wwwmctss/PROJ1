#!/bin/bash
mlflow server --backend-store-uri sqlite:///mlruns.db --host 127.0.0.1 --port 5000
