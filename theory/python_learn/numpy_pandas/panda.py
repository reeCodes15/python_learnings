import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)
#
# # Selecting a column
print("\nColumn 'Name':")
print(df['Name'])

print("\nColumn 'Name':")
print(type(df['Name']))
print(type(df))


# Filtering rows based on condition
print("\nRows with Age > 30:")
print(df[df['Age'] > 30])
#
# # Adding a new column
df['Gender'] = ['F', 'M', 'M', 'M']
print("\nDataFrame with Added Column 'Gender':")
print(df)


sorted_df = df.sort_values(by='Age')
print('ssssss')
print(sorted_df)