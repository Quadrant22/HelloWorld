# as is an alias
import matplotlib.pyplot as plt
import numpy as np


print("Hello, World!", "\U0001F60A")

print("Vegan Vs. Keto")
print("A vegan diet excludes all animal products")
print("Eating a meat-free diet can cut our water footprint in half.")
print("The keto (ketogenic) diet is a high-fat, moderate-protein, very-low-carbohydrate")
print("The keto diet has become a popular weight loss diet.")
print("  ")
#np alias for numpy
#using array [], arrays are changable can hold int, str, booleans at once.
yAxisOfPie = np.array([59,41])
veganLabels = ["Female", "Male"]
#pie char colors
veganColors = ["g", "y"]
plt.pie(yAxisOfPie, labels = veganLabels)
# plt.pie(yAxisOfPie)
plt.show()

print("Veganuary, one of the most popular plant-based campaigns")
print("Dr. Oz Keto campaign.")
#dictionary dietDict holds keys and values.
dietDict = {
    "Veganuary_2022": 629000, "Dr.Oz_Keto2022" : 700000,
}
#list the key values
listKeys = list(dietDict.keys())
#list the values
listValues = list(dietDict.values())
#within the bar() graph place length of dictionary, values of dictionary
#use values as label tick_label = ...
#plt stands for matplotlib
plt.bar(range(len(dietDict)), listValues,tick_label=listKeys)
plt.show()

