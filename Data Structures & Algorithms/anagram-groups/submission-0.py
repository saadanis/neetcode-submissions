class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}

        for i, n in enumerate(strs):

            sn = ''.join(sorted(n))

            if sn in hashMap:
                hashMap[sn].append(n)
            else:
                hashMap[sn] = [n]
        
        return list(hashMap.values())
        
