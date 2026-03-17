import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('sales_data.csv')
print("Data loaded successfully!")
print("Total rows:", len(df))

print("\nFirst 5 rows:")
print(df.head())

print("\nBasic Summary:")
print("Total Revenue: $" + str(df['Total_Revenue'].sum()))
print("Average Revenue: $" + str(round(df['Total_Revenue'].mean(), 1)))
print("Best Month: " + df.groupby('Month')['Total_Revenue'].sum().idxmax())
print("Best Region: " + df.groupby('Region')['Total_Revenue'].sum().idxmax())
print("Best Product: " + df.groupby('Product')['Total_Revenue'].sum().idxmax())

os.makedirs('charts', exist_ok=True)

month_order = ['January','February','March','April','May','June']
monthly = df.groupby('Month')['Total_Revenue'].sum().reindex(month_order)

plt.figure(figsize=(10, 5))
plt.plot(monthly.index, monthly.values, marker='o', color='steelblue', linewidth=2.5)
plt.fill_between(monthly.index, monthly.values, alpha=0.1, color='steelblue')
plt.title('Monthly Revenue Trend', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/monthly_trend_py.png', dpi=150)
plt.close()
print("Chart 1 saved")

category = df.groupby('Category')['Total_Revenue'].sum()
plt.figure(figsize=(7, 7))
plt.pie(category.values, labels=category.index, autopct='%1.1f%%',
        colors=['#4C72B0','#DD8452','#55A868'], startangle=140)
plt.title('Revenue by Category', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('charts/revenue_by_category_py.png', dpi=150)
plt.close()
print("Chart 2 saved")

region = df.groupby('Region')['Total_Revenue'].sum().sort_values()
plt.figure(figsize=(8, 5))
plt.barh(region.index, region.values, color='#4C72B0')
plt.title('Revenue by Region', fontsize=16, fontweight='bold')
plt.xlabel('Total Revenue ($)', fontsize=12)
plt.tight_layout()
plt.savefig('charts/revenue_by_region_py.png', dpi=150)
plt.close()
print("Chart 3 saved")

rep = df.groupby('Sales_Rep')['Total_Revenue'].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
plt.bar(rep.index, rep.values, color=['#4C72B0','#DD8452','#55A868','#C44E52'])
plt.title('Revenue by Sales Rep', fontsize=16, fontweight='bold')
plt.xlabel('Sales Rep', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.tight_layout()
plt.savefig('charts/revenue_by_sales_rep_py.png', dpi=150)
plt.close()
print("Chart 4 saved")

print("\nAll done! Check your charts folder.")