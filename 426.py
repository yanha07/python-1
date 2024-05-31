'''Created by Yanha Loharwad
Python program to print dictionary in table format.'''
dict={'A1':[1,2,3],'A2':[5,6,7],'A3':[9,10,11]}
for i in range(3):
    for j in range(3):
        print(dict[f'A{i+1}'][j], end=' ')
print()
