#to check if n and its double exists

def checkIfExists(list):
    list.sort(reverse = True)
    print(list)
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            print(list[i], list[j])
            if list[i] < 0 and list[j] < 0:
                if list[j] == list[i] * 2:
                    return True
            else:
                if list[i] == list[j] * 2:
                    return True
    return False


l = [-10,12,-20,-8,15]
print(checkIfExists(l))