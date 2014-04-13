"""
N: number of blocks
naomiList: Naomi's list of weights of blocks
kenList: Ken's list of weights of blocks
Return number of points Naomi will score if she plays War optimally.
"""
def war(N, naomiList, kenList):
    naomiList = sorted(naomiList)
    kenList = sorted(kenList)
    kenCopy = kenList
    win = 0
    for i in range(N):
        existBigger = False
        # Naomi always start from smallest to biggest
        # Ken will choose the smallest number that is bigger than than Naomi's chosen number
        for j in range(len(kenCopy)):
            if kenCopy[j] > naomiList[i]:
                kenCopy.pop(j)
                existBigger = True
                break
        # do this until inevitably all Naomis's future numbers will always bigger than Ken's
        if existBigger == False:
            kenCopy.pop(0)
            win += 1
    return win
    
def deceitfulWar(N, naomiList, kenList):
    # sort the list
    naomiList = sorted(naomiList)
    naomiCopy = naomiList
    kenList = sorted(kenList)
    kenCopy = kenList
    win = 0
    # while there is still element in the list
    while len(naomiCopy) > 0:
        # if the largest element of Naomi is smaller than Ken's largest element
        if naomiCopy[-1] < kenCopy[-1]:
            # use Naomi's smallest element to kill Ken's largest element
            naomiCopy.pop(0)
            kenCopy.pop(-1)
        # else if the largest element of Naomi is larger than Ken's largest element
        elif naomiCopy[-1] > kenCopy[-1]:
            # use the largest element to kill Ken's largest element
            naomiCopy.pop(-1)
            kenCopy.pop(-1)
            # add point
            win += 1
    return win

# get number of test cases, T
T = int(raw_input())

# initialize lists
N = [0 for i in range(T)]
Naomi = [0.00000000 for i in range(T)]
Ken = [0.00000000 for i in range(T)]

# for each test cases
for i in range(T):
    # get N, number of blocks each player
    N[i] = int(raw_input())
    string1 = raw_input()
    string2 = raw_input()
    # get weights of each of Naomi's and Ken's blocks
    Naomi[i] = string1.split(" ")
    Ken[i] = string2.split(" ")
    
# for each test cases
for i in range(T):
    # get z, number of points Naomi will score if she plays War optimally
    z = war(N[i], Naomi[i], Ken[i])
    # get y, number of points Naomi will score if she plays Deceitful War optimally
    y = deceitfulWar(N[i], Naomi[i], Ken[i])
    # print output
    print "Case #" + str(i + 1) + ": " + str(y) + " " + str(z)