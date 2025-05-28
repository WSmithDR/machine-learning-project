import pandas as pd
from constants.directories import separated_dir

X_val = pd.read_csv(f"{separated_dir}/X_val.csv")
X_train = pd.read_csv(f"{separated_dir}/X_train.csv")
y_val = pd.read_csv(f"{separated_dir}/y_val.csv")
y_train = pd.read_csv(f"{separated_dir}/y_train.csv")
X_test = pd.read_csv(f"{separated_dir}/X_test.csv")
