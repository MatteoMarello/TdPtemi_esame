from dataclasses import dataclass
from Classroom.FlightDelays.model.airport import Airport
@dataclass
class Connessione:
    v0: Airport
    v1: Airport
    N: int