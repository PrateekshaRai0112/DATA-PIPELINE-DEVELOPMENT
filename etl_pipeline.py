import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Step 1: Extract - Load the data
data = pd.read_csv('data.csv')
print("📥 Extracted Data:\n", data.head())

# Step 2: Transform

# Handle missing values
age_imputer = SimpleImputer(strategy='mean')
data['Age'] = age_imputer.fit_transform(data[['Age']])

salary_imputer = SimpleImputer(strategy='mean')
data['Salary'] = salary_imputer.fit_transform(data[['Salary']])

# Encode categorical variables
gender_encoder = LabelEncoder()
data['Gender'] = gender_encoder.fit_transform(data['Gender'].astype(str))

purchase_encoder = LabelEncoder()
data['Purchased'] = purchase_encoder.fit_transform(data['Purchased'].astype(str))

# Scale numerical features
scaler = StandardScaler()
data[['Age', 'Salary']] = scaler.fit_transform(data[['Age', 'Salary']])

print("\n🔧 Transformed Data:\n", data.head())

# Step 3: Load - Save the processed data
data.to_csv('processed_output.csv', index=False)
print("\n✅ Data pipeline complete. Output saved as 'processed_output.csv'")

