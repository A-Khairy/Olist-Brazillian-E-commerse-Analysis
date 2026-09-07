
# app.py - Clean Streamlit dashboard for Olist Ecommerce
# Requirements: streamlit, pandas, pyodbc, plotly
# Replace SERVER name below with your SQL Server instance if needed.

import streamlit as st
import pandas as pd
import pyodbc
import plotly.express as px

st.set_page_config(page_title="Olist Ecommerce Dashboard", layout="wide")
st.title("📊 Olist Ecommerce Dashboard")

@st.cache_data
def load_data():
    """
    Connect to SQL Server and load the main tables used for visualization.
    Edit the SERVER value if your SQL Server instance name is different.
    """
    conn = None
    try:
        conn = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=SasakiKojiro;'
            'DATABASE=Olist_Ecommerce;'
            'Trusted_Connection=yes;'
        )
    except Exception as e:
        st.error(f"Could not connect to SQL Server: {e}")
        return None, None, None, None, None, None

    # Read only necessary columns to improve performance
    df_orders = pd.read_sql("""
        SELECT order_id, customer_id, order_status, order_purchase_timestamp, order_delivered_customer_date
        FROM orders_dataset
    """, conn)

    df_items = pd.read_sql("""
        SELECT order_id, product_id, seller_id, price, freight_value
        FROM order_items_dataset
    """, conn)

    df_customers = pd.read_sql("""
        SELECT customer_id, customer_unique_id, customer_state, customer_city
        FROM customers_dataset
    """, conn)

    df_products = pd.read_sql("""
        SELECT product_id, product_category_name
        FROM products_dataset
    """, conn)

    df_reviews = pd.read_sql("""
        SELECT order_id, review_score
        FROM order_reviews_dataset
    """, conn)

    df_payments = pd.read_sql("""
        SELECT order_id, payment_type
        FROM order_payments_dataset
    """, conn)

    conn.close()
    return df_orders, df_items, df_customers, df_products, df_reviews, df_payments

# Load data
df_orders, df_items, df_customers, df_products, df_reviews, df_payments = load_data()
if df_orders is None:
    st.stop()

st.success("✅ Data loaded successfully from SQL Server!")

# Simple data preprocessing
df_orders['order_purchase_timestamp'] = pd.to_datetime(df_orders['order_purchase_timestamp'], errors='coerce')
df_orders['order_delivered_customer_date'] = pd.to_datetime(df_orders['order_delivered_customer_date'], errors='coerce')

