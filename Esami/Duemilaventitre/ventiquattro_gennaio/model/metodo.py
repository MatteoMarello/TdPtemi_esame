from dataclasses import dataclass
@dataclass
class Metodo:
    Order_method_code: int
    Order_method_type: str


    def __hash__(self):
        return hash(self.Order_method_code)

    def __str__(self):
        return f"{self.Order_method_type}"