class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in myMap:
                myMap[sorted_word] = []

            myMap[sorted_word].append(word)

        return list(myMap.values())
