from re import T
import pandas as pd

grades = pd.Series([87,100,94])

print(grades)

a = pd.Series(96.6, range(3))

b = grades[0]

c = grades.count()

d = grades.mean()

#describe method will give all the states (from mean to SD)
print(grades.describe())

#giving indexes instead 
grades = pd.Series([87,100,94], index=['Wally', 'Eva', 'Rally'])

#print(grades)

grades_dict = {'Wally': 87, 'Eva': 100, 'Rally': 94}

#converting grades into series 
#key becomes indexas and values become the column 
grades.ds = pd.Series(grades_dict)


print(grades.ds)

eva = grades['Eva']

#without doing the bracket you can also use dot
#dot notation only works with string indexes 
wally = grades.Wally



e = grades.values

hardware = pd.Series(["Hammer", "Saw", "Wrench"])

f = hardware.str.contains('a')

g = hardware.str.upper()

#convert a series object into a python list 
hardware_list = hardware.to_list()

ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,10])

g= ds1 == ds2

h = ds1 > ds2

i = ds1 < ds2



list_of_series = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])


list_of_series = list_of_series.apply(pd.Series).stack().reset_index(drop=True)


#sort a series 

s = pd.Series(['100', '200', 'Python', '300.12', '400'])

sorted_series = s.sort_values()

# s = pd.Series(['100', '200', 'Python', '300.12', '400'])

# sorted_series = s.sort_values()

#adding to a series 
s = s.append(pd.Series(['500', 'php'])).reset_index(drop=True)


#write a Pandas program to calculate the frequency counts of each unique
#value of given series 

import random
list1 = [random.randrange(1,10) for i in range(0,100)]

s = pd.Series(list1)

result = s.value_counts()

print()
