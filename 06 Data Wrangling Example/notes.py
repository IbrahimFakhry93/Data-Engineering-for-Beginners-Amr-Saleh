#
#! 77. Introducing a real-world Data Wrangling Challenge at Kiwilytics


# * We receive from client dataset: order of information

# * it contains problems:
# * Dates as strings
# * Null values


# * - Load the dataset into a DataFrame
# * - Inspect the raw data
# * - Clean invalid entries and handle missing values
# * - Engineer new features such as delivery time and shipping type
# * - Standardize the format for reporting and aggregation
# * - Export a clean version as csv for analysis and client report

# *===============================================================================================

#! 78. Loading and inspecting row data for the Wrangling done Problem

# * 1)reading csv file: pd.read_csv()
# ^  csv file can be file system or csv bucket if it's on cloud
# ^  csv file must be in the same directory of the executing file
# ^  or place the full directory path

# * 2) explore -> sample of dataframe: df.head()
# * 3) summary for the columns: df.info()
# ^   check number of entries and compare it with non-null count per column

# * 4) check no of null (missing values) for each data set: df.isna().sum()

# * 5) check no of shipment orders for each of shipping companies
# ^ check no of shipping order for each of shipping companies
# *    df['ShippingCompany'].value_counts()
# *    value_counts: counts the repeating times of a unique value in a certain column
# *    value_counts → shows the frequency of each distinct entry in a column.
# *    value_counts: returns how often each unique value appears in a column

# * 6) Check number of rows in dataframe
print(len(df))  #! “How many rows are in my DataFrame?”

# *===============================================================================================

#! 79. Data Cleaning for Wrangling Problem

# & Data Problems:
# ^ 1) Convert string Dates to actual dates
# * when uploading data in a csv
# * dates convert to string

# * if some string dates failed to be converted to actual dates

# ~ so we have to handle the error:
# ~  Convert dates (Error Types: #coerce # ignore #raise)
# * raise an error
# ? or:
# * ignore the error
# ? or:
# * coerce (remove value and replace it by nat: not a time)

# * pd.to_datetime() → converts the column into proper datetime objects.
# * errors='coerce' → replaces invalid entries like "not_a_date" with NaT (null datetime).

df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
# print(df['OrderDate'].dtype)
# print('\n')

df["ShippedDate"] = pd.to_datetime(df["ShippedDate"], errors="coerce")
# print(df['ShippedDate'].dtype)

# ^ 2) Handling Shipping cost
# * convert string to numbers
df["ShippingCost"] = pd.to_numeric(df["ShippingCost"], errors="coerce")
# ? verify
print(df["ShippingCost"].dtype)

# * Anything neg, replace it by nan
df.loc[df["ShippingCost"] < 1, "ShippingCost"] = np.nan
print("\n")

# * if there's invalid entry number (for ex. a letter inside the number)
# * we replace it by avg
df['ShippingCost'] = df['ShippingCost'].fillna(df['ShippingCost'].median())

# ^ 3) Handling null for columns:
# * There is no fixed rule, it depends on client requirement the use case
# ? example:
# * if current order id is null, assume the previous order id is the current order id
#~ Handle nulls
df['OrderID']=df['OrderID'].fillna(method='ffill')
#? or: because method ='ffill' is deprecated
df['OrderID']=df['OrderID'].ffill()
#* .ffill() = forward fill.
#* It takes the last non‑missing value and propagates it forward to fill any NaN (missing) values.

#? verify (the effect took place):
print(df['OrderID'].isna().sum())

# * if customer id is null, replace by unknown
df['CustomerID']=df['CustomerID'].fillna('unknown')
#? verify:
print(df['CustomerID'].isna().sum())

# * if ship city is null, replace by unspecified
df['ShipCity']=df['ShipCity'].fillna('unspecified')
#? verify:
print(df['ShipCity'].isna().sum())

# ^ 4) Standardize Column Names: (useful for grouping)
# * Ship country: remove leading or preceding space or tab, .strip()
df['ShipCountry'] = df['ShipCountry'].str.strip().str.title()
# * Format (capital letters): .title()
# * ship city: same above
# * Ship company : no need for title

# print(df.head())

df["ShippingCost"] = df["ShippingCost"].fillna(df["ShippingCost"].median())

# * to verify:
print(df["ShippingCost"].isna().sum())  #! should be zero

# ^ 5)  Drop rows where both dates are missing

df = df[~(df["OrderDate"].isna() & df["ShippedDate"].isna())]

