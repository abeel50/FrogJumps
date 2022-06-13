import math
def solution(X, Y, D):
    # write your code in Python 3.6
    jumps = math.ceil((Y-X) / D)
    return jumps