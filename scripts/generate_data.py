import pandas as pd
import numpy as np

df = pd.DataFrame({
    "feature": np.random.randn(100)
})

df.to_csv("data/reference.csv", index=False)
df2 = pd.DataFrame({
    "feature": np.random.randn(100) + 1
})
df2.to_csv("data/current.csv", index=False)