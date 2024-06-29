import datetime
from dataclasses import dataclass

@dataclass
class Player:
    playerID: str
    birthCountry: str
    birthCity: str
    deathCountry: str
    deathCity: str
    nameFirst: str
    nameLast: str
    weight: int
    height:int
    bats: str
    throws: str
    birth_date: datetime.date
    debut_date: datetime.date
    finalgame_date: datetime.date
    death_date: datetime.date
    salary: int

    def __hash__(self):
        return hash(self.playerID)

    def __str__(self):
        return f"{self.nameFirst} {self.nameLast}"