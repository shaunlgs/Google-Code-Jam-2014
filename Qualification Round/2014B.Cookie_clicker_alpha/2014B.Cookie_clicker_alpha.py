
"""
C: cost to buy cookie farm
rate: current cookies per second
F: extra number cookies per second after buying cookie farm
X: number of cookies to win
Return true if it is faster to achieve X by buying, false otherwise.
"""
def buy(n, C, rate, F, X):
    # time required to achieve X if buy
    buying = X / (rate + F)
    # time required to achieve X if no buy
    noBuying = (X - C) / rate
    if buying < noBuying:
        return True
    else:
        return False
        
"""
C: cost to buy cookie farm
F: extra number cookies per second after buying cookie farm
X: number of cookies to win
"""

# get number of test cases, T
T = int(raw_input())

# initialize list C, F, X
C = [0.000000000 for i in range(T)]
F = [0.000000000 for i in range(T)]
X = [0.000000000 for i in range(T)]

# for each test case
for i in range(T):
    # get C, F, X
    string = raw_input();
    C[i] = float(string.split()[0])
    F[i] = float(string.split()[1])
    X[i] = float(string.split()[2])

# for each test case
for i in range(T):
    # initialize rate = 2.0 cookies per second, current number of cookie, n and time, t
    rate = float(2.000000000)
    n = float(0.000000000)
    time = float(0.000000000)
    # while number of cookie is less than X
    while n < X[i]:
        # if the number of cookie reached more than C
        if n >= C[i]:
            # if decide to buy
            if buy(n, C[i], rate, F[i], X[i]):
                n = float(n - C[i])
                rate += F[i]
        # when n is approaching the C[i]  (adding rate will make n more than c[i])
        if n < C[i]:
            if C[i] - n < rate:
                time += (C[i] - n) / rate
                n = float(C[i])
            else:
                time += float(1.0)
                n += rate
        # else continue 1 second
        else:
            time += float(1.0)
            n += rate
            
    # After the while loop breaks, if n is more than x, adjust for excess time spent
    time -= (n - X[i]) / rate
    print "Case #" + str(i + 1) + ": " + str(time)