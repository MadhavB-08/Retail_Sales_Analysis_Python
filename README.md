# 📊 Retail Sales Analysis & Data Processing Pipeline with Python

An end-to-end data analytics and exploratory data analysis (EDA) pipeline analyzing over **300,000+ retail sales transactions**. Built entirely with Python, Pandas, and Matplotlib, this project implements a rigorous data auditing and cleaning framework, validates transactional and financial integrity, extracts core commercial KPIs, and produces 10 publication-quality analytical visualizations.

---

> [!IMPORTANT]
> **Data Confidentiality Notice**: The datasets used in this project (`row_dataset.csv`, `retail_data_cleaned.csv`, and `retail_sales_cleaned.csv`) contain proprietary and confidential business information. In strict compliance with data privacy policies and non-disclosure obligations, all raw and processed CSV data files are excluded from this public repository via `.gitignore`. The complete codebase, analytical workflows, data schemas, and visualization figures are fully documented below for demonstration and portfolio review.

---

## 🔍 Project Overview

Modern omnichannel retail operations generate massive transactional datasets spanning multiple geographic regions, distribution channels, and customer segments. Raw transactional logs frequently suffer from data hygiene issues such as mixed date formats, whitespace anomalies, missing values, corrupted header artifacts, and transactional discrepancies.

This project delivers a complete, reproducible data pipeline implemented in [`python_analysis.py`](python_analysis.py):
- **Deep Data Quality Audit**: Discovers missing value distributions, calculates null percentages, identifies duplicate transaction IDs, and validates financial integrity (`Total_Amount = Amount × Total_Purchases`).
- **Comprehensive Preprocessing Engine**: Automates string stripping, regex whitespace removal, categorical imputation (`"Unknown"` across 13 columns), numeric coercion, and date normalization.
- **Header Artifact & Outlier Cleansing**: Automatically filters out repeated header entries and corrupted strings in product metadata.
- **Automated Dataset Export**: Generates both a master cleaned dataset (`retail_data_cleaned.csv`) and a targeted sales analysis dataset (`retail_sales_cleaned.csv`).
- **Executive KPI Reporting**: Aggregates enterprise-level commercial metrics across revenue, order velocity, basket size, and customer volume.
- **10 High-Resolution Visualizations**: Exports 300 DPI figures to the `Charts/` directory covering customer demographics, fulfillment, brands, products, and temporal trends.

---

## 📈 Key Business Insights & KPIs

Based on the verified analysis of **301,656 validated sales records** across global operations:

| Metric | Business Indicator / Top Performer | Total Volume / Value |
| :--- | :--- | :--- |
| **Total Net Revenue** | 💰 Overall Sales Across All Channels | **$412,558,519.22** |
| **Total Unique Transactions** | 🧾 Distinct Completed Orders | **294,126** |
| **Total Unique Customers** | 👥 Active Customer Base | **86,748** |
| **Average Transaction Value (AOV)** | 🏷️ Mean Basket Size | **$1,402.66** |
| **Top Country by Revenue** | 🇺🇸 United States (USA) | **$129,722,153.93** |
| **Top Product Category** | 📱 Electronics | **$97,398,318.23** |
| **Top-Selling Brand** | 🥤 Pepsi | **$41,354,053.36** |
| **Top-Selling Single Product** | 💧 Bottled Water | **$3,432,024.73** |
| **Dominant Customer Segment** | 👥 Regular | **$199,963,135.13** |
| **Preferred Payment Gateway** | 💳 Credit Card | **$123,255,207.16** |
| **Primary Shipping Method** | 🚀 Same-Day Delivery | **$142,237,872.48** |
| **Top Order Status** | 📦 Delivered | **$178,115,886.82** |

---

## 🗃️ Dataset Architecture & Schema

The underlying transactional dataset captures 30 distinct attributes across customer profiles, geographic dimensions, transactional financials, and product logistics:

```text
Transaction_ID, Customer_ID, Name, Email, Phone, Address, City, State, Zipcode, 
Country, Age, Gender, Income, Customer_Segment, Date, Year, Month, Time, 
Total_Purchases, Amount, Total_Amount, Product_Category, Product_Brand, 
Product_Type, Feedback, Shipping_Method, Payment_Method, Order_Status, Ratings, products
```

