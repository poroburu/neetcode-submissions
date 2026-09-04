class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += f"{len(s)}#{s}"
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            start = j + 1
            end =  start + length
            result.append(s[start:end])
            i = end 
        return result
