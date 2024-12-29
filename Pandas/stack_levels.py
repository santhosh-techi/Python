import pandas as pd
df = pd.DataFrame({
    ('2023', 'Q1', 'Sales'): [100, 150, 120],
    ('2023', 'Q1', 'Expenses'): [50, 60, 55],
    ('2023', 'Q2', 'Sales'): [130, 180, 140],
    ('2023', 'Q2', 'Expenses'): [60, 70, 65],
})
print(df.stack(level=2))