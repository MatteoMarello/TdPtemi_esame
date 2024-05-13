from dataclasses import dataclass
from Classroom.ArtsMia.model.artObject import ArtObject
@dataclass
class Connessione:
    v1: ArtObject
    v2: ArtObject
    peso: int

    def __str__(self):
        return f'Arco: {self.v1.object_id} - {self.v2.object_id} - Peso: {self.peso}'