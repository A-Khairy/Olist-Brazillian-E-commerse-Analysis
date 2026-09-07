# 📊 Olist Brazilian E-Commerce: Business Intelligence & Operations Analytics

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-Data%20Cleaning-orange?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![PowerBI](https://img.shields.io/badge/Power_BI-Dashboard-yellow?logo=powerbi&logoColor=white)](https://powerbi.microsoft.com/)

An end-to-end data analytics project evaluating order fulfillment, customer satisfaction, payment behaviors, and delivery logistics across 100k+ orders from the Olist Brazilian E-commerce platform.

---

## 📌 Executive Summary

Olist operates a marketplace connecting small merchants across Brazil to major e-commerce channels. This project addresses critical operational bottlenecks:
* **Logistics & Delivery Delays:** Analyzing SLA breaches and transit times across Brazilian states.
* **Customer Retention & Review Sentiment:** Investigating drivers behind low review scores and product return patterns.
* **Revenue & Merchandising Insights:** Identifying top-performing product categories and payment distribution preferences.

---

## 🛠️ Tech Stack & Workflow

* **SQL:** Multi-table data cleaning, whitespace normalization, handling `NULL` records, and schema joins.
* **Python (Pandas, NumPy):** Exploratory data analysis (EDA), statistical distribution profiling, and data extraction pipelines.
* **Power BI:** Interactive multi-page dashboard, DAX measures, star schema data modeling, and operational KPI reporting.

```mermaid
flowchart TD
    A["Raw Data: Olist CSV Datasets"] --> B["SQL Transformations & Data Cleaning"]
    B --> C["Python EDA & Feature Extraction"]
    C --> D["Power BI Star Schema & Data Modeling"]
    D --> E["Interactive Executive & Operational Dashboards"]

    📈 Key Insights & Business Findings
Delivery Performance vs. Customer Satisfaction: Orders delivered after the estimated SLA date experienced an immediate ~70% drop in review scores (averaging 1.4 stars vs. 4.3 stars for on-time deliveries).

Payment Preference: Credit card installments account for over 70% of total payment volume, with higher average order value (AOV) on orders split into 4+ installments.

Regional Logistics Imbalance: Southeastern states (SP, RJ, MG) account for over 60% of total volume with fastest fulfillment times, while North/Northeastern routes exhibit severe transit delays.

📊 Dashboard Preview
(Interactive dashboard file available under dashboards/olist_powerbi_final.pbix)

📂 Repository Structure
├── dashboards/
│   └── olist_powerbi_final.pbix
├── notebooks/
│   ├── Ecommerce_Project.ipynb
│   ├── Export_data_from_sql.py
│   └── app.py
├── reports/
│   ├── images/
│   └── Brazilian-E-Commerce-Data-Analysis-Olist-Dataset.pptx
├── scripts/
│   ├── Data Cleaning - Null.sql
│   ├── Data Cleaning - Spaces.sql
│   └── Data Cleaning.sql
├── .gitignore
├── requirements.txt
└── README.md

🚀 Getting Started

1. Prerequisites
Python 3.10+

SQL Server or PostgreSQL

Microsoft Power BI Desktop

2. Installation

git clone [https://github.com/A-Khairy/Olist-Brazillian-E-commerse-Analysis.git](https://github.com/A-Khairy/Olist-Brazillian-E-commerse-Analysis.git)
cd Olist-Brazillian-E-commerse-Analysis
pip install -r requirements.txt

3. Running SQL Scripts
Execute the scripts in scripts/ sequentially to clean and prepare your relational database tables:

1-Data Cleaning - Spaces.sql

2-Data Cleaning - Null.sql

3-Data Cleaning.sql

sql
