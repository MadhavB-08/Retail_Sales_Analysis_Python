import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("row_dataset.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)


print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

df = df.replace(r'^\s*$', pd.NA, regex=True)

print("\nMissing Values:")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0].sort_values(ascending=False))

print("\nMissing Value Percentage:")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage[missing_percentage > 0].round(2))

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nRepeated Transaction IDs:")
print(df["Transaction_ID"].dropna().duplicated().sum())

print("\nUnique Transaction IDs:")
print(df["Transaction_ID"].nunique())

repeated_ids = df[df["Transaction_ID"].duplicated(keep=False)]

print("\nTotal rows with repeated Transaction IDs:")
print(len(repeated_ids))

print("\nMost Repeated Transaction IDs:")
print(df["Transaction_ID"].value_counts().head(10))

print("\nSample Repeated Transactions:")
print(
    repeated_ids[
        ["Transaction_ID", "Customer_ID", "Date",
         "products", "Total_Amount", "Product_Category"]
    ].head(15).to_string(index=False)
)

print("\nMissing Values Summary:")

missing = df.isnull().sum()

for column, count in missing.items():
    if count > 0:
        print(column, ":", count)

print("\nTotal Missing Values:", df.isnull().sum().sum())

missing_report = df.isnull().sum()

missing_report = missing_report[missing_report > 0].sort_values(
    ascending=False
)

print("\nComplete Missing Values Report:")
print(missing_report.to_string())

print("\nTotal Missing Values:", missing_report.sum())

amount = pd.to_numeric(df["Amount"], errors="coerce")
purchases = pd.to_numeric(df["Total_Purchases"], errors="coerce")
total = pd.to_numeric(df["Total_Amount"], errors="coerce")

valid = amount.notna() & purchases.notna() & total.notna()

difference = abs(
    (amount[valid] * purchases[valid]) - total[valid]
)

print("\nFinancial Data Consistency:")

print("Records with all 3 values:", valid.sum())

print("Records matching the formula:", (difference < 0.01).sum())

print("Records not matching the formula:", (difference >= 0.01).sum())

print("\nMissing Financial Values:")
print("Amount:", amount.isnull().sum())
print("Total Purchases:", purchases.isnull().sum())
print("Total Amount:", total.isnull().sum())

date_check = pd.to_datetime(
    df["Date"],
    format="mixed",
    errors="coerce"
)

print("\nDate Analysis:")
print("Valid Dates:", date_check.notna().sum())
print("Invalid or Missing Dates:", date_check.isnull().sum())

df_clean = df.copy()

df_clean = df_clean.drop_duplicates()

for col in df_clean.select_dtypes(include=["object", "str"]).columns:
    df_clean[col] = df_clean[col].str.strip()

df_clean = df_clean.replace(r'^\s*$', pd.NA, regex=True)

category_columns = [
    "Country",
    "State",
    "City",
    "Gender",
    "Customer_Segment",
    "Product_Category",
    "Product_Brand",
    "Product_Type",
    "Feedback",
    "Shipping_Method",
    "Payment_Method",
    "Order_Status",
    "products"
]

df_clean[category_columns] = df_clean[category_columns].fillna("Unknown")

numeric_columns = [
    "Age",
    "Income",
    "Total_Purchases",
    "Amount",
    "Total_Amount",
    "Ratings"
]

for col in numeric_columns:
    df_clean[col] = pd.to_numeric(df_clean[col], errors="coerce")

df_clean["Date"] = pd.to_datetime(
    df_clean["Date"],
    format="mixed",
    errors="coerce"
)

df_clean["Year"] = df_clean["Date"].dt.year
df_clean["Month"] = df_clean["Date"].dt.month_name()

df_sales = df_clean.dropna(subset=["Total_Amount"]).copy()

print("\nData Cleaning Results:")

print("Original Dataset:", df.shape)
print("Cleaned Dataset:", df_clean.shape)
print("Sales Dataset:", df_sales.shape)

print("\nRemaining Missing Values:")
print(df_clean.isnull().sum()[df_clean.isnull().sum() > 0])

print("\nMissing Total Amount in Sales Dataset:")
print(df_sales["Total_Amount"].isnull().sum())

print("\nFinal Dataset Summary")
print("Original Rows:", len(pd.read_csv("row_dataset.csv")))
print("Cleaned Rows:", len(df_clean))
print("Sales Analysis Rows:", len(df_sales))
print("Valid Date Records:", df_clean["Date"].notna().sum())
print("Missing Sales Values:", df_sales["Total_Amount"].isnull().sum())

df_clean.to_csv("retail_data_cleaned.csv", index=False)

df_sales.to_csv("retail_sales_cleaned.csv", index=False)

print("\nCleaned datasets saved successfully!")

print("Master Dataset: retail_data_cleaned.csv")
print("Sales Dataset: retail_sales_cleaned.csv")

total_revenue = df_sales["Total_Amount"].sum()

total_transactions = df_sales["Transaction_ID"].nunique()

average_transaction = total_revenue / total_transactions

total_customers = df_sales["Customer_ID"].nunique()

category_sales = df_sales.groupby("Product_Category")["Total_Amount"].sum()
top_category = category_sales.idxmax()

