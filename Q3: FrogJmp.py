def solution(X, Y, D):
    distance = Y - X #gets distance from where the frog is and where the point he wants to go is

    jumps = distance // D #How many jumps is determined based on the distance and how far the frog jumps

    if distance % D != 0: #If the distance is not divisible by the distance the frog jumps, just add 1.
        jumps = jumps + 1

    return jumps #returns the amount of jumps

#Example
X = 10
Y = 85
D = 30
print(solution(X, Y, D))