import numpy as np
import pandas as pd

# * Series: Revenue over months
monthly_revenue = pd.Series([30000, 50000, 45000, np.nan, 60000], name="Revenue")

print("🔹 Monthly Revenue Series:\n", monthly_revenue, "\n")

# ^ DataFrame: Employees at different firms
data = {
    "Employee": ["Youssef", "Toka", "Abdelrahman", "Maher"],
    "Company": ["Kiwilytics", "PwC", "EY", "KPMG"],
    "Experience_Years": [5, 7, 3, 9],
}

df = pd.DataFrame(data)

print("🔹 DataFrame Example:\n", df)

# *=================================================================================================
