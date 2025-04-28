import os
from joblib import dump, load
from typing import Any, Optional, List
from constants import models_dir


def save_model(model: Any, model_name: str) -> str:
    # Create models directory if it doesn't exist
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)

    # Ensure the model name has the .joblib extension
    if not model_name.endswith(".joblib"):
        model_name = f"{model_name}.joblib"

    # Create the full path
    model_path = os.path.join(models_dir, model_name)

    # Save the model
    dump(model, model_path)

    return model_path


def load_model(model_name: str) -> Any:
    # Ensure the model name has the .joblib extension
    if not model_name.endswith(".joblib"):
        model_name = f"{model_name}.joblib"

    # Create the full path
    model_path = os.path.join(models_dir, model_name)

    # Check if model exists
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")

    # Load and return the model
    return load(model_path)


def save_multiple_models(models: dict) -> List[str]:
    saved_paths = []
    for model_name, model in models.items():
        path = save_model(model, model_name, models_dir)
        saved_paths.append(path)
    return saved_paths


def load_multiple_models(model_names: List[str]) -> dict:
    models = {}
    for model_name in model_names:
        models[model_name] = load_model(model_name, models_dir)
    return models
