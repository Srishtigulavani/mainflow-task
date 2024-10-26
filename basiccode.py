#add the item in list at the last using append()
l=[6,2,0,8]
print(l)
l.append(7)
print(l)

#sort the list in ascending order
l.sort()
print(l)

#descending order
l.sort(reverse=True)
print(l)

#reverse
l.reverse()
print(l)

#returns the index of the first occurence
print(l.index(6))
print(l)

#it count the number of times tht value is present
print(l.count(7))
print(l)

#return the copy of the list
newlist=l.copy()
print(l)
print(newlist)

#insert the item at the given index
l.insert(2,8)
print(l)

#extend() adds an entire list
m=[455,500,800]
l.extend(m)
print(l)

#concatenating two lists 
k=l+m
print(k)

#tuple creation
tup1=(1,2,3,4,5)
print(type(tup1),tup1)

#tuple without commas are class int 
tup2=(1)
print(type(tup2),tup2)

#tuple need comas and round brackets
tup3=(1,)
print(type(tup3),tup3)

#accessing the tuple
print(tup1[1])
print(tup1[2])
print(tup1[3])

#checking if the item is in the tuple or not
if 3  in tup1:
    print("yes it is there")
else:
    print("no it is not")
#slicing in tuples
print(tup1[2:3])
print(tup1[2:-2])
print(tup1[-3:4])

# converting tuple to list for add,remove or any other operation
countries=("spain","india","england","germany")
temp=list(countries)

temp.append("russuia")

temp.pop(3)

temp[2]="finland"

countries=tuple(temp)

print (countries)

#count()
tuple3=(0,1,2,3,4,5,3,3,3)
res=tuple3.count(3)
print('count of 3 in tuple is:',res)

#index()
print(tuple3.index(3,2,7))


#dictionary
d={'maths':50,'science':90,'english':80}

print(d)

print(d['maths'])

e=d['science']=40
print(e)





