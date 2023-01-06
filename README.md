# date-range-merge

Merge only when *DATE* in one dataset lies between a RANGE (*STARTDT*, *ENDDT*) in the second dataset

***

## Description

*Get the python code [here](https://raw.githubusercontent.com/algorithmbasics/date-range-merge/main/date-range-merge.py)*.

*Get the R code [here](https://raw.githubusercontent.com/algorithmbasics/date-range-merge/main/date-range-merge.R)*.

### 

Let's assume that there are two datasets stored in CSV files named **dataset1.csv** and **dataset2.csv**. The first CSV file **dataset1.csv** contain the variable *DATE* is imported to a dataset *df1* and the second CSV file **dataset2.csv** contains the variables *STARTDT* and *ENDDT* is imported to a dataset *df2*.

The code first creates a new column called *key* in both datasets *df1* and *df2*, and then using this variable *key* for basis for the merge. The resulting merged dataset will have a row for every combination of rows in *df1* and *df2*, with *NaN* values for any missing columns.

After the merge, the code filters the merged dataset to include only rows where the *DATE* column in *df1* is between the *STARTDT* and *ENDDT* columns in *df2*. Finally, the *key* column is removed from the filtered dataset.


***
