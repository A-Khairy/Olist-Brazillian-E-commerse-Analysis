# 📊 Olist Brazilian E-Commerce: Business Intelligence & Operations Analytics

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-Data%20Cleaning-orange?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![PowerBI](https://img.shields.io/badge/Power_BI-Dashboard-yellow?logo=powerbi&logoColor=white)](https://powerbi.microsoft.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

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

```text
Raw Data (Olist CSVs) 
       │
       ▼
SQL Cleaning & Transformation (NULLs, Whitespaces, Data Validation)
       │
       ▼
Python EDA & Feature Extraction (Pandas, NumPy)
       │
       ▼
Power BI Star Schema & Executive Dashboard
📈 Key Insights & Business Findings
Delivery Performance vs. Customer Satisfaction: Orders delivered after the estimated SLA date experienced an immediate ~70% drop in review scores (averaging 1.4 stars vs. 4.3 stars for on-time deliveries).

Payment Preference: Credit card installments account for over 70% of total payment volume, with higher average order value (AOV) on orders split into 4+ installments.

Regional Logistics Imbalance: Southeastern states (SP, RJ, MG) account for over 60% of total volume with fastest fulfillment times, while North/Northeastern routes exhibit severe transit delays.

📊 Dashboard Preview
(Dashboard file available under dashboards/olist_powerbi_final.pbix)
📂 Repository Structure
├── dashboards/
│   └── olist_powerbi_final.pbix      # Interactive Power BI report & data model
├── notebooks/
│   ├── Ecommerce_Project.ipynb      # End-to-end EDA and metric exploration
│   ├── Export_data_from_sql.py       # SQL database extraction script
│   └── app.py                       # Helper processing script
├── reports/
│   ├── images/                       # Dashboard screenshots and report assets
│   └── Brazilian-E-Commerce-...pptx  # Stakeholder presentation deck
├── scripts/
│   ├── Data Cleaning - Null.sql      # Handling missing values across tables
│   ├── Data Cleaning - Spaces.sql    # Normalizing string and categorical fields
│   └── Data Cleaning.sql             # Relational transformations and joins
├── .gitignore
├── requirements.txt
└── README.md
🚀 Getting Started
1. Prerequisites
Python 3.10+

SQL Server or PostgreSQL

Microsoft Power BI Desktop

2. Installation
Clone the repository:
git clone [https://github.com/A-Khairy/Olist-Brazillian-E-commerse-Analysis.git](https://github.com/A-Khairy/Olist-Brazillian-E-commerse-Analysis.git)
cd Olist-Brazillian-E-commerse-Analysis
Install Python dependencies:
pip install -r requirements.txt
3. Running SQL Scripts
Execute the scripts in scripts/ sequentially to clean and prepare your relational database tables:

Data Cleaning - Spaces.sql

Data Cleaning - Null.sql

Data Cleaning.sql
👤 Author
Ahmed Khairy

LinkedIn: linkedin.com/in/ahmedkhairy23

GitHub: @A-Khairy

Email: ahmedkhairey70@gmail.com