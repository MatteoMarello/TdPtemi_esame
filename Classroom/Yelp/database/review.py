from dataclasses import dataclass
from datetime import date
from Classroom.Yelp.database.business import Business

@dataclass
class Review:
    review_id: str
    stars: float
    review_date: date
    votes_funny: int
    votes_useful: int
    votes_cool: int
    review_text: str

    business_id: str
    # Per rappresentare la relazione tra Review e Business, dato che una Review corrisponde a UNA sola Business, posso
    # utilizzare sia il metodo scritto sopra, usando il business_id come attributo, altrimenti posso usare direttamente
    # l'oggetto Business come attributo!
    business: Business

    def __eq__(self, other):
        return self.review_id == other.review_id

    def __hash__(self):
        return hash(self.review_id)