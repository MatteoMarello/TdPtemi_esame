from dataclasses import dataclass
@dataclass
class NTA:
    NTACode: str
    nSSID: int

    def __hash__(self):
        return hash(self.NTACode)

    def __str__(self):
        return f"{self.NTACode}"
