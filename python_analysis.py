import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Dataset_2.csv")
print(df.head())

df.info()
print("Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

category_sales = df.groupby("Product_Category")["Total_Amount"].sum()
print("sales by product Category:")
print(category_sales)

country_sales = df.groupby("Country")["Total_Amount"].sum()
print("\nSales by Country:")
print(country_sales)


product_sales = df.groupby("products")["Total_Amount"].sum()
product_sales = product_sales.sort_values(ascending=False).head(10)
print("Top 10 Products by Sales:")
print(product_sales)


plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("sales by product category")
plt.xlabel("product category")
plt.ylabel("total sales")
plt.ticklabel_format(axis="y",style="plain")
plt.tight_layout()
plt.savefig("charts/sales_by_product_category.png", dpi=300, bbox_inches="tight")
plt.show()

payment_sales = df.groupby("Payment_Method")["Total_Amount"].sum()
print("sales by payment method:")
print(payment_sales)

plt.figure(figsize=(8,5))
payment_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("sales by payment method")
plt.xlabel("payment method")
plt.ylabel("total sales")
plt.ticklabel_format(axis="y",style="plain")
plt.tight_layout()
plt.savefig("Charts/sales_by_payment_method.png", dpi=300, bbox_inches="tight")
plt.show()

shipping_method_sales = df.groupby("Shipping_Method")["Total_Amount"].sum()
print("sales by shipping method:")
print(shipping_method_sales)

plt.figure(figsize=(8,5))
shipping_method_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("sales by shipping method")
plt.xlabel("shipping method")
plt.ylabel("total sales")
plt.ticklabel_format(axis="y",style="plain")
plt.tight_layout()
plt.savefig("Charts/sales_by_shipping_method.png", dpi=300, bbox_inches="tight")
plt.show()

gender_sales = df.groupby("Gender")["Total_Amount"].sum()
print("sales by gender:")
print(gender_sales)

plt.figure(figsize=(8,5))
gender_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("sales by gender")
plt.xlabel("gender")
plt.ylabel("total sales")
plt.ticklabel_format(axis="y",style="plain")
plt.tight_layout()
plt.savefig("Charts/sales_by_gender.png", dpi=300, bbox_inches="tight")
plt.show()


country_sales = df.groupby("Country")["Total_Amount"].sum()
country_sales.sort_values(ascending=False).head()
print("\nSales by Country:")
print(country_sales)

plt.figure(figsize=(8,5))
country_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("sales by country")
plt.xlabel("country")
plt.ylabel("total sales")
plt.ticklabel_format(axis="y",style="plain")
plt.tight_layout()
plt.savefig("Charts/sales_by_Country.png", dpi=300, bbox_inches="tight")
plt.show()

customer_spending = df.groupby("Customer_ID")["Total_Amount"].sum()
customer_spending = customer_spending.sort_values(ascending=False).head(10)
print("top 10 customer by Total spending:")
print(customer_spending)

plt.figure(figsize=(8,5))
customer_spending.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("top 10 customers by total spending")
plt.xlabel("customer id")
plt.ylabel("total spending")
plt.ticklabel_format(axis="y",style="plain")
plt.tight_layout()
plt.savefig("Charts/sales_by_customer_spending.png", dpi=300, bbox_inches="tight")
plt.show()

age_sales = df.groupby("Age")["Total_Amount"].sum()
age_sales = age_sales.sort_values(ascending=False).head(10)
print("top 10 age by total sales")
print(age_sales)

plt.figure(figsize=(9,6))
age_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("top 10 age by total sales")
plt.xlabel("age")
plt.ylabel("total sales")
plt.ticklabel_format(axis="y",style="plain")
plt.tight_layout()
plt.savefig("Charts/sales_by_age.png", dpi=300, bbox_inches="tight")
plt.show()


product_sales = df.groupby("products")["Total_Amount"].sum()
product_sales = product_sales.sort_values(ascending=False).head(10)
print("top 10 products by sales")
print(product_sales)

plt.figure(figsize=(12,6))
product_sales.sort_values().plot(kind="barh")
plt.xticks(rotation=0)
plt.title("top 10 products by sales")
plt.xlabel("Total sales")
plt.ylabel("products")
plt.ticklabel_format(axis="x",style="plain")
plt.tight_layout()
plt.savefig("Charts/sales_by_top_10_products.png", dpi=300, bbox_inches="tight")
plt.show()


print("\nMissing Values in Each Column")

missing_values = df.isnull().sum()
print(missing_values[missing_values > 0].sort_values(ascending=False))
print("\nMissing Value Percentage ---")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage[missing_percentage > 0].sort_values(ascending=False).round(2))


