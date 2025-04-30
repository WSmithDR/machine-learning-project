import pandas as pd
from constants.directories import initial_dir

df_test = pd.read_csv(f"{initial_dir}/vehiculos_test.csv")
df_train = pd.read_csv(f"{initial_dir}/vehiculos_train.csv")
