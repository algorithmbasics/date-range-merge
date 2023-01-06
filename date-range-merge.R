# Load the two datasets
df1 <- read.csv("dataset1.csv")
df2 <- read.csv("dataset2.csv")

df1$key = 1
df2$key = 1

# Merge the two datasets using a left join
merged_df <- merge(df1, df2, by.x="key", by.y="key", all.x=TRUE)

# Filter the merged dataset to include only rows where DATE is between STARTDT and ENDDT
filtered_df <- merged_df[merged_df$DATE >= merged_df$STARTDT & merged_df$DATE <= merged_df$ENDDT, ]

# Print the resulting merged and filtered dataset
print(filtered_df)