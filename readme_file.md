# 🛒 E-Commerce Customer Analytics & Segmentation (Python)

## 📌 Project Overview

This project analyzes **540K+ e-commerce transactions** to understand customer purchasing behavior, revenue contribution, and customer value. Using **Python** and **RFM (Recency, Frequency, Monetary) analysis**, customers are segmented into actionable groups to support **retention strategies** and **targeted marketing decisions**.

The project is designed as an **end-to-end Data Analyst portfolio project**, covering data cleaning, exploratory data analysis, customer segmentation, and business insights.

---

## 🎯 Objectives

* Analyze large-scale e-commerce transaction data
* Identify revenue patterns and customer behavior
* Segment customers based on RFM methodology
* Detect high-value and churn-risk customer groups
* Provide data-driven insights for marketing and retention

---

## 📊 Dataset

* **Source**: Online Retail transactional dataset
* **Records**: 540,000+ transactions
* **Customers**: 4,338 unique customers
* **Total Revenue**: ~$8.9M

### Key Fields

* InvoiceNo
* CustomerID
* InvoiceDate
* Quantity
* UnitPrice
* Country
* Revenue (derived)

---

## 🗂️ Project Structure

```
online-retail-analysis/
│
├── data/
│   ├── raw/
│   │   └── online_retail.csv
│   └── processed/
│       ├── online_retail_cleaned.csv
│       ├── rfm_customer_segmentation.csv
│       └── segment_summary.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   └── 03_rfm_customer_segmentation.ipynb
│
├── dashboard/            # (optional – for Streamlit dashboard)
├── outputs/              # charts, figures, exports
├── requirements.txt
└── README.md
```

---

## 🔍 Analysis Workflow

### 1️⃣ Data Cleaning (`01_data_cleaning.ipynb`)

* Removed cancelled transactions and missing CustomerIDs
* Handled negative quantities and invalid prices
* Created revenue feature (`Quantity × UnitPrice`)
* Exported cleaned dataset for downstream analysis

### 2️⃣ Exploratory Data Analysis (`02_exploratory_data_analysis.ipynb`)

* Revenue trends over time
* Top countries and customers by revenue
* Distribution of order values and purchase frequency
* Customer contribution analysis

### 3️⃣ RFM Customer Segmentation (`03_rfm_customer_segmentation.ipynb`)

* Calculated **Recency, Frequency, Monetary** metrics
* Scored customers using quantile-based RFM scoring
* Segmented customers into **11 distinct groups**
* Identified:

  * Top 10% customers contributing **43% of total revenue**
  * Churn-risk and low-engagement segments

---

## 📈 Key Insights

* A small group of high-value customers drives a disproportionate share of revenue
* Clear behavioral differences between loyal, potential, and at-risk customers
* RFM segmentation enables targeted retention and personalization strategies

---

## 🛠️ Tools & Technologies

* **Python**
* **Pandas, NumPy** – data manipulation
* **Matplotlib / Seaborn** – data visualization
* **Jupyter Notebook** – analysis workflow

---

## 🚀 How to Run

1. Clone the repository

```bash
git clone <repo-url>
cd online-retail-analysis
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Open notebooks

```bash
jupyter notebook
```

Run notebooks in order:

1. `01_data_cleaning.ipynb`
2. `02_exploratory_data_analysis.ipynb`
3. `03_rfm_customer_segmentation.ipynb`

---

## 💡 Future Improvements

* Build an interactive **Streamlit dashboard** for RFM exploration
* Integrate **Power BI** for business-facing reports
* Apply **customer lifetime value (CLV)** modeling
* Automate segmentation pipeline

---

⭐ *This project is part of my Data Analyst portfolio. Feedback is welcome!*
