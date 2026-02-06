# 📊 E-Commerce Sales Analysis & Customer Segmentation

A comprehensive data analysis project analyzing online retail transactions, customer behavior, and building an interactive dashboard for business insights.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.1.4-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Project Objectives

- Clean and prepare e-commerce transaction data
- Perform exploratory data analysis (EDA) to uncover business insights
- Segment customers using RFM (Recency, Frequency, Monetary) analysis
- Build an interactive dashboard for data visualization
- Provide actionable business recommendations

## 📁 Project Structure

```
online-retail-analysis/
│
├── data/
│   ├── raw/                          # Raw dataset
│   │   └── online_retail.csv
│   └── processed/                    # Cleaned data
│       ├── online_retail_cleaned.csv
│       ├── rfm_customer_segmentation.csv
│       └── segment_summary.csv
│
├── notebooks/
│   ├── 01_data_cleaning.py          # Data cleaning script
│   ├── 02_exploratory_data_analysis.py  # EDA script
│   └── 03_rfm_customer_segmentation.py  # RFM analysis script
│
├── dashboard/
│   └── 04_streamlit_dashboard.py    # Interactive dashboard
│
├── outputs/                          # Visualization outputs
│   ├── 01_monthly_revenue_trend.png
│   ├── 02_top_countries_revenue.png
│   ├── 03_revenue_by_dayofweek.png
│   └── ... (more charts)
│
├── requirements.txt                  # Python dependencies
└── README.md                        # Project documentation
```

## 📊 Dataset

**Source:** [Online Retail Dataset - Kaggle](https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset)

**Description:** 
- Transnational dataset of a UK-based online retail company
- Period: December 2010 - December 2011
- Contains: 541,909 transactions from 4,372 customers across 38 countries

**Features:**
- InvoiceNo: Invoice number
- StockCode: Product code
- Description: Product name
- Quantity: Quantity per transaction
- InvoiceDate: Transaction date and time
- UnitPrice: Product price per unit
- CustomerID: Unique customer identifier
- Country: Customer's country

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/online-retail-analysis.git
cd online-retail-analysis
```

### 2. Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download dataset
- Download from [Kaggle](https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset)
- Place `online_retail.csv` in `data/raw/` folder

## 📈 Usage

### Step 1: Data Cleaning
```bash
python notebooks/01_data_cleaning.py
```
**Output:** `data/processed/online_retail_cleaned.csv`

**What it does:**
- Removes cancelled orders
- Handles missing values
- Removes invalid quantities and prices
- Creates new features (TotalPrice, Year, Month, Hour, etc.)

### Step 2: Exploratory Data Analysis
```bash
python notebooks/02_exploratory_data_analysis.py
```
**Output:** 9 visualization charts in `outputs/` folder

**Analysis includes:**
- Revenue trends over time
- Top countries and products
- Customer behavior patterns
- Time-based analysis
- Cohort retention analysis

### Step 3: RFM Customer Segmentation
```bash
python notebooks/03_rfm_customer_segmentation.py
```
**Output:** 
- `data/processed/rfm_customer_segmentation.csv`
- 5 additional visualizations

**Segments customers into:**
- 🏆 Champions
- 💎 Loyal Customers
- 🌟 Potential Loyalists
- 🆕 Recent Customers
- ⚠️ Need Attention
- 🚨 At Risk
- 🆘 Can't Lose Them
- ❄️ Hibernating
- ⛔ Lost

### Step 4: Launch Interactive Dashboard
```bash
cd dashboard
streamlit run 04_streamlit_dashboard.py
```
**Access:** http://localhost:8501

## 📊 Key Findings

### Business Metrics
- **Total Revenue:** $8,887,209
- **Total Transactions:** 18,532
- **Total Customers:** 4,338
- **Average Order Value:** $479.56

### Insights
1. **Revenue Concentration:** Top 10% of customers contribute ~40% of total revenue
2. **Geographic Focus:** United Kingdom dominates with 82% of total revenue
3. **Seasonal Patterns:** Strong sales in Q4, peak in November
4. **Business Model:** B2B wholesale - operates Monday-Friday only
5. **Customer Retention:** ~30% retention rate after 3 months

### Recommendations
- Focus retention strategies on Champions and Loyal Customers
- Reactivate "At Risk" customers with personalized campaigns
- Expand marketing in top-performing international markets
- Optimize inventory for best-selling products
- Implement loyalty programs for Potential Loyalists

## 🛠️ Technologies Used

- **Python 3.8+**
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Dashboard:** Streamlit
- **Notebook:** Jupyter Notebook

## 📸 Dashboard Screenshots

### Key Performance Indicators
![KPI Dashboard](outputs/dashboard_kpi.png)

### RFM Customer Segmentation
![RFM Analysis](outputs/dashboard_rfm.png)

### Revenue Analysis
![Revenue Trends](outputs/dashboard_revenue.png)

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ End-to-end data analysis workflow
- ✅ Data cleaning and preprocessing techniques
- ✅ Exploratory Data Analysis (EDA)
- ✅ Customer segmentation using RFM analysis
- ✅ Data visualization best practices
- ✅ Building interactive dashboards
- ✅ Deriving actionable business insights

## 📝 Future Improvements

- [ ] Add predictive modeling (Customer Lifetime Value)
- [ ] Implement market basket analysis
- [ ] Create automated reporting pipeline
- [ ] Deploy dashboard to cloud (Streamlit Cloud / Heroku)
- [ ] Add A/B testing analysis
- [ ] Include time series forecasting

## 👤 Author

**Your Name**
- LinkedIn: [your-profile](https://linkedin.com/in/your-profile)
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset: [Online Retail Dataset on Kaggle](https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset)
- UCI Machine Learning Repository
- Streamlit community for dashboard inspiration

---

⭐ If you find this project helpful, please give it a star!
