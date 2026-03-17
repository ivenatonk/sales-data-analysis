# 📊 Sales Data Analysis

A beginner-friendly data analysis project using **Excel** and **Python** to analyse monthly sales data across products, regions, and sales representatives.

---

## 📁 Project Structure
```
sales-data-analysis/
├── data/
│   └── sales_data.csv        # Raw sales dataset
├── excel/
│   └── sales_analysis.xlsx   # Excel pivot tables and charts
├── python/
│   └── analysis.py           # Python analysis script
├── charts/
│   └── *.png                 # All generated charts
└── README.md
```

---

## 📋 Dataset Overview

The dataset contains **30 sales records** from January to June with the following columns:

| Column | Description |
|--------|-------------|
| Order_ID | Unique order identifier |
| Month | Month of the sale |
| Product | Product sold |
| Category | Product category |
| Region | Sales region |
| Units_Sold | Number of units sold |
| Unit_Price | Price per unit |
| Total_Revenue | Total revenue generated |
| Sales_Rep | Sales representative name |

---

## 🔍 Key Insights

- 💰 **Total Revenue:** $69,080
- 📅 **Best Month:** April ($13,120)
- 🌍 **Best Region:** West
- 🏆 **Best Product:** Laptop
- 👤 **Top Sales Rep:** David

---

## 📊 Charts

### Monthly Revenue Trend
[![Monthly Revenue Trend](https://github.com/ivenatonk/sales-data-analysis/blob/main/data/excel/python/charts/monthly_trend_py.png?raw=true)

### Revenue by Category
![Revenue by Category](https://github.com/ivenatonk/sales-data-analysis/blob/main/data/excel/python/charts/revenue_by_category_py.png?raw=true)

### Revenue by Region
![Revenue by Region](https://github.com/ivenatonk/sales-data-analysis/blob/main/data/excel/python/charts/revenue_by_region_py.png?raw=true
))

### Revenue by Sales Rep
![Revenue by Sales Rep](https://github.com/ivenatonk/sales-data-analysis/blob/main/data/excel/python/charts/revenue_by_sales_rep_py.png?raw=true)

---

## 🛠️ Tools Used

- **Microsoft Excel** — Pivot tables and charts
- **Python 3** — Data analysis and visualisation
- **Pandas** — Data manipulation
- **Matplotlib** — Chart generation

---

## 🚀 How to Run the Python Script

1. Clone this repository
2. Make sure you have Python installed
3. Install dependencies:
```
   pip install pandas matplotlib openpyxl
```
4. Run the script:
```
   python python/analysis.py
```

---

## 👤 Author

**ivenatonk** — Beginner Data Analyst
