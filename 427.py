'''Created by Yanha Loharwad'''
print("Numbers divisible by 7 and multiple of 5:")
list1=[]
for i in range(1500,2701):
 if i%7==0 and i%5==0:
   list1.append(i)
print(list1)
