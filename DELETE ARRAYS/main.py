# array1 = [1,2,3,4,5,6,7]
# array1.pop()
# print(array1)

# array1 = [1,2,3,4,5,6,7]
# array1.pop(0)
# print(array1)


def removeLongNames(names):
    for i in range(len(names)-1,-1,-1):
        if len(names[i]) > 4:
            del(names[i])

team1 = ["Adam", "Benjamin", "Caleb", "Dave", "Evelyn"]
removeLongNames(team1)
print(team1)



####################################################################

# def removeAll(anArray, item):
#     for i in range(anArray.count(item)):
#         anArray.remove(item)


# nums = [10, 70, 70, 100, 70, 45, 70, 70, 70]
# removeAll(nums, 70)
# print(nums)


























































































































