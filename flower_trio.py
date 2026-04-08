#! /usr/bin/env python3
import sys
import re
import pandas as pd
import matplotlib.pyplot as plt
import scipy

if __name__ == '__main__':
    print ('hello!')

def species (csv, category, cat_name):
    dataframe = pd.read_csv(csv)
    species = dataframe[csv.category == cat_name]
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

linear_reg(species(iris.csv, 'iris_versicolor', 'species'), 'versicolor', green, "ver_petal_v_sepal_length_regress.png")
linear_reg(species(iris.csv, 'iris_setosa', 'species'), 'setosa', blue, "set_petal_v_sepal_length_regress.png")
linear_reg(species(iris.csv, 'iris_virginica', 'species'), 'virginica', purple, "vir_petal_v_sepal_length_regress.png")



"""
import pandas as pd
import matplotlib.pyplot as plt  (look up matplotlib.plot scatter)
from scipy import stats

dataframe = pd.read_csv("iris.csv") READ IN CSV and NAME DATA FRAME
versicolor = dataframe[dataframe.species == "Iris_versicolor"]  SPLIT DATA FRAME BY FLOWER SPECIES
setosa = dataframe[dataframe.species == "Iris_setosa"]  SPLIT DATA FRAME BY FLOWER SPECIES
virginica = dataframe[dataframe.species == "Iris_virginica"]  SPLIT DATA FRAME BY FLOWER SPECIES

x = dataframe.petal_length_cm ASSIGN X AXIS VALUES
y = dataframe.sepal_length_cm ASSIGN Y AXIS VALUES
regression = stats.linregress(x, y) GET LINEAR REGRESSION
slope = regression.slope GET SLOPE OF REGRESSION
intercept = regression.intercept GET INTERCEPT OF REGRESSION

plt.scatter(x, y, label = 'Data') PLOT X AND Y SCATTER PLOT POINTS
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line') APPLY FITTED LINE
plt.xlabel("Petal length (cm)") LABEL X AXIS
plt.ylabel("Sepal length (cm)") LABEL Y AXIS
plt.legend() ADD LEGEND
plt.savefig("petal_v_sepal_length_regress.png") SAVE GRAPH
quit()

Write a Python script to perform the linear regression 
and create the plot we did above but for each of the 
three species of Iris separately. Use best practices when
writing your script. 
"""


"""
Code Anatomy

Organs:

def species (csv, category, cat_name):
    dataframe = pd.read_csv(csv)
    species = dataframe[csv.category == cat_name]
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

"""