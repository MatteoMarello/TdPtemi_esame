from dataclasses import dataclass

@dataclass(frozen = True)
class Location:
    Location: str
    OBJECTID: int
    Latitude: float
    Longitude: float

    def __hash__(self):
        # Hash basato su identificativo univoco
        return hash(self.Location)

    def __str__(self):
        return f"{self.Location}"
