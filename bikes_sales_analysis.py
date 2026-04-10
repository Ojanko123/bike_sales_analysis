Lab 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sales = pd.read_csv("C:\\Users\\ojank\\Desktop\\Biostatistics\\bikesales.csv")
print(sales)
sales.head()
#Density plot and Box plot for the Customer's Age
sales['Customer_Age'].mean()
sales["Customer_Age"].plot(kind= 'kde',figsize = (14,6),
     color="darkblue")   
plt.title("Density plot of the mean age of a customer",fontsize= 14)
plt.xlabel("Age",fontsize=12)
plt.show() 
sales ['Customer_Age'].plot(kind= "box", vert= False, figsize=(14,6),
        color = "darkblue",)
plt.title("Boxplot of Customer Age", fontsize=14)
plt.show()
#Histogram for Order Quantity
sales['Order_Quantity'].mean()
plt.figure(figsize=(14, 6))
sales['Order_Quantity'].plot( 
    kind='hist',
    bins=30,
    edgecolor='black',
    alpha=0.7)
plt.title('Distribution of Order Quantity', fontsize=16)
plt.xlabel('Order Quantity')
plt.ylabel('Frequency')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
#Box plot for Order Quantity
plt.figure(figsize = (12,6))
sales['Order_Quantity'].plot(kind = 'box',
         vert=False,
         patch_artist = True,
         boxprops=dict(facecolor='lightblue', alpha = 0.7, edgecolor = 'black'),
         medianprops= dict(color= 'red' ,linewidth= 2),
         whiskerprops= dict(color = 'black'),
         capprops = dict(color='black'),
         flierprops = dict(marker='o',markersize= 4,alpha = 0.5)
)
plt.title('Boxplot of Order Quantity',fontsize = 16)
plt.ylabel('Order Quantity')
plt.grid(True, linestyle='--', alpha= 0.5)
plt.show()
#Pie chart for sales per year
year_counts= sales['Year'].value_counts().sort_index()
print(year_counts)
plt.figure(figsize = (20,27))
year_counts.plot(kind='pie',
                 figsize=(6,6),
                 autopct='%1.1f%%',
                 startangle=90,
                 shadow=True,
                 explode=[0.05]*len(year_counts),
                 colors=("purple",'red','lightblue','orange','grey'),)
plt.title("Sales per Year", fontsize=14, weight='bold')
plt.show()
#Relationship between profit per country
import seaborn as sns 
sns.set_style('whitegrid')
plt.figure(figsize= (14,18))
sns.scatterplot(data = sales,
                x= 'Order_Quantity',
                y = 'Profit',
                hue = 'Country',
                palette= 'tab20',
                s=100,
                alpha=0.7)
plt.xlabel('Order Quantity',fontsize = 12)
plt.ylabel('Profit',fontsize = 12)
plt.title('Relationship Between Order Quantity and Profit per Country', fontsize = 16)
plt.legend(title = 'Country',bbox_to_anchor=(1.05,1),loc= 'upper left')
plt.tight_layout
plt.show()
#Normality Test on Country and Order Quantity In order to apply a linear reggression analysis and examine a possible correlation
from scipy import stats
price = sales['Order_Quantity']
mean_price= price.mean()
std_price = price.std()
ks_stat, ks_p = stats.kstest(price, 'norm', args=(mean_price,std_price)) #Kolmogorov-Smirnoff Test
print(f"Kolmogorov-Smirnov test: statistic={ks_stat}, p-value={ks_p}")
ad_result = stats.anderson(price,dist='norm')
print(ad_result) #Anderson-Darling test
#for countries
country_mapping = {country: i for i, country in enumerate(sales['Country'].unique(), start=1)}
sales['Country_Num'] = sales['Country'].map(country_mapping)
print(sales[['Country', 'Country_Num']].head())  # we need to make it numeric 
ks_stat, ks_p = stats.kstest(sales['Country_Num'], 'norm', args=(sales['Country_Num'].mean(), sales['Country_Num'].std()))
print(print(f"KS test p-value:statistic={ks_stat}  {ks_p:.20f}"))
#According to our p-value and in a 95% confidence level there is a strong indication that variables: Country and Sales do not follow normal distribution 
#Therefore we cant apply a simple linear reggression

#Country with the most quantity of sales
sales_per_country= sales['Country'].value_counts()
top_country = sales_per_country.idxmax()
top_sales = sales_per_country.max()
print(f'Top Country: {top_country} with {top_sales} sales')
print('\nSales per Country:')
print(sales_per_country)
#Barplot for the countries with the most quantity of sales
sns.set_style('whitegrid')
plt.figure(figsize = (14,6))
sns.barplot(x= sales_per_country.index, y= sales_per_country.values, palette='viridis')
plt.xlabel('Country',fontsize = 12)
plt.ylabel("Number of Sales", fontsize= 12)
plt.title("Quantity of Sales per Country", fontsize = 16)
plt.xticks(rotation= 45)
plt.tight_layout()
plt.show()