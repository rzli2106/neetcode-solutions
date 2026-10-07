class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        myMap1, myMap2 = {}, {}
        for i in range(len(s)):
            key = s[i]
            if key in myMap1:
                myMap1[key] += 1
            else:
                myMap1[key] = 1
        for i in range(len(t)):
            key = t[i]
            if key in myMap2:
                myMap2[key] += 1
            else:
                myMap2[key] = 1
        for key in myMap1:
            if myMap1[key] != myMap2.get(key, 0):
                return False
        return True