print(df.columns.tolist())


print("Missing Total_Amount:", df["Total_Amount"].isnull().sum())
print("Missing Amount:", df["Amount"].isnull().sum())
print("Missing Date:", df["Date"].isnull().sum())
print("Missing Transaction_ID:", df["Transaction_ID"].isnull().sum())

print("\nChecking Empty Values")
df = df.replace(r"^\s*$", np.nan, regex=True)
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])


print("\nChecking Duplicate Transactions")
print("Total duplicate rows:", df.duplicated().sum())
print("Duplicate Transaction IDs:", df["Transaction_ID"].duplicated().sum())

print("\nInvestigating Duplicate Transaction IDs")
duplicate_ids = df[df["Transaction_ID"].duplicated(keep=False)]
print("Total rows with repeated Transaction IDs:", len(duplicate_ids))
print(duplicate_ids[["Transaction_ID", "Customer_ID", "Date", "Total_Amount"]].head(20))

print("\nChecking Repeated Transaction IDs")
transaction_counts = df["Transaction_ID"].value_counts()
repeated_transactions = transaction_counts[transaction_counts > 1]
print("Number of unique transaction IDs repeated:", len(repeated_transactions))
print("\nMost frequently repeated transaction IDs:")
print(repeated_transactions.head(10))

print("\nInvestigating One Repeated Transaction")
transaction_id = 6145934
transaction_details = df[df["Transaction_ID"] == transaction_id]
print("Number of matching rows:", len(transaction_details))

print(
    transaction_details[
        ["Transaction_ID", "Customer_ID", "Date", "products",
         "Total_Amount", "Payment_Method", "Order_Status"]
    ].to_string(index=False)
)


print("\nChecking Transaction ID Uniqueness")
print("Total rows:", len(df))
print("Unique Transaction IDs:", df["Transaction_ID"].nunique())
print("Missing Transaction IDs:", df["Transaction_ID"].isnull().sum())


print("\nRecords with Missing Transaction IDs")
missing_transaction_ids = df[df["Transaction_ID"].isnull()]
print("Total records:", len(missing_transaction_ids))
print(
    missing_transaction_ids[
        ["Transaction_ID", "Customer_ID", "Date", "products", "Total_Amount"]
    ].head(10).to_string(index=False)
)

print("\nChecking Missing Transaction ID Records")
print(
    "Rows with missing Transaction_ID:",
    len(missing_transaction_ids)
)
print(
    "Rows duplicated across all columns:",
    missing_transaction_ids.duplicated().sum()
)

print("\nMissing Values Analysis")
missing_values = df.isnull().sum()
missing_values = missing_values[missing_values > 0]
print("Columns with missing values:")
print(missing_values.sort_values(ascending=False))
print("\nTotal missing values:", df.isnull().sum().sum())
print("\nTotal rows:", len(df))

print("\nInvestigating Missing Total_Amount")
missing_sales = df[df["Total_Amount"].isnull()]
print("Rows with missing Total_Amount:", len(missing_sales))
print(missing_sales[ ["Transaction_ID", "Amount", "Product_Category", "products"]
].head(15).to_string(index=False))

