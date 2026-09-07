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
    A[Raw Data: Olist CSVs] --> B[SQL Transformations & Cleaning]
    B --> C[Python EDA & Metric Extraction]
    C --> D[Power BI Star Schema Modeling]
    D --> E[Interactive Executive Dashboards]
