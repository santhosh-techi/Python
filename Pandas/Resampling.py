import pandas as pd

# Sample DataFrame with daily data
data = {'date': pd.date_range('2024-01-01', periods=6, freq='D'),
        'value': [10, 20, 30, 40, 50, 60]}
df = pd.DataFrame(data)
print(df)
df.set_index('date', inplace=True)

# Downsampling to monthly data, taking the sum
monthly_data = df.resample('Y').min()
print(monthly_data)

# Upsampling to hourly data, filling missing values with forward fill
hourly_data = df.resample('Y').ffill()  # forward fill missing values
print(hourly_data)