print("\nComparing Missing Total_Amount and Amount")
print("Missing Total_Amount:", df["Total_Amount"].isnull().sum())
print("Missing Amount:", df["Amount"].isnull().sum())
print("Both values missing:",(df["Total_Amount"].isnull() & df["Amount"].isnull()).sum()
)

print("\nChecking Amount and Total_Amount Relationship")
print("Correlation:", df["Amount"].corr(df["Total_Amount"]))
print("\nSample records where Total_Amount is missing:")
print(
    df.loc[
        df["Total_Amount"].isnull(),
        ["Amount", "Total_Amount", "Product_Category", "products"]
    ].head(10).to_string(index=False)
)

print("\nChecking Amount vs Total_Amount")
print(df[["Amount", "Total_Amount"]].describe())

print("\nChecking Missing Total_Amount by Product Category")
print(
    df[df["Total_Amount"].isnull()]
    .groupby("Product_Category")["Amount"]
    .agg(["count", "mean", "min", "max"])
    .sort_values("count", ascending=False)
)

print("\nChecking Total_Amount divided by Amount")
valid_amounts = df.dropna(subset=["Amount", "Total_Amount"])
valid_amounts = valid_amounts[valid_amounts["Amount"] != 0]
print(
    (valid_amounts["Total_Amount"] / valid_amounts["Amount"])
    .describe()
)

print("\nFrequency of Amount Ratios")
ratio = (valid_amounts["Total_Amount"] / valid_amounts["Amount"]
).round(2)
print(ratio.value_counts().head(15))


print("\nRecords where ratio is 5:")
print(valid_amounts[ratio == 5][["Amount", "Total_Amount", "Product_Category"]].head())

print("\nChecking records where ratio is not 5:")
print(valid_amounts[ratio != 5][["Amount", "Total_Amount", "Product_Category"]].head(10))

print("\nChecking Total_Amount and Amount relationship:")
print(df[["Amount", "Total_Amount"]].corr())



category_columns = [
    "Country",
    "Product_Category",
    "Gender",
    "Payment_Method",
    "Shipping_Method",
    "products"
]

df_clean = df.copy()
df_clean = df_clean.drop_duplicates()

for col in df_clean.select_dtypes(include=["object", "str"]).columns:
    df_clean[col] = df_clean[col].str.strip().replace("", np.nan)
df_clean[category_columns] = df_clean[category_columns].fillna("Unknown")
df_sales = df_clean.dropna(subset=["Total_Amount"]).copy()


for col in df_clean.select_dtypes(include="object").columns:
    df_clean[col] = df_clean[col].str.strip().replace("", np.nan)

print("\nOriginal dataset:", df.shape)
print("Cleaned dataset:", df_clean.shape)
print("Remaining missing values:", df_clean.isnull().sum().sum())


print("\nMissing values in important columns:")
print(df_clean[["Total_Amount", "Product_Category", "Country", "Date"]].isnull().sum())



df_sales = df_clean.dropna(subset=["Total_Amount"]).copy()

df_sales["Date"] = pd.to_datetime(df_sales["Date"], errors="coerce")

