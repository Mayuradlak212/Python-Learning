import numpy as np

import random
l1=[23,4,1,67,89,90,12]

l2=[34,66,11,43,90,77,12]

arr1=np.array([l1])

arr2=np.array([l2])
print("Element of array : ",arr1[0])

print("Element of array 2 : ",arr2[0])

print("Sum of all Element : ",arr2.sum(axis=0))

print("Mean of arr2 ",arr2.mean())

print("Minimum Element in array: ",arr1.min())

print(arr1.shape)

print("Type of array 2 : ",type(arr2))

print("Sorted element of arr2  : ",np.sort(arr1)[0])

print("Sorted Element of arr1 : ",np.sort(arr2)[0])

print(" Median  Function :  ",np.median(arr1))

row=5

col=6

Full=np.full((row,col),10)
print(" Full  Function : \n",Full)

print("Check shape of Full Fucntion : \n",Full.shape)

print("Zeros Function : \n",np.zeros((5,5)))

# print("Let's Disscuss About Arange Function \n")

print(np.arange(10,100,5))

# print( "Random in Numpy : ")
# # I want to print any 10 number using Loop let's see
for i in range (10):
    print(np.random.randint(10,100),end=' ')
print()
# Full.shape=(3,10)

# print("After Change Shape : ")
# print("\n",Full)
# # Merge Two array

merge=np.vstack((arr1,arr2))
print ("After Megre two array : \n",merge)
# After Merge two array is conveert in ND array :
print("Type After Megre Vertically: ",type(merge))

# print("Megre To array Horizontally : ")

Hor=np.hstack((arr1,arr2))

print(Hor)

print("Sort to Meged Array: ")

# s=np.sort(Hor)
# print("Sorted array : \n",s)

# # Setdifference and Intersection :
# Differ=np.setdiff1d(arr2,arr1)

# print("Set Difference in two array : \n",Differ)

# # InterSection into to array L

# inter=np.intersect1d(arr1,arr2)

# print("Intersection : ",inter)

# # if you add 2 in arr so all element increse to 2
# arr1=arr1+10

# print("After Addind 10 in whole array : \n",arr1)

# arr2=arr2-5

# print("Minus into whole element :\n ",arr2)

# div=np.std(arr1)

# print("Standard Derivation : ",div)

# print("Median of Merged Array : ",np.median(Hor))

# print("This all Complete Tutorial of Numpy :")

# print("Mean of hor : ",np.mean(Hor))