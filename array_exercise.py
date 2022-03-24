## Numpy Exercise
import numpy as np 

## Step 1: Create a 4x3 array of all 2s
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")
array1 = np.full((4,3), 2)

print(array1)

print()

## Step 2: Create a 3x4 array with a range from 0 to 110 where each number increases by 10
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")

array2 = np.arange(0, 111, 10).reshape(3,4)

print(array2)

print()

## Step 3: Change the layout of the above array to be 4x3, store it in a new array
print("-----------------------------------------------   STEP THREE   -----------------------------------------------")

array3 = np.arange(0, 111, 10).reshape(4,3)
#broadcasting method
print(array3)

print()

## Step 4: Multiply every elemnt of the above array by 3 and store the new values in a different array
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")

array4 = np.arange(0, 111, 10).reshape(4,3) * 3

#new_array = array3*3

print(array4)

print()

## Step 5: Multiply your array from step one by your array from step 2
print("-----------------------------------------------   STEP FIVE   -----------------------------------------------")
# new_array = np.full((4,3), 2) * np.arange(0, 111, 10).reshape(3,4)

# print(new_array)
#print(array1*array2)
## This errored out... why? because number of rows and column matrics is different in both steps 
print()

## Step 6: Comment out your code from Step 5 and then multiply your array from step 1 by your array from step 3
print("-----------------------------------------------   STEP SIX   -----------------------------------------------")

array6 = np.full((4,3), 2) * np.arange(0, 111, 10).reshape(4,3)

print(array6)
## this worked! why?

#print(array1*array3)
print()