df_clean.to_csv("retail_data_cleaned.csv", index=False)
df_sales.to_csv("retail_sales_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("All cleaned records:", df_clean.shape)
print("Records available for sales analysis:", df_sales.shape)

df_clean = df.copy().drop_duplicates()

for col in df_clean.columns:
    if df_clean[col].dtype == "object" or df_clean[col].dtype.name == "str":
        df_clean[col] = df_clean[col].astype("string").str.strip().replace("", "Unknown").fillna("Unknown")
    else:
        df_clean[col] = df_clean[col].fillna("Unknown")

df_sales = df_clean[df_clean["Total_Amount"] != "Unknown"].copy()
df_sales["Total_Amount"] = pd.to_numeric(df_sales["Total_Amount"], errors="coerce")
df_sales = df_sales.dropna(subset=["Total_Amount"])

df["Total_Purchases"] = pd.to_numeric(df["Total_Purchases"], errors="coerce")
mask = df["Total_Purchases"].isna()
df.loc[mask, "Total_Purchases"] = np.random.randint(1, 11, size=mask.sum())

df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
mask = df["Amount"].isna()
df.loc[mask, "Amount"] = np.random.randint(100, 5001, size=mask.sum())

df["Total_Amount"] = pd.to_numeric(df["Total_Amount"], errors="coerce")
mask = df["Total_Amount"].isna()
df.loc[mask, "Total_Amount"] = (
    df.loc[mask, "Total_Purchases"] * df.loc[mask, "Amount"]
)
print(df[["Total_Purchases", "Amount", "Total_Amount"]].head(10))
print("\nRemaining missing values:")
print(df[["Total_Purchases", "Amount", "Total_Amount"]].isna().sum())


plt.figure(figsize=(9,6))
country_sales = df_sales.groupby("Country")["Total_Amount"].sum().nlargest(10).sort_values()
bars = country_sales.plot(kind="barh")
plt.title("Top 10 Countries by Total Sales - Cleaned Data")
plt.xlabel("Total Sales")
plt.ylabel("Country")
plt.ticklabel_format(axis="x", style="plain")
for bar in bars.patches:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
             f'{bar.get_width():,.0f}', va="center", ha="left", fontsize=9)
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}'))
    plt.xlim(right=country_sales.max() * 1.15)
plt.tight_layout()
plt.savefig("Charts/Cleaned_sales_by_country.png", dpi=300, bbox_inches="tight")
plt.show()


plt.figure(figsize=(9,6))
payment_sales = df_sales.groupby("Payment_Method")["Total_Amount"].sum().sort_values(ascending=False)
bars = payment_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("Sales by Payment Method - Cleaned Data")
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")
plt.ticklabel_format(axis="y", style="plain")
for bar in bars.patches:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'{bar.get_height():,.0f}', ha="center", va="bottom", fontsize=9)
plt.tight_layout()
plt.savefig("Charts/Cleaned_sales_by_payment_method.png", dpi=300, bbox_inches="tight")
plt.show()



plt.figure(figsize=(9,6))
customer_sales = df_sales[df_sales["Customer_ID"] != "Unknown"].groupby("Customer_ID")["Total_Amount"].sum().nlargest(10).sort_values()
customer_sales.index = customer_sales.index.astype(int).astype(str)
bars = customer_sales.plot(kind="barh")
plt.title("Top 10 Customers by Total Spending - Cleaned Data")
plt.xlabel("Total Spending")
plt.ylabel("Customer ID")
plt.ticklabel_format(axis="x", style="plain")
for bar in bars.patches:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
             f'{bar.get_width():,.0f}', va="center", ha="left", fontsize=9)
plt.xlim(right=customer_sales.max() * 1.15)
plt.tight_layout()
plt.savefig("Charts/Cleaned_sales_by_customer_spending.png", dpi=300, bbox_inches="tight")
plt.show()


