#1Basic Assignment

a = 10  #created a variable a and assigned a value to it
b = 20  #created a variable a and assigned b value to it
c = a+b-5  #expression for adding and subtracting
print(c) #print statement
print() #Here I am printing a new line becasue we can see our output clearly

#2 Augumented assignment

x = 10  # Here I created a variable x and assigned  
x += 1  #expression: it will increment the value of x by 1 
print(x) #print the value of x
print() #Here I am printing a new line becasue we can see our output clearly

#3 Tuple Assignment

a,b = 2,3  #Here I created 2 variables a,b and assigned values to it
a,b = b,a  #Here I used a simple scenario to swap two numbers
print('a = ', a) #printing the value of a after swapping
print('b = ',b) #Here I am printing a new line becasue we can see our output clearly
print()

#4 List Assignment

mylist = [1,2,3,4] #Assigning values to a list 
mylist.append(0)   #appending a value to the list
mylist += [5,6]  #expression for adding elements to a list
print(mylist) #print statement
print()#Here I am printing a new line becasue we can see our output clearly

#5 Etended sequence Assignment

seq = [1,2,3,4] #assigning values to a variable seq
a,b,c,d = seq 
print(a,b,c,d)  #print statement
a, *b = seq     #expression
print(a)
print(b)
*a, b = seq
print(a)


