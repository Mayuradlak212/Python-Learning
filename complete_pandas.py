import pandas as pd
# Single Dimentional-Series Object
# Multi Dimentional- Data frame
# l=[10,20,30,40,50]
# s=pd.Series(l)
# Output Like
'''
0    10
1    20
2    30
3    40
4    50
dtype: int64
'''
# Printing Series and Index wise Element

# print(s);
# Printing Data Type :
# print(type(s));
# Output Like
#<class 'pandas.core.series.Series'>
# You can change index:
# dex=['a','b','c','d','e'];
# index=pd.Series(l,dex);
'''
Output
 a    10
b    20
c    30
d    40
e    50
dtype: int64

'''
# print(index);
# Using Dictionary
# You can Change index of Element
# p=pd.Series({'a':10,'b':20,'c':30,'d':40},index=['b','c','a','d']);
# print(p);
# Output
'''a    10
b    20
c    30
d    40
dtype: int64
'''
# # l=[10,20,30,40,50];
# # m=[11,12,13,14,15];
# # s=pd.Series(l)
# s2=pd.Series(m);
# : mean Vaha tak ke element print krna hai
# Exampl :3
# 0,1,2
#print("You can Extract Individual Element \n",s[0:3]);
#print(s[-len(l):])
#Using This Method Itrate all /Element
# s=s+10;
# print(s);
#-----------------------------------------------------------------------------
# Multi Dimentional Data frame
# data=pd.DataFrame({"Name": ['Mayur','Vijay','Vishal','Mahendra','Raj','Varun'],"DOB": ['2002','2003','2002','2002','2002','2002'],"Marks":[92,88,89,91,87,88]})
# print(data);
# OutPut
'''    Name   DOB  Marks
0     Mayur  2002     92
1     Vijay  2003     88
2    Vishal  2002     89
3  Mahendra  2002     91
4       Raj  2002     87
5     Varun  2002     88
'''
# here i'm Openning CSV File
# One Things is very Important is
#You need to add current Directory
# print("This is Head of CSV ");
# print("Head top 5 data");
Iris=pd.read_csv('Iris.csv');
first=Iris.head();
# print(first);
print("From Bottum 5 data set :");
print("Using tail function: ");
data=pd.read_csv('Iris.csv');
#t=Iris.describe();
# Using iloc method you can
# Print as pattern
#-----------------------------------------------------------------------------
 # iloc method Method :
# 0:4 it means 0th row to 4th row
# 0:3 it mean column row to 3rd column
# t=Iris.iloc[0:4,0:3];
# print(t);
# Output For Example
'''     Name   DOB  Marks
0  Mayur   2002     92
1  Vijay   2002     91
2  Vishal  2002     90
3    Raj   2002     88'''
# t=Iris.loc[0:3,("Name","Marks")];
'''Output
Name  Marks
0  Mayur      92
1  Vijay      91
2  Vishal     90
3    Raj      88

'''
# Drop Method is Used for Drop data row
# t=Iris.drop('DOB',axis=0);
i=Iris.min();
print("Minimum Data set in CSV file :");
print(i);
a=Iris.max();
print("Maximum Data set in CSV file ");
print(a);
# Here i'm Using sort_Value Function for sort given data
S=first.sort_values(by='Marks');
print(S);
print(first);
# i'm Using count_value method for count how many time reapet this value :
# Ok Alright
count=Iris['Marks'].value_counts();
print(count);