# * df['OrderDate'].isna() → True where OrderDate is missing.

# * df['ShippedDate'].isna() → True where ShippedDate is missing.

# & → logical AND → True only where both are missing.

# ~(...) → flips it → True where NOT both missing.

# * df[...] → keeps only rows where the condition is True.

# ^ ✅ Meaning in plain words
# * This line removes rows where both OrderDate and ShippedDate are missing.
# * If at least one of them is present, the row is kept.
# * If both are NaN, the row is dropped.

print(len(df))  #! “How many rows are in my DataFrame?”

# ^ 6) Specific Case:
# * We have set of shipping companies, created by kiwilytics in different countries
# * with different names but all contain (kiwilytics) so we need standarad name for grouping

df.loc[
    df["ShippingCompany"].str.contains("Kiwilytics", na=False), "ShippingCompany"
] = "Kiwilytics Goods Shipping LLC."

#* .loc[rows, cols] lets you target only the ShippingCompany column in those rows.
#* This safely updates just that column, leaving the rest of the row intact.

``
#! wrong approach when not using loc, (data corruption)

df[df["ShippingCompany"].str.contains("Kiwilytics", na=False)] = (
    '"Kiwilytics Goods Shipping LLC."'
)
#* df[...] here is selecting rows where the condition is True.
#* Then you assign 'UPS Limited' to the entire row, not just the ShippingCompany column.
#* That means every column in those rows will be overwritten with 'UPS Limited'.
#* This is usually not what you want — it corrupts your data.

#& Important:
#* Always take copy of your data before execute uncertain statement 
#^  df_correct = df.copy()

# *===============================================================================================

#! Feature Engineering:

#* Extracts new fields and insights
#* we want to know number of late orders
#* and number of on time orders
#* assuming delivery time should be 15 days

#? Days between order and shipment
df["deliveryTime"] = df["ShippedDate"] - df["OrderDate"]
df['DeliveryDays'] = (df['ShippedDate'] - df['OrderDate']).dt.days  # will be in float

#* deliveryTime → full timedelta object (keeps precision, can show “12 days 05:30:00”).

#* DeliveryDays → just the numerical (float) count of days (no hours/minutes).


#^ Flags
def get_status(x):
    if pd.isna(x):
        return "Unknown"
    elif x > 15:
        return "Late"
    else:
        return "OnTime"

df['DeliveryStatus'] = df['DeliveryDays'].apply(get_status)

#^ Domestic vs International


def check_domestic(country):
    if country in domestic_countries:
        return "Yes"
    else:
        return "No"

domestic_countries = ["Germany"]

df['IsDomestic'] = df['ShipCountry'].apply(check_domestic)

df.head()

#^ Customer Loyalty

def isRegular(x):
    if pd.isna(x):
     return 'Unknown'
    if x >=9:
     return 'Regular Customer'
    else:
     return 'Normal Customer'
 
df['Customer Loyalty'] = df.groupby('CustomerID')['OrderID'].transform('count').apply(isRegular)
print('\n')
df.head()

# *===============================================================================================

#! 82. Grouping Data for Wrangling Problem

#^ Calculate average shipping cost by a shipping company

avg_shipping_by_company = df.groupby("ShippingCompany")['ShippingCost'].mean()
print("📊 Avg Shipping Cost by Company:")
print(avg_shipping_by_company)

#*===============================================================================================
#! 83. Export Data and Reporting for Wrangling Problem

df.to_csv("cleaned_orders_final.csv)",index=False)

# Final summary
print("\n✅ Final Dataset Snapshot:")
print(df.head())

print("\n📈 Delivery Status Breakdown:")
print(df['DeliveryStatus'].value_counts())


print("\n🌎 Orders by Country:")
print(df['ShipCountry'].value_counts())

print("\n🌎 Orders by City:")
print(df['ShipCity'].value_counts())

#^====================================================

print("\n📦 Top 3 Shipping Companies:")

print(df['ShippingCompany'].value_counts().head(3))

#* no_ship_comp = df['ShippingCompany'].value_counts()
 df['ShippingCompany']  #* → selects the column with shipping company names.

#* .value_counts() → counts how many times each unique company appears.

#* Result: a Series showing frequency of orders handled by each shipping company.

#? ✅ Business interpretation
# ^This expresses market share of shipping companies in your dataset:

# *Which shipping company is used most often.

# *Relative workload distribution among carriers.

# *Potential dependency on one provider (risk if they fail).

# *Opportunities to negotiate better rates with high‑volume partners.