# KPIs
total_orders = df_orders['order_id'].nunique()
total_revenue = (df_items['price'].fillna(0) + df_items['freight_value'].fillna(0)).sum()
unique_customers = df_customers['customer_unique_id'].nunique()
avg_review = df_reviews['review_score'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("🛒 Total Orders", int(total_orders))
col2.metric("💰 Total Revenue", f"${total_revenue:,.2f}")
col3.metric("👥 Unique Customers", int(unique_customers))
col4.metric("⭐ Average Review", f"{avg_review:.2f}" if pd.notnull(avg_review) else "N/A")

st.markdown("---")

# Filters (slicers)
st.sidebar.header("Filters")
selected_status = st.sidebar.multiselect("Order Status", options=sorted(df_orders['order_status'].dropna().unique()), default=[])
selected_category = st.sidebar.multiselect("Category", options=sorted(df_products['product_category_name'].dropna().unique()), default=[])
selected_state = st.sidebar.multiselect("State", options=sorted(df_customers['customer_state'].dropna().unique()), default=[])

# Apply filters by building masks
mask_orders = pd.Series(True, index=df_orders.index)
if selected_status:
    mask_orders &= df_orders['order_status'].isin(selected_status)

# Merge items->orders->customers->products for filtering and visuals
df_items_orders = pd.merge(df_items, df_orders[mask_orders], on='order_id', how='inner')
df_items_orders_customers = pd.merge(df_items_orders, df_customers, on='customer_id', how='left')
df_items_products = pd.merge(df_items, df_products, on='product_id', how='left')
df_items_orders_products = pd.merge(df_items_orders, df_products, on='product_id', how='left')

if selected_state:
    df_items_orders_customers = df_items_orders_customers[df_items_orders_customers['customer_state'].isin(selected_state)]

if selected_category:
    df_items_orders_products = df_items_orders_products[df_items_orders_products['product_category_name'].isin(selected_category)]
    df_items_orders = df_items_orders.merge(df_products[['product_id','product_category_name']], on='product_id', how='left')
    df_items_orders = df_items_orders[df_items_orders['product_category_name'].isin(selected_category)]

# Sales Trend (Line chart)
st.subheader("📈 Sales Trend Over Time")
monthly = df_orders[mask_orders].copy()
monthly['month'] = monthly['order_purchase_timestamp'].dt.to_period('M')
monthly_sales = monthly.groupby('month').size().reset_index(name='Orders')
monthly_sales['month'] = monthly_sales['month'].dt.to_timestamp()
st.line_chart(monthly_sales.set_index('month')['Orders'])

st.markdown("---")

# Top Product Categories by Revenue
st.subheader("🏆 Top Product Categories by Revenue")
df_items_products = pd.merge(df_items, df_products, on='product_id', how='left')
category_sales = (
    df_items_products.groupby('product_category_name')[['price','freight_value']]
    .sum()
    .reset_index()
)
category_sales['Total_Revenue'] = category_sales['price'].fillna(0) + category_sales['freight_value'].fillna(0)
top_categories = category_sales.sort_values(by='Total_Revenue', ascending=False).head(10)
fig_cat = px.bar(top_categories, x='product_category_name', y='Total_Revenue',
                 labels={'product_category_name':'Category','Total_Revenue':'Revenue'},
                 title="Top 10 Categories")
fig_cat.update_layout(xaxis_tickangle=-45, showlegend=False)
st.plotly_chart(fig_cat, use_container_width=True)

st.markdown("---")

# Revenue by State (bar chart)
st.subheader("🌎 Revenue by State")
revenue_by_state = (
    df_items_orders_customers.groupby('customer_state')[['price','freight_value']]
    .sum()
    .reset_index()
)
revenue_by_state['Total_Revenue'] = revenue_by_state['price'].fillna(0) + revenue_by_state['freight_value'].fillna(0)
fig_state = px.bar(revenue_by_state.sort_values('Total_Revenue', ascending=False),
                   x='customer_state', y='Total_Revenue', labels={'customer_state':'State','Total_Revenue':'Revenue'})
st.plotly_chart(fig_state, use_container_width=True)

st.markdown("---")

# Payment Types Distribution
st.subheader("💳 Payment Type Distribution")
payment_distribution = df_payments.merge(df_orders[['order_id']], on='order_id', how='inner')
payment_counts = payment_distribution['payment_type'].value_counts().reset_index()
payment_counts.columns = ['Payment_Type','Count']
fig_payment = px.pie(payment_counts, names='Payment_Type', values='Count', hole=0.5,
                     title="Payment Types")
fig_payment.update_traces(textinfo='percent+label')
st.plotly_chart(fig_payment, use_container_width=True)

st.markdown("---")

# Customer Review Ratings
st.subheader("⭐ Customer Review Ratings Distribution")
review_dist = df_reviews['review_score'].value_counts().reset_index()
review_dist.columns = ['Review_Score','Count']
review_dist = review_dist.sort_values('Review_Score')
fig_reviews = px.bar(review_dist, x='Review_Score', y='Count', labels={'Review_Score':'Score','Count':'Count'},
                     title="Review Scores", color='Review_Score', color_continuous_scale=px.colors.sequential.Viridis)
fig_reviews.update_layout(showlegend=False)
st.plotly_chart(fig_reviews, use_container_width=True)

# Footer
st.markdown("---")
st.write("Built with Streamlit • Data source: Olist_Ecommerce (SQL Server)")
