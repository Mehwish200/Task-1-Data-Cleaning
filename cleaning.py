
import pandas as pd

# -------------------------------
# 1. Load Dataset
# -------------------------------
df =  df = pd.read_csv(r"C:\Users\Saqlain shaikh\Desktop\internship\Task1\dataset.csv")
      # <-- your dataset file
print("Original Shape:", df.shape)


# -------------------------------
# 2. Check Missing Values
# -------------------------------
print("\nMissing Values Before Cleaning:\n", df.isnull().sum())

# Fill numerical NaNs with median
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Fill categorical NaNs with mode
cat_cols = df.select_dtypes(include=['object']).columns
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])


# -------------------------------
# 3. Remove Duplicates
# -------------------------------
df.drop_duplicates(inplace=True)


# -------------------------------
# 4. Standardize Text Columns
# -------------------------------
for col in cat_cols:
    df[col] = df[col].astype(str).str.strip().str.title()


# -------------------------------
# 5. Fix Date Formats
# -------------------------------
date_cols = [col for col in df.columns if "date" in col.lower()]

for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce", dayfirst=True)


# -------------------------------
# 6. Clean Column Names
# -------------------------------
df.columns = (
    df.columns.str.strip()
              .str.lower()
              .str.replace(" ", "_")
)


# -------------------------------
# 7. Fix Data Types
# -------------------------------
for col in ["age", "income", "salary"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")


# -------------------------------
# 8. Save Cleaned Dataset
# -------------------------------
df.to_csv("cleaned_dataset.csv", index=False)
print("\nCleaned dataset saved as cleaned_dataset.csv")
print("Final Shape:", df.shape)

