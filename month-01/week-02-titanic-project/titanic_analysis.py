import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset directly from the URL
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_df = pd.read_csv(url)

# --- Your task starts here ---

# 1. Print the first 5 rows of the dataframe
# print(titanic_df.head())
# 2. Print a concise summary of the dataframe (info)
# print(titanic_df.info())
# 3. Print the basic statistical details of the numerical columns
# print(titanic_df.describe())

avg_age = titanic_df['Age'].median()
titanic_df['Age'] = titanic_df['Age'].fillna(avg_age)

avg_surv_rate_by_sex = titanic_df.groupby('Sex')['Survived'].mean()
# print(avg_surv_rate_by_sex)

avg_surv_rate_by_class = titanic_df.groupby('Pclass')['Survived'].mean()
# print(avg_surv_rate_by_class)

plt.figure(figsize=(12, 4))

plt.subplot(2, 2, 1)
# plt.bar(titanic_df['Sex'].unique(), avg_surv_rate_by_sex)
avg_surv_rate_by_sex.plot(kind='bar')
plt.xlabel("Gender")
plt.ylabel("Survival Rate")
plt.title("Survival Rate by Gender")

plt.subplot(2, 2, 2)
# plt.bar(titanic_df['Pclass'].unique(), avg_surv_rate_by_class)
avg_surv_rate_by_class.plot(kind='bar')
plt.xlabel("Passanger Class")
plt.ylabel("Survival Rate")
plt.title("Survival Rate by Passanger Class")

plt.subplot(2, 2, (3, 4))
plt.hist(titanic_df['Age'], bins=20, edgecolor='black')
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.title("Age Distribution of Passengers")

plt.tight_layout()
plt.show()