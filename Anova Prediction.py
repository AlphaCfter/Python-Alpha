try:
    print("Checking for modules")
    import pandas as pd
    from scipy.stats import f_oneway
    import seaborn as sns
    import matplotlib.pyplot as plt
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    import time
    print("Modules found")
    print()
except ModuleNotFoundError as e:
    print(f"Modules not found. Install the required modules by using # pip install -r requirements.txt#\n", e)
    
    exit(0)
print("=============================")
print("Group 2")
printf("ANOVA for Weather Prediction")
print("1. Find ANOVA using a CSV file")
print("2. Find ANOVA random function")
sel = int(input("Enter your choise[1,2]: "))
if sel == 1:
    try:
        weather = pd.read_csv('weather.csv')
        region1_data = weather['WindSpeed9am'].dropna()  
        region2_data = weather['WindSpeed3pm'].dropna()  

        humiddata1 = weather['Humidity9am'].dropna()  
        humiddata2 = weather['Humidity3pm'].dropna()
        time.sleep(2)

        f_statistic, p_value = f_oneway(region1_data, region2_data)
        f_statistic2, p_value2 = f_oneway(humiddata1, humiddata2)

        alpha = float(input("Enter the value of significance [0.05,0.01]: "))
        time.sleep(2)
        print()
        print("F-statistic for Windspeed:",f_statistic)
        print("p-value for Windspeed:","{:.4e}".format(p_value))
        time.sleep(2)
        print()

        sns.scatterplot(data=weather, x='WindSpeed9am', y='WindSpeed3pm')
        plt.title('Scatter Plot of WindSpeed9am vs WindSpeed3pm')
        plt.xlabel('Wind Speed 9am')
        plt.ylabel('Wind Speed 3pm')
        plt.show()

        if p_value < alpha:
            time.sleep(2)
            print("Null hypothesis is rejected. There are significant differences in wind speeds across different time periods.")
            print()
        else:
            time.sleep(2)
            print("Null hypothesis is accepted. There are no significant differences in wind speeds across different time periods.")
            print()
        time.sleep(2)
        print("F-statistic for Humidity:", f_statistic2)
        print("p-value for Humidity:","{:.4e}".format(p_value2))
        print()

        sns.scatterplot(data=weather, x='Humidity9am', y='Humidity3pm')
        plt.title('Scatter Plot of Humidity9am vs Humidity3pm')
        plt.xlabel('Humidity 9am')
        plt.ylabel('Humidity 3pm')
        plt.show()
        if p_value2 < alpha:
            time.sleep(2)
            print("Null hypothesis rejected. There are significant differences in humidity across different time periods.")
        else:
            time.sleep(2)
            print("Null hypothesis accepted. There are no significant differences in humidity across different time periods.")

        time.sleep(2)
        print("============================================")
        print("For 2 way ANOVA")

        # Define the ANOVA model
        model = ols('MinTemp ~ Evaporation + Sunshine + WindGustSpeed + Humidity9am + Pressure9am + Evaporation:Sunshine + Evaporation:WindGustSpeed + Evaporation:Humidity9am + Evaporation:Pressure9am + Sunshine:WindGustSpeed + Sunshine:Humidity9am + Sunshine:Pressure9am + WindGustSpeed:Humidity9am + WindGustSpeed:Pressure9am + Humidity9am:Pressure9am', data=weather).fit()

        # Perform ANOVA
        anova_table = sm.stats.anova_lm(model, type=2)
        residuals = model.resid
        time.sleep(2)
        print(anova_table)
        print()
        # Create a pairplot to visualize the relationship between MinTemp and the independent variables
        sns.pairplot(weather, x_vars=['Evaporation', 'Sunshine', 'WindGustSpeed', 'Humidity9am', 'Pressure9am'], y_vars=['MinTemp'], kind='scatter')
        plt.show()
    except FileNotFoundError as fnf:
        print(f"File not found. Check the file names as 'weather.csv'\n",fnf)
    except KeyError as kr:
        print("Key errors. Check the given values in the sheet \n",kr)
    except ValueError as ve:
        print("Value errors. Check the values \n",ve)
    except KeyboardInterrupt:
        print("\n Terminated program by user")

elif sel == 2:
    print("======================")
    print()
    time.sleep(2)
    import randomgen
