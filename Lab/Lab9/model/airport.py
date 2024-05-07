from dataclasses import dataclass
@dataclass
class Airport:
    id: int
    iata_code: str
    airport: str
    city: str
    state: str
    country: str
    latitude: float
    longitude: float
    timezone_offset: float

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f'{self.id} - {self.airport}'
