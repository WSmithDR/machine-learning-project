import pandas as pd
from constants.directories import converted_dir

df_test = pd.read_csv(f"{converted_dir}/vehiculos_test.csv")
df_train = pd.read_csv(f"{converted_dir}/vehiculos_train.csv")
