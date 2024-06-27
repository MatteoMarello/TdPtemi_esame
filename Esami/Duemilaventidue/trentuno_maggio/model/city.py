from dataclasses import dataclass
@dataclass
class City:
    City: str
    latitude: float
    longitude: float

    def __hash__(self):
        return hash(self.City)

    def __str__(self):
        return f"{self.City}"