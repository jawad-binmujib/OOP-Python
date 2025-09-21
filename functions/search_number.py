
def is_james_bond(l1):
    for num in range(len(l1)-2):
        if l1[num] == 0 and l1[num + 1] == 0 and l1[num+2] == 7:
            return True
        elif l1[num] == 0 and l1[num+2] == 0 and l1[num+4] == 7:
            return True
        elif l1[num+1] == 0 and l1[num+3] == 0 and l1[num+5] == 7:
            return True
    return False



is_james_bond([1, 0, 2, 0, 4, 7, 5] )