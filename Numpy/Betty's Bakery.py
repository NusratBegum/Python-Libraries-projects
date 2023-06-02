

"""
1.Start by importing NumPy 

2.All of Betty’s recipes call for milk, eggs, sugar, flour, and butter. For example, her cupcake recipe calls for:

Flour	Sugar	Eggs	Milk	Butter
2 cups	0.75 cups	2 eggs	1 cups	0.5 cups
Create a NumPy array that represents this data. Each element should be a number (i.e., 2 for “2 cups”). Save this array as cupcakes.

3.Betty’s assistant has compiled all of her recipes into a csv file called recipes.csv Load this file into a variable called recipes.

4.Display recipes  where each row represents a different recipe and each column represents a different ingredient.

5.The 3rd column represents the number of eggs that each recipe needs. we saved the 3rd column as eggs. now we will use logical statement to find out the recipes where exactly required 1 egg.

6.Betty is going to make 2 batches of cupcakes (1st row) and 1 batch of cookies (3rd row).we have a variable for cupcakes. Now, we will create a variable for cookies with the data from the 3rd row.

7.Get the number of ingredients for a double batch of cupcakes by using aggregate function on cupcakes. Save your new variable to double_batch.

"""














#num-1
import numpy as np

#Num-2
cupcakes = np.array([2,0.75,2,1,0.5])
print(cupcakes)
print("\n")

#num-3
recipes = np.genfromtxt('recipes.csv', delimiter = ',')
#num-4
print(recipes)
print("\n")

#Num-5
eggs =recipes[:,2]
print(eggs)

print("\n")

#num-6
one_egg =recipes[(eggs==1)]
print(one_egg)
print("\n")
#num-7
cookies = recipes[2,:]
print(cookies)
print("\n")
#num-8
double_batch = cupcakes * 2
print(double_batch)
print("\n")
#num-9
grocery_list = cookies + double_batch
print(grocery_list)



