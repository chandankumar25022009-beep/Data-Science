
# A7: Data Cleaning — Coding Practice

import pandas as pd

# 1. Create a dataset with data-quality issues
data = {
    "Name": [" Aman ", "Rahul", "Chandan", "Aman", "Rahul"],
    "Age": [20, 21, None, 20, 21],
    "Marks": [85, 90, 75, 85, 90],
    "City": ["Meerut", "Delhi", "Agra", "Meerut", "Delhi"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# 2. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Clean text BEFORE removing duplicates
df["Name"] = df["Name"].str.strip()
df["City"] = df["City"].str.strip().str.title()

print("\nAfter Standardizing Text:")
print(df)

# 4. Remove duplicate rows
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

# 5. Fill missing ages with the mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nAfter Filling Missing Ages:")
print(df)

# 6. Display final dataset information
print("\nFinal Dataset Information:")
df.info()

print("\nFinal Dataset:")
print(df)

# 7. Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved as cleaned_data.csv")
