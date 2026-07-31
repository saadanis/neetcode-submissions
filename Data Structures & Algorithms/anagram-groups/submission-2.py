class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = defaultdict(list)
        for n in strs:
            count = [0] * 26
            for c in n:
                count[ord(c)-ord('a')] += 1
            hashTable[tuple(count)].append(n)
        return list(hashTable.values())