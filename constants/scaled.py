import pandas as pd
from constants.directories import scaled_dir

X_test_scaled = pd.read_csv(f"{scaled_dir}/X_test.csv")


X_val_scaled = pd.read_csv(f"{scaled_dir}/X_val.csv")
X_train_scaled = pd.read_csv(f"{scaled_dir}/X_train.csv")
y_val_scaled = pd.read_csv(f"{scaled_dir}/y_val.csv")
y_train_scaled = pd.read_csv(f"{scaled_dir}/y_train.csv")
