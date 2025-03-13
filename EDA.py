import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Chiranth\OneDrive\Documents\codes\Ecommerce_Delivery_Analytics_New.csv")

unique_orders = df.groupby('Customer ID').agg({'Order ID': 'nunique'}).reset_index()

high_order_users = unique_orders[unique_orders['Order ID'] > 10]

top_user = high_order_users.sort_values('Order ID', ascending=False).iloc[0]
print("Top user with highest multiple orders:", top_user)

platform_sales = df.groupby('Platform')['Order ID'].nunique().reset_index()

# Bar plot for unique sales by platform
plt.figure(figsize=(10, 6))
sns.barplot(x='Platform', y='Order ID', data=platform_sales, palette='muted')
plt.ylim(32000, 34000)
plt.yticks(range(32000, 34001, 100))
plt.title('Unique Sales by Platform')
plt.xlabel('Platform')
plt.ylabel('Unique Sales')
plt.show()

df['Order Date & Time'] = pd.to_datetime(df['Order Date & Time'],errors='coerce')

df['Year'] = df['Order Date & Time'].dt.year
df['Month'] = df['Order Date & Time'].dt.month
df['Week'] = df['Order Date & Time'].dt.isocalendar().week

yearly_orders = df.groupby('Year')['Order ID'].count()
print("Yearly Order Analysis:", yearly_orders)

monthly_orders = df.groupby(['Year', 'Month'])['Order ID'].count()
print("Monthly Order Analysis:", monthly_orders)

weekly_orders = df.groupby(['Year', 'Week'])['Order ID'].count()
print("Weekly Order Analysis:", weekly_orders)

platform_performance = df.groupby('Platform')['Order ID'].count().reset_index().sort_values('Order ID', ascending=False)

best_platform = platform_performance.iloc[0]
least_platform = platform_performance.iloc[-1]

print(f"Best performing platform: {best_platform['Platform']} with {best_platform['Order ID']} orders.")
print(f"Least performing platform: {least_platform['Platform']} with {least_platform['Order ID']} orders.")

top_10_products = df.groupby('Product Category')['Service Rating'].mean().sort_values(ascending=False).head(10)
print("Top 10 Highest Rated Products:", top_10_products)

lowest_5_products = df.groupby('Product Category')['Service Rating'].mean().sort_values().head(5)
print("Top 5 Lowest Rated Products:", lowest_5_products)

status_counts = df['Delivery Delay'].value_counts(normalize=True) * 100

print("Order Status Analysis (in %):", status_counts)

plt.figure(figsize=(8, 6))
status_counts.plot(kind='bar', color=['green', 'red', 'orange'])
plt.title('Order Status Distribution')
plt.xlabel('Delivery Status')
plt.ylabel('Percentage (%)')
plt.show()

for platform in df['Platform'].unique():
    platform_data = df[df['Platform'] == platform]

    avg_rating = platform_data['Service Rating'].mean()


    print(f"\nPlatform: {platform}")
    print(f"Average Rating: {avg_rating:.2f}")


    if avg_rating < 3:
        print(f"Suggestion: Improve customer satisfaction on {platform} by addressing common complaints.")
