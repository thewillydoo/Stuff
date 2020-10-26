#lists 

x = [1,1,2,3,4,5,6,7,43234,234]
print (x[0])
#will be 1 
print (x[8])
#will print 43234 which is the 8th element in this list 
print (x[2], x[7])
#will print the 3rd and 8th number 


y = [2,12,3,12,3,512]
#will change the 1st number to 10
y[0] = 10
print (y[0])

#will change the last to 1000 and the 3rd last to 2000
y[-1] = 1000
y[-3] = 2000
print(y)

w = (3,4)

print (w)
print (w[0])
x[0] = 2 #will not change, add, or remove elements since it has rounded brackets because it is a tuple



#Loops through a list 


my_list = [101, 20, 10, 50, 60]
for item in my_list:
    print(item)

#will print
# 101
# 20
# 10
# 50
# 60


my_list = ["Spoon", "Fork", "Knife"]
for item in my_list:
    print(item)

#output
# Spoon
# Knife
# Fork


my_list = [ [2,3], [4,3], [6,7] ]
for item in my_list:
    print(item)

# output
# [2,3]
# [4,3]
# [6,7]


#adding to the list 

my_list = [2, 4, 5, 6]
print(my_list)
my_list.append(9)
print(my_list)
# Output:
# [2, 4, 5, 6]
# [2, 4, 5, 6, 9]



#Creating a list of numbers from user input

my_list = [] # Empty list
for i in range(5):
    user_input = input( "Enter an integer: ")
    user_input = int(user_input)
    my_list.append(user_input)
    print(my_list)

# Output
# Enter an integer: 4
# [4]
# Enter an integer: 5
# [4, 5]
# Enter an integer: 3
# [4, 5, 3]
# Enter an integer: 1
# [4, 5, 3, 1]
# Enter an integer: 8
# [4, 5, 3, 1, 8]






















































