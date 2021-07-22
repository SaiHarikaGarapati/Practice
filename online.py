def online_status(**ps):
    count = 0
    for i, j in ps.items():
        if j == "online":
            count = count+1
    print(count)


online_status(Alice="online", Bob="offline", Eve="offline")
