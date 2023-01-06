import pandas as pd

# Load the two datasets
df1 = pd.read_csv('dataset1.csv')
df2 = pd.read_csv('dataset2.csv')

# Create a new column in df1 called 'key' that will be used as the key for the merge
df1['key'] = 1

# Create a new column in df2 called 'key' that will be used as the key for the merge
df2['key'] = 1

# Merge the two datasets using a left join
merged_df = pd.merge(df1, df2, how='left', on='key')

# Filter the merged dataset to include only rows where DATE is between STARTDT and ENDDT
filtered_df = merged_df[(merged_df['DATE'] >= merged_df['STARTDT']) & (merged_df['DATE'] <= merged_df['ENDDT'])]

# Drop the 'key' column from the filtered dataset
filtered_df = filtered_df.drop(columns=['key'])

# Print the resulting merged and filtered dataset
print(filtered_df)