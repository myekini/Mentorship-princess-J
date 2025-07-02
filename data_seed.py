import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Sample data
data = {
    'CustomerID': np.arange(1, 21),  # 20 customers
    'Name': [
        'Alice', 'Bob', 'Charlie', 'David', 'Eva',
        'Frank', 'Grace', 'Helen', 'Ian', 'Jane',
        'Kyle', 'Laura', 'Mike', 'Nina', 'Owen',
        'Paula', 'Quinn', 'Rachel', 'Steve', 'Tina'
    ],
    'Age': np.random.choice([25, 30, 35, 40, np.nan], size=20),
    'Gender': np.random.choice(['Male', 'Female'], size=20),
    'Department': np.random.choice(['HR', 'IT', 'Finance'], size=20),
    'Salary': np.random.randint(40000, 90000, size=20)
}

df = pd.DataFrame(data)

# Introduce some duplicate rows
duplicates = df.iloc[5:8].copy()
df = pd.concat([df, duplicates], ignore_index=True)

# Introduce some more missing values
df.loc[3, 'Department'] = np.nan
df.loc[7, 'Salary'] = np.nan

# Save to CSV
df.to_csv('sample_data.csv', index=False)

print("✅ Sample dataset 'sample_data.csv' created!")
