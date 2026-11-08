def solution(A):
    n = len(A) #counts every element in the array

    left = 0 #makes left with the first element and the right the rest
    right = sum(A)

    minimum = float('inf') #doing this cause we want a value that is larger than any possible difference, and infinity is always going to be the largest so the calculated difference will always be smaller and replace it

    for P in range(1, n): #Test every possible split
        left = left + A[P - 1] #Move numbers between the two sides
        right = right - A[P - 1]
        difference = abs(left - right) #calculates the difference and finds the absolute value between the two sums
        if difference < minimum: #check if it's the smallest, if the new difference is smaller it replaces the previous minimum
            minimum = difference

    return minimum #returns the answer

#Example
A = [3, 1, 2, 4, 3]
print(solution(A))

