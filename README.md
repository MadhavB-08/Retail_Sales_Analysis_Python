# 📊 Retail Sales Analysis with Python

An end-to-end data analytics and exploratory data analysis (EDA) project analyzing over **300,000+ retail sales transactions**. This project focuses on end-to-end data processing: data ingestion, data hygiene and cleaning, missing value imputation, transaction-level aggregation, and publication-ready data visualization.

---

## 🔍 Project Overview

Retail businesses generate high-volume transaction data across multiple global territories, distribution channels, and product categories. Uncovering customer purchasing patterns, seasonal sales velocity, payment preferences, and shipping channel usage is critical for optimizing revenue and inventory management.

This project delivers:
- **Comprehensive Data Audit**: Identification of missing values, anomalies, and duplicate records across 30 attributes.
- **Robust Cleaning Pipeline**: Systematic whitespace stripping, imputation of missing monetary figures via calculated relationships (`Total_Amount = Total_Purchases × Amount`), and datetime normalization.
- **Multi-Dimensional Business Analysis**: Sales breakdown across countries, product lines, payment gateways, demographics, customer segments, and monthly timeline trends.
- **Publication-Ready Visualizations**: High-DPI bar charts, horizontal rankings, and formatted labels stored in the `Charts/` directory.

---

## 📈 Key Business Insights

Based on analysis of **301,656+ validated sales records**:

| Metric | Insight / Top Performer | Total Sales Volume |
| :--- | :--- | :--- |
| **Top Country** | 🇺🇸 **United States (USA)** | **$129,722,154** |
| **Leading Product Category** | 📱 **Electronics** | **$97,398,320** |
| **Secondary Product Category** | 🛒 **Grocery** | **$91,076,810** |
| **Preferred Payment Method** | 💳 **Credit Card** | **$123,255,207** |
| **Top Shipping Method** | 🚀 **Same-Day Delivery** | **$142,239,400** |
| **Highest Sales Month** | 📅 **March** | **$21,597,056** |
| **Lowest Sales Month** | ❄️ **February** | **$19,702,425** |
| **Top-Selling Single Product** | 💧 **Bottled Water** | **$3,432,025** |
| **Demographic Breakdown** | 👨 **Male** vs 👩 **Female** | **$256.18M** vs **$155.95M** |

---

## 🗃️ Dataset Architecture

The project works with retail transaction records containing 30 features across demographics, product data, and order metrics:

```
Transaction_ID, Customer_ID, Name, Email, Phone, Address, City, State, Zipcode, 
Country, Age, Gender, Income, Customer_Segment, Date, Year, Month, Time, 
Total_Purchases, Amount, Total_Amount, Product_Category, Product_Brand, 
Product_Type, Feedback, Shipping_Method, Payment_Method, Order_Status, Ratings, products
```

### Core Data Categories:
- **Customer Profiles**: `Customer_ID`, `Age`, `Gender`, `Income`, `Customer_Segment`
- **Geographic Data**: `Country`, `State`, `City`, `Zipcode`
- **Order & Financials**: `Total_Purchases`, `Amount` (Unit Price), `Total_Amount`, `Payment_Method`
- **Product Information**: `Product_Category`, `Product_Brand`, `Product_Type`, `products`
- **Logistics & Service**: `Shipping_Method`, `Order_Status`, `Feedback`, `Ratings`, `Date`

---

## 🧹 Data Cleaning & Pipeline

The pipeline in [`python_analysis.py`](python_analysis.py) standardizes and fixes dirty raw data:

1. **Deduplication**: Removes exact duplicates from the raw 302,010-row dataset.
2. **String Standardization**: Strips leading/trailing whitespaces and replaces empty string literals with explicit `'Unknown'` categories for categorical fields (`Country`, `Product_Category`, `Gender`, `Payment_Method`, `Shipping_Method`).
3. **Data Imputation & Integrity**:
   - Validates that `Total_Amount = Total_Purchases * Amount`.
   - Populates missing numerical indicators seamlessly using verifiable transaction relationships.
4. **Date Standardization**: Parses varied date formats into unified pandas `datetime64` representations for monthly aggregation and trend reporting.
5. **Output Generation**:
   - `retail_data_cleaned.csv`: Cleaned dataset across all attributes.
   - `retail_sales_cleaned.csv`: Validated sales-specific dataset ready for immediate BI and machine learning tasks.

---

## 📊 Visualizations & Charts

Visualizations are saved with high resolution (300 DPI) in the `Charts/` directory:

| Visualized Metric | File Path |
| :--- | :--- |
| **Sales by Country** | `Charts/Cleaned_sales_by_country.png` |
| **Sales by Product Category** | `Charts/Cleaned_sales_by_product_category.png` |
| **Sales by Payment Method** | `Charts/Cleaned_sales_by_payment_method.png` |
| **Sales by Shipping Method** | `Charts/Cleaned_sales_by_shipping_method.png` |
| **Sales by Gender** | `Charts/Cleaned_sales_by_gender.png` |
| **Top 10 Products by Sales** | `Charts/Cleaned_sales_by_top_10_products.png` |
| **Top 10 Customer Spending** | `Charts/Cleaned_sales_by_customer_spending.png` |
| **Monthly Sales Trend** | `Charts/Cleaned_monthly_sales_trend.png` |

---

## 📁 Project Structure

```text
Retail_Sales_Analysis_Python/
│
├── Charts/                               # Generated high-resolution plots
│   ├── Cleaned_monthly_sales_trend.png
│   ├── Cleaned_sales_by_country.png
│   ├── Cleaned_sales_by_customer_spending.png
│   ├── Cleaned_sales_by_gender.png
│   ├── Cleaned_sales_by_payment_method.png
│   ├── Cleaned_sales_by_product_category.png
│   ├── Cleaned_sales_by_shipping_method.png
│   ├── Cleaned_sales_by_top_10_products.png
│   └── ... (raw chart variations)
│
├── Dataset_2.csv                         # Raw retail sales dataset (300k+ rows)
├── retail_data_cleaned.csv               # Preprocessed & standardized dataset
├── retail_sales_cleaned.csv              # Cleaned dataset tailored for sales analysis
├── python_analysis.py                    # Main script: cleaning, EDA, aggregation, charts
└── README.md                             # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### 2. Clone / Open the Workspace
```bash
git clone https://github.com/MadhavB-08/Retail_Sales_Analysis_Python.git
cd Retail_Sales_Analysis_Python
```

### 3. Install Required Libraries
```bash
pip install pandas matplotlib numpy
```

---

## 🚀 Usage

Execute the complete data processing, statistical reporting, and visual generation workflow by running:

```bash
python python_analysis.py
```

### Script Execution Highlights:
- Displays summary dimensions and initial missing-value distribution.
- Computes aggregated sales metrics across product category, country, payment method, shipping method, and demographics.
- Performs data cleaning and exports `retail_data_cleaned.csv` and `retail_sales_cleaned.csv`.
- Generates and saves visualization figures directly into the `Charts/` directory.
- Prints executive summary KPI findings to the console.

---

## 🔒 Data Confidentiality & Disclaimer

The dataset utilized in this project consists of confidential retail transaction data. In compliance with privacy standards and non-disclosure obligations, the raw dataset and processed CSV files cannot be uploaded or shared in this repository. All code, schemas, and analytical outputs are provided exclusively for methodology demonstration and portfolio review.

