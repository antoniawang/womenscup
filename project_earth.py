# Problem Statement

# Project Earth, California's biggest environmental organization, is working to protect the planet Earth from global warming. 
#Dr. Ritika is a scientist at Project Earth. 
#She created a chemical called K29 which can increase the absorption rate of carbon dioxide by plants and help reduce global warming.

# Unfortunately, K29 is not reacting the way it should.
#Dr. Ritika noticed that when K29 is used in plants, the reaction time is exactly T seconds. 
#However, the chemical's reaction time changes as time passes, by following a specific pattern. 
#It will change by 1 second every two hours, alternately increasing or decreasing every two hours.
#For the first two hours, the reaction time DECREASES by 1 second. During the next two hours, the reaction time INCREASES by 2 seconds. 
#Then, for the next two hours, the reaction time DECREASES by 3 seconds. 
#The reaction time follows this pattern by incremental seconds until the Nth hour.

# Dr. Ritika needs the final reaction time in the Nth hour to correct K29. 
#As her assistant, you must help Dr. Ritika correct the error so that she can save planet Earth. 
# Given the value of N and an initial reaction time, T, find the final reaction time after N hours.

# Enter your code here. Read input from STDIN. Print output to STDOUT
def project_earth(n, t):
    if n%4 == 0:
        delta = (n/2) 
    elif n%4 == 1:
        delta = (- 1)
    elif n%4 == 2:
        delta = (-n/2 - 1)
    else:
        delta = 0
    if int(t + delta) < 0:
        return 0
    else:
        return int(t + delta)
    
S = raw_input().split()
N = int(S[0])
T = int(S[1])
print project_earth(N, T)