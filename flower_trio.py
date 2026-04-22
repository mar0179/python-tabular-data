#! /usr/bin/env python3
import os
import sys
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats



"""

Write a Python script to perform the linear regression 
and create the plot we did above but for each of the 
three species of Iris separately. Use best practices when
writing your script. 

"""

def species (dataframe, col_name, cat_name):
    species = dataframe[dataframe[col_name] == cat_name]
    return species

def linear_reg (dataframe, name, color, save_name):
    x = dataframe.petal_length_cm
    y = dataframe.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = name)
    plt.plot(x, slope * x + intercept, color = color, label = name+'fitted line') 
    plt.xlabel("Petal length (cm)") 
    plt.ylabel("Sepal length (cm)") 
    plt.legend()
    plt.savefig(save_name)
    plt.show()
    return






if __name__ == '__main__':
    dataframe = pd.read_csv('iris.csv')
    flow1 = species(dataframe, 'species', 'iris_versicolor')
    flow2 = species(dataframe, 'species', 'iris_setosa')
    flow3 = species(dataframe, 'species', 'iris_virginica')

    linear_reg(flow1, 'versicolor', 'green', "ver_petal_v_sepal_length_regress.png")
    linear_reg(flow2, 'setosa', 'blue', "set_petal_v_sepal_length_regress.png")
    linear_reg(flow3, 'virginica', 'purple', "vir_petal_v_sepal_length_regress.png")