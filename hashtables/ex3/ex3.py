def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    #I possibly could have been more efficient, not sure how
    #Needed a hash table of all numbers, amount of arrays passed,
    #and I made a second hash table for only the same nubmers
    #because I wasn't sure how else to move the data around
    only_same = {}
    everything = {}
    length = len(arrays)

    result = []


    #go over the list of arrays, then in each array add each item to
    #a hash table, if it's already in the hash table increment the 
    #second variable
    for array in arrays:
        for i in array:
            if i not in everything:
                everything[i] = 1
            else:
                everything[i] += 1
        
    #check the elements in everything, if the variable matches the 
    #length that key is in every array
    for i in everything:
        if everything[i] == length:
            only_same[i] = everything[i]

    #pull the key off the element in only same and put it in the list 'result'
    for key, value in only_same.items():
        result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
