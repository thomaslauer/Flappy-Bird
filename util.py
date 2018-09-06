
def checkCollide(rectA, rectB):
    if (    rectA[0] < rectB[0] + rectB[2] and
            rectA[0] + rectA[2] > rectB[0] and 
            rectA[1] < rectB[1] + rectB[3] and
            rectA[1] + rectA[3] > rectB[1]):
        return True
    return False
