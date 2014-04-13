# get number of test cases, T
T = int(raw_input())

# initialize list to store row number of the chosen card in the first arrangement
q = [0 for i in range(T)]

# initialize list to store row number of the chosen card in the second arrangement
r = [0 for i in range(T)]

# initialize list to store the four rows of the first arrangement
s = [["" for i in range(4)] for i in range(T)]

# initialize list to store the four rows of the second arrangement
t = [["" for i in range(4)] for i in range(T)]

# for each test case
for i in range(T):
    # get the row number, q of the chosen card in the first arrangement
    q[i] = int(raw_input())
    # get four rows of the first arrangement
    for j in range(4):
        s[i][j] = raw_input()
    # get the row number, r of the chosen card in the second arrangement
    r[i] = int(raw_input())
    # get four rows of the second arrangement
    for j in range(4):
        t[i][j] = raw_input()
            
# for each test cases
for i in range(T):
    # test1 is a list of elements in row number, q of first arrangement
    test1 = s[i][q[i] - 1].split()
    # test2 is a list of elements in row number, r of second arrangement
    test2 = t[i][r[i] - 1].split()
    
    # matches is a list of matches between lists test1 and test2
    matches = []
    for l in test1:
        for m in test2:
            if l == m:
                matches.append(l)
    
    # if the number of matches in test1 and test2 is 1
    if len(matches) == 1:
        # get the number that is matched
        print "Case #" + str(i + 1) + ": " + matches[0]
    # else if the number of matches is more than 1
    elif len(matches) > 1:
        # user is a bad magician
        print "Case #" + str(i + 1) + ": " + "Bad magician!"
    # else if there is no matches
    elif len(matches) == 0:
        # user cheated
        print "Case #" + str(i + 1) + ": " + "Volunteer cheated!"
    
