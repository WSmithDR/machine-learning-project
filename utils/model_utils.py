import os
from joblib import dump, load
from typing import Any, Optional, List
from constants import models_dir, best_model_dir, optimized_model_dir


def save_model(model: Any, model_name: str, model_dir: str = models_dir) -> str:
    # Create models directory if it doesn't exist
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Ensure the model name has the .joblib extension
    if not model_name.endswith(".joblib"):
        model_name = f"{model_name}.joblib"

    # Create the full path
    model_path = os.path.join(model_dir, model_name)

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


def open_best_model() -> Any:
    # Get the only model file in the best_model directory
    model_files = [f for f in os.listdir(best_model_dir) if f.endswith(".joblib")]

    if not model_files:
        raise FileNotFoundError(f"No model file found in {best_model_dir}")

    if len(model_files) > 1:
        raise ValueError(
            f"Multiple model files found in {best_model_dir}. Expected only one."
        )

    # Create the full path to the model
    model_path = os.path.join(best_model_dir, model_files[0])

    # Load and return the model
    return load(model_path)


def save_best_model(model: Any, model_name: str) -> str:
    # Create best_model directory if it doesn't exist
    if not os.path.exists(best_model_dir):
        os.makedirs(best_model_dir)

    # Clear any existing models in the best_model directory
    for file in os.listdir(best_model_dir):
        if file.endswith(".joblib"):
            os.remove(os.path.join(best_model_dir, file))

    # Save the new best model
    return save_model(model, model_name, best_model_dir)


def open_optimized_model() -> Any:
    # Get the only model file in the optimized_model directory
    model_files = [f for f in os.listdir(optimized_model_dir) if f.endswith(".joblib")]

    if not model_files:
        raise FileNotFoundError(f"No model file found in {optimized_model_dir}")

    if len(model_files) > 1:
        raise ValueError(
            f"Multiple model files found in {optimized_model_dir}. Expected only one."
        )

    # Create the full path to the model
    model_path = os.path.join(optimized_model_dir, model_files[0])

    # Load and return the model
    return load(model_path)


def save_optimized_model(model: Any, model_name: str) -> str:
    # Create best_model directory if it doesn't exist
    if not os.path.exists(optimized_model_dir):
        os.makedirs(optimized_model_dir)

    # Clear any existing models in the best_model directory
    for file in os.listdir(best_model_dir):
        if file.endswith(".joblib"):
            os.remove(os.path.join(best_model_dir, file))

    # Save the new best model
    return save_model(model, model_name, best_model_dir)


def save_multiple_models(models: dict) -> List[str]:
    saved_paths = []
    for model_name, model in models.items():
        path = save_model(model, model_name)
        saved_paths.append(path)
    return saved_paths


def load_multiple_models(model_names: List[str]) -> dict:
    models = {}
    for model_name in model_names:
        models[model_name] = load_model(model_name)
    return models


def get_best_model_name():
    """Get the name of the best model from the best_model directory"""
    try:
        # Get the only model file in the best_model directory
        model_files = [f for f in os.listdir(best_model_dir) if f.endswith(".joblib")]

        if not model_files:
            return "unknown"

        if len(model_files) > 1:
            raise ValueError(
                f"Multiple model files found in {best_model_dir}. Expected only one."
            )

        # Return the model name without the .joblib extension
        return os.path.splitext(model_files[0])[0]

    except Exception:
        return "unknown"
