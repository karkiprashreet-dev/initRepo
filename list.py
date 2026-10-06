#List of 5 numbers and printing it:
print("===List of 5 numbers===")
myNum = [1, 2, 3, 5, 4]
for n in myNum:
    print(n)
print()

#Finding the length of list:myNum
print("===Length of list myNum===")
print("The length of the list myNum is ", len(myNum))
print()

#Finding the first and last element of the list
print("===Finding the first and last element of the list===")
print("first element and last element", myNum[0], myNum[-1])
print()

#Adding a new element to the end of the list
print("===Adding a new element of the end of list===")
myNum.append(9)
for n in myNum:
    print(n)
print()

#Removing an element from the list
print("===Removing an element from list===")
delItem = myNum[2]
myNum.pop(2)
for n in myNum:
    print(n)
print(f'The deleted item was {delItem}')
print()

#Adding all the items in the list
print("===Adding all the items in the list===")
sum = 0
for n in range(len(myNum)):
    sum = sum + myNum[n]
print(f'The sum of all the items in list: {sum}')
print()


#finding the maximum and minimum number from the list
print("===Maximum and Minimum number from the list===")
maxValue = max(myNum)
minValue = min(myNum)
print("The current list is:")
for i in myNum:
    print(i)
print(f"The maximum and minimum number of the list is {maxValue} and {minValue}")

#Reversing the list without using reverse
print("===Reverse list with out using reverse function")
print("Original list:")
for i in myNum:
    print(i)
print()
if len(myNum) <= 1:
    print(myNum)
    
else:
    for i in range(len(myNum)):
        print(myNum[-(i+1)])

#Finding the second largest number in the list
print("===Second largest number in the list===")
largestNum = max(myNum)
myNum.remove(largestNum)
secondLargestNum = max(myNum)
myNum.append(9)
for i in myNum:
    print(i)
print()
print(f"The second largest number is {secondLargestNum}")

#Count the number of times an item has been repeated 
print("===Counted the number of times an item has been repeated===")
