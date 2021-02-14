"""
Sample Input

6 
Sample Output

     #
    ##
   ###
  ####
 #####
######
"""


def staircase(n):
    for i in range(n):
        print((' ') * (n - (i + 1)) + ('#' * (i + 1)))


#staircase(1) # -> #
staircase(2) # ->  #\n##
staircase(3) # ->   #\n ##\n###
staircase(6)