### Feature Classification:
- **Customer Profiles**: `Customer_ID`, `Name`, `Email`, `Phone`, `Age`, `Gender`, `Income`, `Customer_Segment`
- **Geographic Information**: `Address`, `City`, `State`, `Zipcode`, `Country`
- **Order & Financial Metrics**: `Transaction_ID`, `Date`, `Year`, `Month`, `Time`, `Total_Purchases` (Quantity), `Amount` (Unit Price), `Total_Amount` (Gross Sales)
- **Product Taxonomy**: `Product_Category`, `Product_Brand`, `Product_Type`, `products`
- **Fulfillment & Customer Experience**: `Shipping_Method`, `Payment_Method`, `Order_Status`, `Feedback`, `Ratings`

---

## 🛠️ Pipeline Architecture (`python_analysis.py`)

The end-to-end Python script executes in 6 systematic stages:

```
┌─────────────────────────┐
│   1. Data Ingestion     │ ──> Load row_dataset.csv, profile shape, datatypes & info
└───────────┬─────────────┘
            │
┌───────────▼─────────────┐
│ 2. Audit & Verification │ ──> Regex whitespace audit, null %, duplicate Transaction_ID,
│                         │     and financial validation (Total_Amount == Amount * Total_Purchases)
└───────────┬─────────────┘
            │
┌───────────▼─────────────┐
│  3. Cleaning & Cleansing│ ──> Drop duplicate rows, strip string whitespace, fill categorical
│                         │     missing with 'Unknown', coerce numerics, parse mixed dates
└───────────┬─────────────┘
            │
┌───────────▼─────────────┐
│  4. Dataset Separation  │ ──> Filter out corrupted header artifact rows ("products", "product_type")
│       & Persistence     │     Export retail_data_cleaned.csv and retail_sales_cleaned.csv
└───────────┬─────────────┘
            │
┌───────────▼─────────────┐
│  5. Business KPI Engine │ ──> Calculate total revenue, transaction counts, AOV, top performers
└───────────┬─────────────┘
            │
┌───────────▼─────────────┐
│ 6. High-Res Visualization│ ──> Generate & export 10 charts (300 DPI) to Charts/ directory
└─────────────────────────┘
```

### Step-by-Step Breakdown:

1. **Data Ingestion & Profiling**:
   - Reads raw transaction data into a pandas DataFrame (`row_dataset.csv`).
   - Inspects dataset dimensions, column names, memory footprint, and initial records.

2. **Data Hygiene & Consistency Audit**:
   - Converts blank and whitespace-only strings into `pd.NA` using regular expressions (`r'^\s*$'`).
   - Identifies total missing records and ranks columns by missing percentage.
   - Evaluates row-level duplicate records and transaction ID collision frequency.
   - **Financial Formula Consistency**: Verifies transaction integrity using numeric checks:
     $$\text{Consistency} = |\text{Amount} \times \text{Total\_Purchases} - \text{Total\_Amount}| < 0.01$$

3. **Data Transformation & Imputation**:
   - Deduplication: Removes redundant records via `drop_duplicates()`.
   - String Sanitization: Trims leading and trailing spaces from all object/string columns.
   - Categorical Imputation: Systematically fills missing values in 13 categorical fields (`Country`, `State`, `City`, `Gender`, `Customer_Segment`, `Product_Category`, `Product_Brand`, `Product_Type`, `Feedback`, `Shipping_Method`, `Payment_Method`, `Order_Status`, `products`) with `"Unknown"`.
   - Numeric Coercion: Safely casts numeric fields (`Age`, `Income`, `Total_Purchases`, `Amount`, `Total_Amount`, `Ratings`) using `errors="coerce"`.
   - Datetime Standardization: Parses varied date strings into unified `datetime64` representations using `format="mixed"`, and engineers `Year` and `Month` features.

4. **Header Artifact Cleaning & Dataset Export**:
   - Removes corrupted rows where header strings were inadvertently ingested as values (e.g. `products == "products"` or `Product_Type == "product_type"`).
   - Generates two CSV files:
     - `retail_data_cleaned.csv`: Master preprocessed dataset.
     - `retail_sales_cleaned.csv`: Cleaned dataset containing records with validated `Total_Amount`.

5. **Automated KPI Aggregations**:
   - Computes aggregated sales metrics across product category, country, payment method, shipping method, and demographics.

6. **Visualization Suite**:
   - Automatically builds and saves 10 publication-ready figures with 300 DPI resolution, clean labeling, unscientific notation (`style="plain"`), and tight bounding boxes into `Charts/`.

---

## 📊 Visualizations & Output Catalog

The script produces 10 high-resolution charts saved directly to the [`Charts/`](Charts/) folder:

