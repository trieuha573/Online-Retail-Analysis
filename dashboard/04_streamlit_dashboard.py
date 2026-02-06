"""
E-Commerce Analytics Dashboard
Built with Streamlit
Save this as: 04_streamlit_dashboard.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import numpy as np

# ============================================================================
# PAGE CONFIG
# ============================================================================
st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
    }
    .stMetric label {
        color: #31333F !important;
        font-weight: 600 !important;
    }
    .stMetric [data-testid="stMetricValue"] {
        color: #0068C9 !important;
        font-size: 2rem !important;
        font-weight: bold !important;
    }
    .stMetric [data-testid="stMetricDelta"] {
        color: #09AB3B !important;
    }
    h1 {
        color: #1f77b4;
    }
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# LOAD DATA
# ============================================================================
@st.cache_data
def load_data():
    df = pd.read_csv('../data/processed/online_retail_cleaned.csv')
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['YearMonth'] = pd.to_datetime(df['YearMonth'])
    
    rfm = pd.read_csv('../data/processed/rfm_customer_segmentation.csv')
    
    return df, rfm

try:
    df, rfm = load_data()
except:
    st.error("⚠️ Error loading data! Please run data cleaning and RFM analysis scripts first.")
    st.stop()

# ============================================================================
# SIDEBAR FILTERS
# ============================================================================
st.sidebar.header("🔍 Filters")

# Date range filter
min_date = df['InvoiceDate'].min().date()
max_date = df['InvoiceDate'].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Country filter
countries = ['All'] + sorted(df['Country'].unique().tolist())
selected_country = st.sidebar.selectbox("Select Country", countries)

# Apply filters
if len(date_range) == 2:
    df_filtered = df[(df['InvoiceDate'].dt.date >= date_range[0]) & 
                     (df['InvoiceDate'].dt.date <= date_range[1])]
else:
    df_filtered = df

if selected_country != 'All':
    df_filtered = df_filtered[df_filtered['Country'] == selected_country]

# ============================================================================
# MAIN DASHBOARD
# ============================================================================
st.title("📊 E-Commerce Analytics Dashboard")
st.markdown("---")

# ============================================================================
# KPI METRICS
# ============================================================================
st.header("📈 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

total_revenue = df_filtered['TotalPrice'].sum()
total_transactions = df_filtered['InvoiceNo'].nunique()
total_customers = df_filtered['CustomerID'].nunique()
avg_order_value = total_revenue / total_transactions if total_transactions > 0 else 0

with col1:
    st.metric(
        label="💰 Total Revenue",
        value=f"${total_revenue:,.0f}",
        delta=f"{(total_revenue/df['TotalPrice'].sum()*100):.1f}% of total"
    )

with col2:
    st.metric(
        label="🛒 Total Transactions",
        value=f"{total_transactions:,}",
        delta=f"{(total_transactions/df['InvoiceNo'].nunique()*100):.1f}% of total"
    )

with col3:
    st.metric(
        label="👥 Total Customers",
        value=f"{total_customers:,}",
        delta=f"{(total_customers/df['CustomerID'].nunique()*100):.1f}% of total"
    )

with col4:
    st.metric(
        label="💵 Avg Order Value",
        value=f"${avg_order_value:,.2f}",
        delta="Per Transaction"
    )

st.markdown("---")

# ============================================================================
# REVENUE ANALYSIS
# ============================================================================
st.header("💰 Revenue Analysis")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Monthly Revenue Trend")
    monthly_revenue = df_filtered.groupby(df_filtered['InvoiceDate'].dt.to_period('M'))['TotalPrice'].sum().reset_index()
    monthly_revenue['InvoiceDate'] = monthly_revenue['InvoiceDate'].astype(str)
    
    fig = px.line(monthly_revenue, x='InvoiceDate', y='TotalPrice',
                  labels={'InvoiceDate': 'Month', 'TotalPrice': 'Revenue ($)'},
                  markers=True)
    fig.update_traces(line_color='#1f77b4', line_width=3)
    fig.update_layout(hovermode='x unified', height=400)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🌍 Top 10 Countries by Revenue")
    country_revenue = df_filtered.groupby('Country')['TotalPrice'].sum().nlargest(10).reset_index()
    
    fig = px.bar(country_revenue, x='TotalPrice', y='Country',
                 labels={'TotalPrice': 'Revenue ($)', 'Country': 'Country'},
                 orientation='h',
                 color='TotalPrice',
                 color_continuous_scale='Blues')
    fig.update_layout(showlegend=False, height=400, yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)

# Revenue by Day of Week
st.subheader("📅 Revenue by Day of Week")
dayofweek_revenue = df_filtered.groupby('DayName')['TotalPrice'].sum().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
], fill_value=0)

fig = px.bar(x=dayofweek_revenue.index, y=dayofweek_revenue.values,
             labels={'x': 'Day of Week', 'y': 'Revenue ($)'},
             color=dayofweek_revenue.values,
             color_continuous_scale='Viridis')
fig.update_layout(showlegend=False, height=400)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================================================================
# PRODUCT ANALYSIS
# ============================================================================
st.header("📦 Product Analysis")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top 10 Products by Revenue")
    product_revenue = df_filtered.groupby(['StockCode', 'Description']).agg({
        'TotalPrice': 'sum',
        'Quantity': 'sum'
    }).reset_index()
    product_revenue = product_revenue.nlargest(10, 'TotalPrice')
    
    product_revenue['Description_Short'] = product_revenue['Description'].apply(
        lambda x: x[:30] + '...' if len(x) > 30 else x
    )
    
    fig = px.bar(product_revenue, x='TotalPrice', y='Description_Short',
                 labels={'TotalPrice': 'Revenue ($)', 'Description_Short': 'Product'},
                 orientation='h',
                 color='TotalPrice',
                 color_continuous_scale='Greens')
    fig.update_layout(showlegend=False, height=400, yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📊 Top 10 Products by Quantity Sold")
    product_quantity = df_filtered.groupby(['StockCode', 'Description']).agg({
        'Quantity': 'sum',
        'TotalPrice': 'sum'
    }).reset_index()
    product_quantity = product_quantity.nlargest(10, 'Quantity')
    
    product_quantity['Description_Short'] = product_quantity['Description'].apply(
        lambda x: x[:30] + '...' if len(x) > 30 else x
    )
    
    fig = px.bar(product_quantity, x='Quantity', y='Description_Short',
                 labels={'Quantity': 'Quantity Sold', 'Description_Short': 'Product'},
                 orientation='h',
                 color='Quantity',
                 color_continuous_scale='Oranges')
    fig.update_layout(showlegend=False, height=400, yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================================================================
# CUSTOMER ANALYSIS
# ============================================================================
st.header("👥 Customer Analysis")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🌟 Top 20 Customers by Revenue")
    customer_revenue = df_filtered.groupby('CustomerID')['TotalPrice'].sum().nlargest(20).reset_index()
    
    # Format Customer ID for better display
    customer_revenue['Customer_Label'] = 'C-' + customer_revenue['CustomerID'].astype(str)
    customer_revenue['CustomerID_str'] = customer_revenue['CustomerID'].astype(str)
    
    fig = px.bar(customer_revenue, x='Customer_Label', y='TotalPrice',
                 labels={'Customer_Label': 'Customer ID', 'TotalPrice': 'Revenue ($)'},
                 color='TotalPrice',
                 color_continuous_scale='Purples',
                 hover_data={'CustomerID_str': True, 'TotalPrice': ':$,.2f'})
    fig.update_layout(showlegend=False, height=400, xaxis_tickangle=-45)
    fig.update_traces(hovertemplate='<b>Customer: %{customdata[0]}</b><br>Revenue: %{y:$,.2f}<extra></extra>')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📊 Customer Purchase Frequency Distribution")
    customer_freq = df_filtered.groupby('CustomerID')['InvoiceNo'].nunique()
    
    fig = px.histogram(x=customer_freq.values, nbins=50,
                       labels={'x': 'Number of Transactions', 'y': 'Number of Customers'},
                       color_discrete_sequence=['#ff7f0e'])
    fig.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================================================================
# RFM SEGMENTATION
# ============================================================================
st.header("🎯 Customer Segmentation (RFM Analysis)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("👥 Customer Segments Distribution")
    segment_counts = rfm['Segment'].value_counts().reset_index()
    segment_counts.columns = ['Segment', 'Count']
    
    fig = px.pie(segment_counts, values='Count', names='Segment',
                 hole=0.4,
                 color_discrete_sequence=px.colors.qualitative.Set3)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("💰 Revenue by Customer Segment")
    segment_revenue = rfm.groupby('Segment')['Monetary'].sum().sort_values(ascending=False).reset_index()
    
    fig = px.bar(segment_revenue, x='Segment', y='Monetary',
                 labels={'Segment': 'Customer Segment', 'Monetary': 'Total Revenue ($)'},
                 color='Monetary',
                 color_continuous_scale='Teal')
    fig.update_layout(showlegend=False, height=500, xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

# RFM 3D Scatter
st.subheader("📍 RFM 3D Distribution")
rfm_sample = rfm.sample(n=min(1000, len(rfm)), random_state=42)

fig = go.Figure(data=[go.Scatter3d(
    x=rfm_sample['Recency'],
    y=rfm_sample['Frequency'],
    z=rfm_sample['Monetary'],
    mode='markers',
    marker=dict(
        size=5,
        color=rfm_sample['RFM_Score_Numeric'],
        colorscale='Viridis',
        showscale=True,
        colorbar=dict(title="RFM Score"),
        line=dict(color='white', width=0.5)
    ),
    text=rfm_sample['Segment'],
    hovertemplate='<b>%{text}</b><br>' +
                  'Recency: %{x} days<br>' +
                  'Frequency: %{y}<br>' +
                  'Monetary: $%{z:,.2f}<br>' +
                  '<extra></extra>'
)])

fig.update_layout(
    scene=dict(
        xaxis_title='Recency (days)',
        yaxis_title='Frequency',
        zaxis_title='Monetary ($)'
    ),
    height=600
)
st.plotly_chart(fig, use_container_width=True)

# Segment Details Table
st.subheader("📋 Segment Summary Table")
segment_summary = rfm.groupby('Segment').agg({
    'CustomerID': 'count',
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': ['mean', 'sum']
}).round(2)
segment_summary.columns = ['Count', 'Avg_Recency', 'Avg_Frequency', 'Avg_Monetary', 'Total_Revenue']
segment_summary = segment_summary.sort_values('Total_Revenue', ascending=False)
segment_summary['Revenue_%'] = (segment_summary['Total_Revenue'] / segment_summary['Total_Revenue'].sum() * 100).round(2)

st.dataframe(segment_summary, use_container_width=True)

st.markdown("---")

# ============================================================================
# TIME ANALYSIS
# ============================================================================
st.header("⏰ Time-Based Analysis")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🕐 Hourly Sales Pattern")
    hourly_sales = df_filtered.groupby('Hour')['TotalPrice'].sum().reset_index()
    
    fig = px.line(hourly_sales, x='Hour', y='TotalPrice',
                  labels={'Hour': 'Hour of Day', 'TotalPrice': 'Revenue ($)'},
                  markers=True)
    fig.update_traces(line_color='#ff7f0e', line_width=3)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📆 Monthly Transaction Count")
    monthly_transactions = df_filtered.groupby(df_filtered['InvoiceDate'].dt.to_period('M'))['InvoiceNo'].nunique().reset_index()
    monthly_transactions['InvoiceDate'] = monthly_transactions['InvoiceDate'].astype(str)
    
    fig = px.bar(monthly_transactions, x='InvoiceDate', y='InvoiceNo',
                 labels={'InvoiceDate': 'Month', 'InvoiceNo': 'Number of Transactions'},
                 color='InvoiceNo',
                 color_continuous_scale='Reds')
    fig.update_layout(showlegend=False, height=400, xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>📊 E-Commerce Analytics Dashboard | Built with Streamlit & Plotly</p>
        <p>Data Source: Online Retail Dataset (UK-based)</p>
    </div>
    """, unsafe_allow_html=True)