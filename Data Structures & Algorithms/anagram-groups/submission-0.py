class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        
        for n in strs :
            val = "".join(sorted(n))

            anagram.setdefault(val,[])

            anagram[val].append(n)

        return list(anagram.values())
