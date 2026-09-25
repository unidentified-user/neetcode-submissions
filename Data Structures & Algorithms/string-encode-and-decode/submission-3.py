class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for s in strs:
            output += f'{len(s)}#{s}'
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        start, end, pos, step = 0, 0, 0, 0
        while pos < len(s):
            if s[pos] == '#':
                step = int(s[end:pos])
                start = pos + 1
                end = start + step
                output.append(s[start:end])
                pos = end
            pos += 1
        return output