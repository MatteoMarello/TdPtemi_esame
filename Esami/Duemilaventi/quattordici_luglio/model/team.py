from dataclasses import dataclass

@dataclass
class Team:
    TeamID: id
    Name: str

    def __hash__(self):
        return hash(self.TeamID)

    def __str__(self):
        return f"{self.Name}"

    def __eq__(self, other):
        if isinstance(other, Team):
            return self.TeamID == other.TeamID
        return False
