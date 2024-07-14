import random
import numpy as np
import pandas as pd
from scipy.stats import f_oneway
import time
    
time.sleep(2)
    # Generate random weather data for each month over the last 3 years
random.seed(10)  # For reproducibility

years = ['2019', '2020', '2021']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
weather_data = {month: [random.randint(0, 100) for _ in range(3)] for month in months}

    # Construct DataFrame from the generated data
df = pd.DataFrame(weather_data, index=years)

    # Displaying the generated data
print("Generated Weather Data:")
print(df)

    # Calculating the overall mean
overall_mean = df.values.mean()
print("\nOverall Mean:", overall_mean)
    # Calculating the overall variance
overall_variance = df.values.var()
print("Overall Variance:", overall_variance)

    # Calculating the mean for each month
month_means = df.mean()
print("\nMean for each month:")
print(month_means)

    # Calculating the variance for each month
month_variances = df.var()
print("\nVariance for each month:")
print(month_variances)

    # Calculating the sum of squares for each month
month_sum_squares = df.sum(axis=0) ** 2
print("\nSum of Squares for each month:")
print(month_sum_squares)

    # Perform one-way ANOVA
f_statistic, p_value = f_oneway(*[df[month] for month in months])

    # Display the ANOVA results
print("\nOne-way ANOVA Results:")
print("F-statistic:", f_statistic)
print("p-value:", p_value)

    # Prepare the results in a tabular form
results = pd.DataFrame({
    'Month': months,
    'Mean': df.mean(),
    'Variance': df.var(),
    'Sum of Squares': df.sum(axis=0)**2,
})

time.sleep(2)
    # Generate random weather data for each month and location over the last 3 years
random.seed(10)  # For reproducibility

years = ['2019', '2020', '2021']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
locations = ['Location A', 'Location B', 'Location C']  # Additional factor for two-way ANOVA

    # Generating data for each combination of month and location
weather_data = {(year, month, location): random.randint(0, 100) for year in years for month in months for location in locations}

    # Construct DataFrame from the generated data with MultiIndex
df = pd.DataFrame(weather_data.values(), index=pd.MultiIndex.from_tuples(weather_data.keys(), names=['Year', 'Month', 'Location']), columns=['Value'])

    # Displaying the generated data
print("Generated Weather Data:")
print(df)

    # Calculating the overall mean
overall_mean = df['Value'].mean()
print("\nOverall Mean:", overall_mean)

    # Calculating the overall variance
overall_variance = df['Value'].var()
print("Overall Variance:", overall_variance)

    # Calculating the mean for each month
month_means = df.groupby('Month')['Value'].mean()
print("\nMean for each month:")
print(month_means)

    # Calculating the variance for each month
month_variances = df.groupby('Month')['Value'].var()
print("\nVariance for each month:")
print(month_variances)

    # Calculating the sum of squares for each month
month_sum_squares = df.groupby('Month')['Value'].sum() ** 2
print("\nSum of Squares for each month:")
print(month_sum_squares)

    # Perform two-way ANOVA
    # For simplicity, we'll perform one-way ANOVA for each factor (month and location)
# This is not a complete two-way ANOVA, but rather an illustration of the steps involved
f_statistic_month, p_value_month = f_oneway(*[df.loc[(slice(None), month), 'Value'] for month in months])
f_statistic_location, p_value_location = f_oneway(*[df.loc[(slice(None), slice(None), location), 'Value'] for location in locations])

    # Display the ANOVA results for each factor
print("\nTwo-way ANOVA Results (Month):")
print("F-statistic:", f_statistic_month)
print("p-value:", p_value_month)

print("\nTwo-way ANOVA Results (Location):")
print("F-statistic:", f_statistic_location)
print("p-value:", p_value_location)

    # Prepare the results in a tabular form
results = pd.DataFrame({
    'Month': months,
    'Mean': df.groupby('Month')['Value'].mean(),
    'Variance': df.groupby('Month')['Value'].var(),
    'Sum of Squares': df.groupby('Month')['Value'].sum() ** 2,
})

    # Add overall statistics
overall_stats = pd.DataFrame({
     'Overall Mean': df['Value'].mean(),
    'Overall Variance': df['Value'].var()
}, index=['Overall'])

    # Display the results in tabular form
print("\nResults in Tabular Form:")
print(results)
print("\nOverall Statistics:")
print(overall_stats)