country_sales = df_sales.groupby("Country")["Total_Amount"].sum()
top_country = country_sales.idxmax()

payment_sales = df_sales.groupby("Payment_Method")["Total_Amount"].sum()
best_payment = payment_sales.idxmax()

print(df_sales["products"].value_counts().head(15))

print("\nProduct Type Values:")
print(df_sales["Product_Type"].value_counts().head(15))

print("\nProducts Column Values:")
print(df_sales["products"].value_counts().head(15))

df_sales = df_sales[
    (df_sales["products"].astype(str).str.strip().str.lower() != "products") &
    (df_sales["Product_Type"].astype(str).str.strip().str.lower() != "product_type")
].copy()

print("BUSINESS KPIs")

print("Total Revenue:", round(total_revenue, 2))
print("Total Transactions:", total_transactions)
print("Average Transaction Value:", round(average_transaction, 2))
print("Total Customers:", total_customers)
print("Top Product Category:", top_category)
print("Top Country:", top_country)
print("Best Payment Method:", best_payment)

category_sales = df_sales.groupby("Product_Category")["Total_Amount"].sum()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.ticklabel_format(axis="y", style="plain")
plt.tight_layout()
plt.savefig("Charts/sales_by_product_category.png", dpi=300, bbox_inches="tight")
plt.show()

country_sales = df_sales.groupby("Country")["Total_Amount"].sum()
country_sales = country_sales.sort_values(ascending=False).head(10)

plt.figure(figsize=(8, 5))
country_sales.sort_values().plot(kind="barh")
plt.title("Top 10 Countries by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Country")
plt.ticklabel_format(axis="x", style="plain")
plt.tight_layout()
plt.savefig("Charts/top_10_countries_by_sales.png", dpi=300, bbox_inches="tight")
plt.show()


monthly_sales = df_sales.groupby(df_sales["Date"].dt.month)["Total_Amount"].sum()

monthly_sales.index = pd.to_datetime(monthly_sales.index, format="%m").strftime("%B")

plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="line", marker="o")
plt.xticks(range(len(monthly_sales)), monthly_sales.index, rotation=45)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.ticklabel_format(axis="y", style="plain")
plt.tight_layout()
plt.savefig("Charts/monthly_sales_trend.png", dpi=300, bbox_inches="tight")
plt.show()


payment_sales = df_sales.groupby("Payment_Method")["Total_Amount"].sum()

plt.figure(figsize=(8, 5))
payment_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")
plt.ticklabel_format(axis="y", style="plain")
plt.tight_layout()
plt.savefig("Charts/sales_by_payment_method.png", dpi=300, bbox_inches="tight")
plt.show()

shipping_sales = df_sales.groupby("Shipping_Method")["Total_Amount"].sum()

plt.figure(figsize=(8, 5))
shipping_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("Sales by Shipping Method")
plt.xlabel("Shipping Method")
plt.ylabel("Total Sales")
plt.ticklabel_format(axis="y", style="plain")
plt.tight_layout()
plt.savefig("Charts/sales_by_shipping_method.png", dpi=300, bbox_inches="tight")
plt.show()


gender_sales = df_sales.groupby("Gender")["Total_Amount"].sum()

plt.figure(figsize=(8, 5))
gender_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.ticklabel_format(axis="y", style="plain")
plt.tight_layout()
plt.savefig("Charts/sales_by_gender.png", dpi=300, bbox_inches="tight")
plt.show()


print(df_sales["products"].value_counts().head(15))



product_sales = df_sales.groupby("products")["Total_Amount"].sum()

product_sales = product_sales.sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
product_sales.sort_values().plot(kind="barh")
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.ticklabel_format(axis="x", style="plain")
plt.tight_layout()
plt.savefig("Charts/top_10_products_by_sales.png", dpi=300, bbox_inches="tight")
plt.show()

segment_sales = df_sales.groupby("Customer_Segment")["Total_Amount"].sum()

plt.figure(figsize=(8, 5))
segment_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales")
plt.ticklabel_format(axis="y", style="plain")
plt.tight_layout()
plt.savefig("Charts/sales_by_customer_segment.png", dpi=300, bbox_inches="tight")
plt.show()

brand_sales = df_sales.groupby("Product_Brand")["Total_Amount"].sum()

brand_sales = brand_sales.sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
brand_sales.sort_values().plot(kind="barh")
plt.title("Top 10 Brands by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Brand")
plt.ticklabel_format(axis="x", style="plain")
plt.tight_layout()
plt.savefig("Charts/top_10_brands_by_sales.png", dpi=300, bbox_inches="tight")
plt.show()

status_sales = df_sales.groupby("Order_Status")["Total_Amount"].sum()

plt.figure(figsize=(8, 5))
status_sales.plot(kind="bar")
plt.xticks(rotation=0)
plt.title("Sales by Order Status")
plt.xlabel("Order Status")
plt.ylabel("Total Sales")
plt.ticklabel_format(axis="y", style="plain")
plt.tight_layout()
plt.savefig("Charts/sales_by_order_status.png", dpi=300, bbox_inches="tight")
plt.show()
