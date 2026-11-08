def solution(a, k):


    n = len(a) # finds out the amount of numbers in the array

    if n == 0: # if the amount of numbers in the array is 0, then just return the array
        return a

    NewArray = [0] * n #Make a new array same as the original

    for i in range(0, n):

        NewPosition = (i + k) % n

        NewArray[NewPosition] = a[i]

    return NewArray #This basically just calculates and moves the numbers to their new positions while moving them back based on their remainder and then returning the final result

a = [4, 5, 1, 2, 3] #example
k = 2
print(solution(a, k))


