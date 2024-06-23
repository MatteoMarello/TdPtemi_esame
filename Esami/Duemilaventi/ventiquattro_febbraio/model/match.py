from dataclasses import dataclass

@dataclass
class Match:
    id: int
    TeamHomeName: str
    TeamHomeID: int
    TeamAwayName: str
    TeamAwayID: int

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"[{self.id}] {self.TeamHomeName} vs. {self.TeamAwayName}"