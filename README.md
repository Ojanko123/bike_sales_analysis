
Exploratory data analysis of a bike sales dataset using Python. The project combines data visualization with formal statistical hypothesis testing to uncover patterns in customer behavior, sales distribution, and profitability — and to evaluate whether the data meets the assumptions required for linear regression.



## Dataset

- **File:** `bikesales.csv`
- **Key columns:** Customer Age, Order Quantity, Profit, Country, Year



## Tools & Libraries

| Library | Purpose |
|---|---|
| Pandas | Data loading and manipulation |
| NumPy | Numerical operations |
| Matplotlib | Core visualizations |
| Seaborn | Statistical plots and styling |
| SciPy (stats) | Hypothesis testing |



## Analysis

### Visualizations

- **KDE Density Plot** — distribution of customer age across the dataset
- **Boxplots** — spread and outliers for customer age and order quantity
- **Histogram** — frequency distribution of order quantity (30 bins)
- **Pie Chart** — sales volume breakdown by year
- **Scatter Plot** — relationship between order quantity and profit, segmented by country
- **Bar Chart** — total sales quantity per country

### Statistical Hypothesis Testing

Before attempting any correlation or regression analysis, normality was formally tested on the key variables.

**Kolmogorov-Smirnov Test** (Order Quantity):
- Tests whether the variable follows a normal distribution
- Used `scipy.stats.kstest` against a normal distribution fitted to the data

**Anderson-Darling Test** (Order Quantity):
- A more sensitive normality test, especially in the tails of the distribution
- Used `scipy.stats.anderson`

**KS Test** (Country — encoded numerically):
- Country variable was encoded numerically to allow statistical testing
- Tested for normality using the same KS approach

**Conclusion:**

At a 95% confidence level, both Order Quantity and Country show strong evidence of **non-normal distribution**. This means the assumptions required for simple linear regression are not met — therefore a standard linear regression model cannot be reliably applied to examine the relationship between these variables.





## Key Insights

- Customer age distribution is approximately bell-shaped but with notable spread
- Order quantity shows significant variability and outliers across countries
- Profit does not scale linearly with order quantity — relationship varies by country
- Neither order quantity nor country follows a normal distribution, ruling out simple linear regression for correlation analysis


## How to Run

1. Clone the repository
2. Place `bikesales.csv` in the same directory as the script
3. Install dependencies:
```bash
pip install pandas numpy matplotlib seaborn scipy
```
4. Run the script:
```bash
python bike_sales_analysis.py
```



**Oresti Janko**
Statistics graduate with focus on data analysis, statistical modelling, and Python-based visualization.
