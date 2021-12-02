#removing the duplicated from a sorted array

#prompt the user to enter the list of the numbers
lst = []
n = int(input("Enter the number of elements to be entered : "))
for i in range(n):
    temp = int(input())
    lst.append(temp)

#now removing the duplicates form the list
i = 0
count = 0
for j in range(1,len(lst)):
    if lst[i] != lst[j]:
        i += 1
        lst[i] = lst[j]
        count += 1
print(count)