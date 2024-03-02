class Codec:
    def encode(self, strs: List[str]) -> str:
        return "\U0001f601".join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split("\U0001f601")
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))