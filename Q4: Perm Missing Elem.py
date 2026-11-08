def solution(A):
    n = len(A) #counts amount of elements in the array

    total = (n+1) * (n+2) // 2 #calculates the expected sum of numbers from 1 to n+1...

    for element in A: #subtracts every number in the array from the total
        total = total - element

    return total #returns the missing number

#Example
A = [1, 3, 4, 5]
print(solution(A))