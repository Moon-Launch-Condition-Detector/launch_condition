

def maxArea(height) -> int:
    firstMax = 0 
    secondMax = 0 
    biggest = height[0] 

    if len(height) == 1: 
        return height[0]

    for i in range(len(height)): 

        secondMax += 1 
        if secondMax > len(height) - 1: 
            break 

        if height[secondMax] > height[firstMax]: 
            firstMax += 1 

        if height[secondMax] > biggest and height[secondMax] != height[firstMax]: 
            biggest = height[secondMax]

    if height[firstMax] > biggest and biggest != 1: 
        difference = height[firstMax] - biggest
        newHeight = height[firstMax] - difference 
        return newHeight * biggest

    elif height[firstMax] < biggest and biggest != 1: 
        difference = biggest - height[firstMax] 
        newHeight = biggest - difference 
        return newHeight * height[firstMax]     

    return height[firstMax] * biggest

height = [1,2,13,14,4,7,9,4,10]
print(maxArea(height))
