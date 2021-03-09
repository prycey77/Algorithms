"""
You are given a text represented as a string t, and a string s of 
length 3. Your task is to count the number of indices i, such that 
titi+2ti+4 = s.
Example
For t = "azcabcab" and s = "acb", the output should be 
almostSubstring(t, s) = 2.
t0t2t4 = "acb" = s;
t1t3t5 = "zac" ≠ s;
t2t4t6 = "cba" ≠ s;
t3t5t7 = "acb" = s.
For t = "" and s = "xyz", the output should be 
almostSubstring(t, s) = 0.
"""

def almostSubstring(t,s):
    count = 0
    if len(t) > 4:
        max = len(t) - 4
    else:
        return 0
    for i in range(max):
        sub_string = "".join([t[i], t[i+2], t[i+4]])
        if sub_string == s:
            count += 1
    return count

print(almostSubstring("azcabcabkkjkjacb", "acb"))
print(almostSubstring("aaaaaaaaaaaa", "aaa"))