plt.figure(figsize=(9,6))
gender_sales = df_sales.groupby("Gender")["Total_Amount"].sum().sort_values(ascending=False)
bars = gender_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("Sales by Gender - Cleaned Data")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.ticklabel_format(axis="y", style="plain")
for bar in bars.patches:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'{bar.get_height():,.0f}', ha="center", va="bottom", fontsize=9)
plt.tight_layout()
plt.savefig("Charts/Cleaned_sales_by_gender.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(9,6))
category_sales = df_sales.groupby("Product_Category")["Total_Amount"].sum().sort_values(ascending=False)
bars = category_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("Sales by Product Category - Cleaned Data")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.ticklabel_format(axis="y", style="plain")
for bar in bars.patches:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'{bar.get_height():,.0f}', ha="center", va="bottom", fontsize=9)
plt.tight_layout()
plt.savefig("Charts/Cleaned_sales_by_product_category.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(9,6))
category_sales = df_sales.groupby("Product_Category")["Total_Amount"].sum().sort_values(ascending=False)
bars = category_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("Sales by Product Category - Cleaned Data")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.ticklabel_format(axis="y", style="plain")
for bar in bars.patches:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'{bar.get_height():,.0f}', ha="center", va="bottom", fontsize=9)
plt.tight_layout()
plt.savefig("Charts/Cleaned_sales_by_product_category.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(9,6))
shipping_sales = df_sales.groupby("Shipping_Method")["Total_Amount"].sum().sort_values(ascending=False)
bars = shipping_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("Sales by Shipping Method - Cleaned Data")
plt.xlabel("Shipping Method")
plt.ylabel("Total Sales")
plt.ticklabel_format(axis="y", style="plain")
for bar in bars.patches:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'{bar.get_height():,.0f}', ha="center", va="bottom", fontsize=9)
plt.tight_layout()
plt.savefig("Charts/Cleaned_sales_by_shipping_method.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(10,6))
product_sales = df_sales.groupby("products")["Total_Amount"].sum().nlargest(10).sort_values()
bars = product_sales.plot(kind="barh")
plt.title("Top 10 Products by Total Sales - Cleaned Data")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.ticklabel_format(axis="x", style="plain")
for bar in bars.patches:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
             f'{bar.get_width():,.0f}', va="center", ha="left", fontsize=9)
plt.xlim(right=product_sales.max() * 1.15)
plt.tight_layout()
plt.savefig("Charts/Cleaned_sales_by_top_10_products.png", dpi=300, bbox_inches="tight")
plt.show()

df_sales["Date"] = pd.to_datetime(df_sales["Date"], errors="coerce")
plt.figure(figsize=(10,6))
df_sales["Date"] = pd.to_datetime(df_sales["Date"], errors="coerce")
monthly_sales = df_sales.dropna(subset=["Date"]).groupby(
    df_sales.dropna(subset=["Date"])["Date"].dt.month
)["Total_Amount"].sum()
monthly_sales.index = pd.to_datetime(monthly_sales.index, format="%m").strftime("%B")
bars = monthly_sales.plot(kind="bar")
plt.title("Monthly Sales - Cleaned Data")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.ticklabel_format(axis="y", style="plain")
for bar in bars.patches:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'{bar.get_height():,.0f}', ha="center", va="bottom", fontsize=8)
plt.tight_layout()
plt.savefig("Charts/Cleaned_monthly_sales.png", dpi=300, bbox_inches="tight")
plt.show()



country_sales = df_sales.groupby("Country")["Total_Amount"].sum()
print("1. Highest Sales Country:", country_sales.idxmax())
print("   Total Sales:", f"{country_sales.max():,.0f}")

payment_sales = df_sales.groupby("Payment_Method")["Total_Amount"].sum()
print("\n2. Best Payment Method:", payment_sales.idxmax())
print("   Total Sales:", f"{payment_sales.max():,.0f}")

gender_sales = df_sales.groupby("Gender")["Total_Amount"].sum()
print("\n3. Highest Sales by Gender:", gender_sales.idxmax())
print("   Total Sales:", f"{gender_sales.max():,.0f}")

product_sales = df_sales.groupby("products")["Total_Amount"].sum()
print("\n4. Top-Selling Product:", product_sales.idxmax())
print("   Total Sales:", f"{product_sales.max():,.0f}")


df_sales["Date"] = pd.to_datetime(df_sales["Date"], errors="coerce")
monthly_sales = df_sales.dropna(subset=["Date"]).groupby(
    df_sales.dropna(subset=["Date"])["Date"].dt.month
)["Total_Amount"].sum()

monthly_sales.index = pd.to_datetime(
    monthly_sales.index, format="%m"
).strftime("%B")

print("\n5. Highest Sales Month:", monthly_sales.idxmax())
print("   Total Sales:", f"{monthly_sales.max():,.0f}")
print("   Lowest Sales Month:", monthly_sales.idxmin())
print("   Total Sales:", f"{monthly_sales.min():,.0f}")