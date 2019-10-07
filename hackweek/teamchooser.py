import random
def teamgen():
    n = int(input("Enter the total number of players: "))
    m = int(input("Enter the number of players in a team: "))
    b = []
    temp = []
    final_teams = []
    teams = []
    flag = 0
    for i in range(1,n+1):
        b.append(i) #b contains a list of all players
    print(b)
    temp = b.copy()
    while True:
            if(len(temp)<m):
                final_teams.append(temp)
                #print(f"Temp {temp}")
                break
            if(flag<=m-1):
                randp = random.randint(1,n)
                if(randp in temp):
                    temp.remove(randp)
                    teams.append(randp)
                    flag += 1
                    """print(f"rANDOM NUMBER {randp}")
                    print(f"Temp {temp}")
                    print(f"Teams {teams}")
                    print(f"Flag {flag}")"""
                    continue
                elif(randp not in temp):
                    continue
            elif(flag == m):
                final_teams.append(teams)
                flag = 0
                teams = []
                continue
            else:
                print("Error")
                print(final_teams) #lines for debugging
                print(flag)
                print(teams)
                print(temp)
                break

    print(f"Final teams are {final_teams}")
    #print(temp)