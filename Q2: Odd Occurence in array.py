def solution(A):
    n = len(A) #counts how many elements there are in the array
    if n == 0:
        return A

    unpaired = 0 #makes a variable called unpaired and sets it at 0

    for index in range (0, n): #starts a loop at 0 to n
        unpaired = unpaired ^ A[index] #takes the current value of unpaired and performs XOR, which cancels out matching numbers

    return unpaired #returns the unpaired number

#Example
A = [5, 5, 3, 3, 2]
print(solution(A))