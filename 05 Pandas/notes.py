import numpy as np
import pandas as pd


#

#! 68. Introduction to Pandas

# ^ look up the slides

#! 69. Import Pandas and Create DataFrame and Series

# & Pandas Series and DataFrames Basics

# ^ Series is close to list
# ^ DateFrame is close to table  (most common when dealing with data)

import numpy as np
import pandas as pd

# ~ Series: Revenue over months
monthly_revenue = pd.Series([30000, 50000, 45000, np.nan, 60000], name="Revenue")
print("🔹 Monthly Revenue Series:\n", monthly_revenue, "\n")

# ~ DataFrame: Employees at different firms
data = {
    "Employee": ["Youssef", "Toka", "Abdelrahman", "Maher"],
    "Company": ["Kiwilytics", "PwC", "EY", "KPMG"],
    "Experience_Years": [5, 7, 3, 9],
}

df = pd.DataFrame(data)

print("🔹 DataFrame Example:\n", df)

# & Pandas Essentials: Series vs DataFrame
# ^ Business Logic:
# * - Track monthly revenue (some months missing data → NaN).
# * - Represent employees at different companies with their years of experience.

# ? Key Rule:
# * - pd.Series() → receives a LIST (1D data) + optional argument name
# * - pd.DataFrame() → receives a DICTIONARY (keys = column names, values = lists of column data)

# ^ Import libraries
import numpy as np
import pandas as pd

# ^ Create a Series (1D data)
# * - Input: list of values
# * - Argument: name="..." gives the Series a label
monthly_revenue = pd.Series([30000, 50000, 45000, np.nan, 60000], name="Revenue")

# ^ Create a DataFrame (2D table)
# * - Input: dictionary
# *   Keys   → column names
# *   Values → lists of column data (all lists must be same length)
data = {
    "Employee": ["Youssef", "Toka", "Abdelrahman", "Maher"],
    "Company": ["Kiwilytics", "PwC", "EY", "KPMG"],
    "Experience_Years": [5, 7, 3, 9],
}

df = pd.DataFrame(data)

# * Print DataFrame
print("🔹 DataFrame Example:\n", df)


# *======================================================================================================

#! 70. Inspect and Explore Dataframe
# * First thing we do once we receive new data problem or file,
# * we start to inspect how we will execute data cleansing
# * the size of file, column names, how many null rows or null columns

# ^ we execute set of commands to explore our data frame

# ^ show (by default) top 5 rows:
# * df.head()

# ^ to get last 5 rows:
# * use tail instead of head
# *  df.tail()

# ? First five rows
print("🔹 First 5 Rows:")
print(df.head())

# ? Last five rows

print("\n🔹 Last 5 Rows:")
print(df.tail())
# &===========================================================================================
# ^ info command
# ^ how many rows,columns, how many null, data types, memory usage
# * df.info()

# ~ Info summary
print("\n📋 DataFrame Info:")
df.info()
# &===========================================================================================
# ^ describe command
# * df. describe command

# ~ Describe numerical columns
#! min,max,mean
print("\n📊 Summary Statistics:")
df.describe()

# &===========================================================================================

# ^ deal with null:

# & Handling Missing Data in Pandas

# ? Business Logic:
# * - In real datasets, some values may be missing (NaN).
# * - We often need to check how many nulls each column has before cleaning.

# * df.isna() → returns a DataFrame of True/False (True = value is NaN)
# * df.isna().sum() → counts how many NaN values per column

# * df.isna().sum()

# ~ Check if any values are missing
print("\n🚨 Missing Values Per Column:")
print(df.isna().sum())

# &===========================================================================================

# ^ to display all table entries
# * df.isna()

# ~ View full matrix of missing positions
print("\n🧼 Matrix of Missing Values:")
print(df.isna())

# *=================================================================

#! 71. Simulating a Null

# & Simulate a missing experience value

# ^ set a value in dataframe to be null

# * - Sometimes you need to mark a value as missing (NaN).
# ~ - Example: Employee at row index 1 has unknown experience years.

# ^ df.loc[row_index, "ColumnName"] = np.nan

# * - loc[] → label-based indexing (row, column)
# * - np.nan → represents a missing value (Not a Number)

df.loc[1, "Experience_Years"] = np.nan
print(df, "\n")

# & Re-run missing value check
# ^ display number of nulls in each column
# * df.isna().sum()

