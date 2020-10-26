import random



# def createRandomArray(numb, low, high):
#   Array = []
#   for n in range(numb):
#      Array.append(random.uniform(low, high))
#   return Array
# sampleData = createRandomArray(5, 20, 40)
# print(sampleData)


# def arrayInfo(anArray):
#   print("Length of Array:", len(anArray))
#   print("First Element:", anArray[0])
#   print("Last Element:", anArray[-1])

# arrayInfo([100, 200, 300, 400, 500])
# arrayInfo(["apple", "banana", "cherry"])


# def printNegatives(anArray):
#   for n in anArray:
#     if n < 0:
#       print(n)
# temps = [2, -4, -8, 0, 7, 3, -5]
# printNegatives(temps)

##########################################################
# def countHonours(anArray):
#   count = 0
#   for n in anArray:
#     if n >= 80:
#       count += 1 
#   return count

# grades1 = [70, 80, 82, 90, 65, 95, 90, 75, 80, 81]
# grades2 = [90, 90, 92, 90, 95, 95, 90, 95, 85, 80]
 
# print("Number of Honour Students in Class 1: " + str(countHonours(grades1)))
# print("Number of Honour Students in Class 2: " + str(countHonours(grades2)))

#############################################################################################
# def arraySum(anArray):
#   count = 0 
#   for sum in anArray:
#     count += sum 
#   return count
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [2, 4, 6, 8]
 
# print("Sum of first number list is: " + str(arraySum(nums1)))
# print("Sum of second number list is: " + str(arraySum(nums2)))
####################################################################################################
# array1 = [1, 2, 3, 4, "ds", 24, 2, 235]
# array1.insert(5, 80)
# print(array1)
######################################################################
# def adjustGrades(anArray):
#   for n in range(len(anArray)):
#     if anArray[n] == 48 or anArray[n] == 49:
#       anArray[n] = 50
#     elif anArray[n] == 78 or anArray[n] == 79:
#       anArray[n] = 80
#   print(anArray)

# grades1 = [70, 78, 49, 50, 81, 48, 79]
# adjustGrades(grades1) # grades1 should now be: [70, 80, 50, 50, 81, 50, 80]
##################################################################################




# def replaceAll(anArray, maybe, no):
#   for n in range(len(anArray)):
#     if anArray[n] == maybe:
#       anArray[n] = no
#   print(anArray)
# myArray = ["yes", "maybe", "no", "maybe", "yes", "no"]
# replaceAll(myArray, "maybe", "no")

##############################################################
# def swap(anArray, index1, index2):
#   anArray[index1], anArray[index2] = anArray[index2], anArray[index1]
#   print(anArray)

# letters = ["a", "b", "c", "d", "e"]

# swap(letters, 1, 4)




# n = []
# for i in range(400):
#    n.append("algorithm")
# print(n)

# n = []
# for i in range(20, 804, 4):
#      n.append(i)
# print(n)




def createRandomArray(numb, low, high):
    Array = []
    for n in range(numb):
        Array.append(random.randrange(low, high))
    return Array
 
 
sampleData = createRandomArray(5, 20, 40)
print(sampleData)




















































