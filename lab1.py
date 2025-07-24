import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# import dataset
df = pd.read_csv(r"C:\Users\meher\Downloads\titanic.csv")

print(df.head()) # print first five records 
print(df.shape)            # print no of Rows & Columns
print(df.columns)         # print all Column names
print(df.info())          # print Data types and null values
print(df.describe())      # Summary statistics


# Step 4: Handle Missing Data
print(df.isnull().sum())  # Count missing values



# Example: Fill missing 'Age' with mean
df['Age'].fillna(df['Age'].mean(), inplace=True)



# Drop rows with missing 'Embarked'
df.dropna(subset=['Embarked'], inplace=True)




#Step 5: Analyze the Data
print(df['Survived'].value_counts())
print(df['Pclass'].value_counts())


#Plot survival count:
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()

#Histogram of Age:
plt.hist(df['Age'], bins=30, color='skyblue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