print("\n🚨 After introducing missing data:")
print(df.isna().sum())


# & Drop rows with missing data
# ^ drop row with null or missing values (just a display, won't change original df)
# * df.dropna()

print("\n🧹 After dropping missing rows:")


# *===================================================================

#! 72. Selecting and Filtering Dataframes

# ^ Re-initialize the DataFrame to its original clean state

data = {
    "Employee": ["Youssef", "Toka", "Abdelrahman", "Maher"],
    "Company": ["Kiwilytics", "PwC", "EY", "KPMG"],
    "Experience_Years": [5, 7, 3, 9],
}

df = pd.DataFrame(data)

# ? Optional preview
print("✅ DataFrame Reset:")
print(df)

# * in real world, we deal with big size dataframes
# * no of columns can be in hundreds and thousands, especially, if we have big memory in the working server

# ^ Selecting columns
print("🔸 Company Column:\n", df["Company"], "\n")

# ~ print("🔸 Name & Experience:\n",  ,"\n")
print("🔸 Company Column:\n", df[["Employee", "Experience_Years"]], "\n")

# ^ Selecting rows
print("🔸 Row by label (loc):\n", df.loc[2], "\n")
print("🔸 Row by position (iloc):\n", df.iloc[2], "\n")

# ^ Filtering: Employees with more than 5 years
print("🔸 Experienced Employees:\n", df[df["Experience_Years"] > 5], "\n")

# ^ Filter: Working at Kiwilytics
print("🔸 Kiwilytics Team:\n", df[df["Company"] == "Kiwilytics"], "\n")

# *=========================================================================================

#! 73. Standardize Dataframe and Add Columns

# & Modifying DataFrames and Adding Columns

# ^ Standardize company names

df["Company"] = df[
    "Company"
].str.upper()  # ~ transform column values to upper case and replace the old values
print("🔹 Standardized Company Names:\n", df, "\n")

# ^ Add a seniority flag (add new column)
df["Is_Very_Senior"] = df["Experience_Years"] >= 8
print("🔹 With Seniority Flag:\n", df, "\n")

# *=========================================================================================

#! Handling Missing Data

# ^ Create dataset of project budgets
df_projects = pd.DataFrame(
    {
        "Client": ["Kiwilytics", "PwC", "EY", "KPMG", "McKinsey"],
        "Budget_kUSD": [120, 200, np.nan, 150, None],
    }
)
print("🔸 Original Budgets:\n", df_projects, "\n")

# ^ Fill missing budgets with mean values using (  .fillna(mean_value)  )

# ~ calculate mean of the column
# ~ access column by dataframe_name["col name"] then apply mean function on column set
mean_budget = df_projects["Budget_kUSD"].mean()
print(mean_budget)

df_projects["Budget_kUSD"] = df_projects["Budget_kUSD"].fillna(mean_budget)

print("🔹 After Filling Missing Budgets:\n", df_projects, "\n")

# *=========================================================================================

#! Grouping & Aggregating DataFrames

# ^ note: can be done by sql too

# ^ Revenue per company per quarter
df_revenue = pd.DataFrame(
    {
        "Company": ["Kiwilytics", "PwC", "EY", "KPMG", "Kiwilytics", "PwC"],
        "Quarter": ["Q1", "Q1", "Q1", "Q1", "Q2", "Q2"],
        "Revenue_kUSD": [120, 200, 180, 150, 130, 210],
    }
)

print(df_revenue)

grouped = df_revenue.groupby("Company")["Revenue_kUSD"].sum()

print("📊 Total Revenue by Company:\n", grouped, "\n")

# *=========================================================================================

#! Merging DataFrames

# ^ note: can be done by sql too (join)

# ^ Merge project managers and projects
df_managers = pd.DataFrame(
    {"ManagerID": [1, 2, 3], "Name": ["Ibrahim", "Maher", "Abdelrahman"]}
)

print(df_managers)

df_projects = pd.DataFrame(
    {
        "ProjectID": [101, 102, 103],
        "ManagerID": [1, 2, 2],
        "Client": ["Kiwilytics", "PwC", "EY"],
    }
)
print(df_projects)

merged_df = pd.merge(df_managers, df_projects, on="ManagerID", how="inner")
print("🔗 Merged Managers & Projects:\n", merged_df, "\n")