| Chart Filename | Chart Type | Analytical Focus |
| :--- | :--- | :--- |
| [`sales_by_product_category.png`](Charts/sales_by_product_category.png) | Vertical Bar Chart | Revenue distribution across major product categories (Electronics, Grocery, Clothing, etc.) |
| [`top_10_countries_by_sales.png`](Charts/top_10_countries_by_sales.png) | Horizontal Bar Chart | Top 10 revenue-generating countries globally |
| [`monthly_sales_trend.png`](Charts/monthly_sales_trend.png) | Line Plot with Markers | Longitudinal monthly revenue trajectory across the calendar year |
| [`sales_by_payment_method.png`](Charts/sales_by_payment_method.png) | Vertical Bar Chart | Revenue share comparison by payment gateway (Credit Card, Debit Card, PayPal, Cash) |
| [`sales_by_shipping_method.png`](Charts/sales_by_shipping_method.png) | Vertical Bar Chart | Logistics distribution by shipping tier (Same-Day, Express, Standard) |
| [`sales_by_gender.png`](Charts/sales_by_gender.png) | Vertical Bar Chart | Demographic spending patterns segmented by gender |
| [`top_10_products_by_sales.png`](Charts/top_10_products_by_sales.png) | Horizontal Bar Chart | Top 10 individual products by cumulative sales volume |
| [`sales_by_customer_segment.png`](Charts/sales_by_customer_segment.png) | Vertical Bar Chart | Revenue generated by customer tier (Regular, Premium, VIP) |
| [`top_10_brands_by_sales.png`](Charts/top_10_brands_by_sales.png) | Horizontal Bar Chart | Top 10 leading manufacturing brands by gross revenue |
| [`sales_by_order_status.png`](Charts/sales_by_order_status.png) | Vertical Bar Chart | Transaction value distribution across fulfillment statuses (Delivered, Shipped, Processing, Cancelled) |

---

## 📁 Repository Structure

```text
Retail_Sales_Analysis_Python/
│
├── Charts/                               # Generated 300 DPI visualization figures
│   ├── monthly_sales_trend.png           # Monthly revenue velocity
│   ├── sales_by_customer_segment.png     # Customer tier sales comparison
│   ├── sales_by_gender.png               # Gender-based sales distribution
│   ├── sales_by_order_status.png         # Fulfillment status breakdown
│   ├── sales_by_payment_method.png       # Payment gateway usage
│   ├── sales_by_product_category.png     # Category revenue breakdown
│   ├── sales_by_shipping_method.png      # Logistics channel distribution
│   ├── top_10_brands_by_sales.png        # Brand leaderboard
│   ├── top_10_countries_by_sales.png     # Geographic sales leaderboard
│   └── top_10_products_by_sales.png      # Individual product leaderboard
│
├── .gitignore                            # Excludes *.csv and temporary runtime files
├── python_analysis.py                    # Complete end-to-end Python pipeline
├── README.md                             # Project documentation
│
├── [EXCLUDED] row_dataset.csv            # Raw retail dataset (omitted due to confidentiality)
├── [EXCLUDED] retail_data_cleaned.csv    # Cleaned master dataset (omitted due to confidentiality)
└── [EXCLUDED] retail_sales_cleaned.csv   # Cleaned sales dataset (omitted due to confidentiality)
```

---

## ⚙️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.8+** installed. Check your version with:
```bash
python --version
```

### 2. Clone the Repository
```bash
git clone https://github.com/MadhavB-08/Retail_Sales_Analysis_Python.git
cd Retail_Sales_Analysis_Python
```

### 3. Install Dependencies
Install the required scientific Python libraries using `pip`:
```bash
pip install pandas matplotlib numpy
```

---

## 🚀 Execution & Usage

To run the complete data audit, preprocessing pipeline, KPI extraction, and chart generation workflow:

```bash
python python_analysis.py
```

### Execution Output:
1. **Console Logging**: Outputs raw data dimensions, missing value reports, duplicate transaction frequency, financial consistency results, and executive business KPIs.
2. **Dataset Exports**: Generates `retail_data_cleaned.csv` and `retail_sales_cleaned.csv` in the project root.
3. **Chart Exports**: Saves all 10 high-resolution analytical plots directly into the `Charts/` directory.

> [!NOTE]
> Since the original dataset is confidential and excluded from this repository via `.gitignore`, executing the pipeline locally requires placing your own compatible dataset structured according to the documented schema (named `row_dataset.csv`) in the root directory.

---

## 🔒 Data Confidentiality & Compliance Disclaimer

The transaction data analyzed in this project originates from proprietary business operations and is strictly confidential. In compliance with enterprise non-disclosure agreements (NDAs) and international data privacy regulations, the dataset cannot be uploaded, published, or distributed in this repository. All code implementations, data processing methodologies, schema definitions, and statistical visualizations are presented exclusively for technical evaluation and portfolio demonstration.

