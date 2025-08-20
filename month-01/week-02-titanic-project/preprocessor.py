import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset directly from the URL
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_df = pd.read_csv(url)

avg_age = titanic_df['Age'].median()
titanic_df['Age'] = titanic_df['Age'].fillna(avg_age)

gender_mapping = {'male': 0, 'female': 1}
titanic_df['Sex'] = titanic_df['Sex'].map(gender_mapping)

titanic_df = pd.get_dummies(titanic_df, columns=['Embarked'], dtype=int)

titanic_df = titanic_df.drop(columns=['Name', 'PassengerId', 'Ticket', 'Cabin'])

print(titanic_df.head())
print(titanic_df.info())