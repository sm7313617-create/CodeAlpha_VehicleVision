import pandas as pd

df = pd.read_csv('data/car_data.csv')
df['Car_Age'] = 2024 - df['Year']
df = df.drop('Car_Name', axis=1)
df = pd.get_dummies(df, drop_first=True)
X = df.drop('Selling_Price', axis=1)

print('Feature columns in training order:')
print(X.columns.tolist())
print(f'\nTotal features: {len(X.columns)}')
