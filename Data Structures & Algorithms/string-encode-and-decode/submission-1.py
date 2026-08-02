class Solution:

    def encode(self, strs: List[str]) -> str:
        ec = ''
        for s in strs:
            ec += str(len(s)) + '#' + s
        return ec

    def decode(self, s: str) -> List[str]:
        
        dc = []
        i = 0
        num = ''

        while i < len(s):
            if s[i] == '#':
                n = int(num)
                num = ''
                dc.append(s[i + 1 : i + n + 1])
                i = i + n + 1
            else:
                num += s[i]
                i += 1
        
        return dc
            




