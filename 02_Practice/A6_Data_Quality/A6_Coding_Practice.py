# A6: Data Quality — Coding Practice

import pandas as pd

# 1. Create a sample dataset
data = {
    "Name": ["Aman", "Rahul", "Chandan", "Aman"],
    "Age": [20, 21, None, 20],
    "Marks": [85, 90, 75, 85]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# 2. Check dataset shape
print("\nDataset Shape:")
print(df.shape)

# 3. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 5. Remove duplicate rows
df = df.drop_duplicates()

print("\nDataset After Removing Duplicates:")
print(df)

# 6. Fill missing age with the mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nDataset After Filling Missing Values:")
print(df)

# 7. Check data types
print("\nData Types:")
print(df.dtypes)

# 8. Check basic statistics
print("\nBasic Statistics:")
print(df.describe())