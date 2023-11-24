#importing libraries

import pandas as pd
import matplotlib.pyplot as plt

# 1)temperature_data

temp_data = pd.read_csv('path_file')
def temperature_change(data):
    plt.figure(figsize=(26, 6))
    areas = data['Area'].unique()  
    for area in areas:
        area_data = data[data['Area'] == area]
        plt.plot(area_data['Month'], area_data['TemperatureChange'], label=area)
    plt.title('Temperature Changes Over Months by Area in 2019')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.show()
temperature_change(temp_data)


# 2) salary experience data

sal_exp_data=pd.read_csv('path_file')
def sal_exp(data, x, y):
    plt.figure(figsize=(9, 6))
    
    plt.scatter(data[x], data[y], alpha=0.9)
    
    plt.title(f'Scatter Plot - {x} vs. {y}')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(True)
    plt.show()

# Call the function with your actual dataset
sal_exp(sal_exp_data, 'YearsExperience', 'Salary')


# 3) heart disease usi data

heart_uci_data=pd.read_csv('path_file')
def heart_uci(data):

    plt.figure(figsize=(8, 6))
    
    plt.hist(data['age'], bins=20, edgecolor='black')
    
    plt.title('Age Distribution in Heart Disease UCI Dataset')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

heart_uci(heart_uci_data)
