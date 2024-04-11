from dataclasses import dataclass

from review import Review


@dataclass
class Business:
    business_id: str
    full_address: str
    active: str
    categories: str
    city: str
    review_count: int
    business_name: str
    neighborhoods: str
    latitude: float
    longitude: float
    state: str
    stars: float

    # Dato che a una Business possono corrispondere diverse Review, per rappresentare la relazione fra le due classi
    # non potrò utilizzare Review come attributo di Business, ma dovrò utilizzare una COLLEZIONE di Review. In questo caso
    # ho deciso di utilizzare una lista di Review. Altrimenti, potrei anche utilizzare una lista di stringhe, dove
    # ciascuna stringa rappresenta l'ID della Review. Questa cosa si può fare perchè l'IDReview è chiave primaria di Review!
    reviews_id: list[str]
    reviews: list[Review] = None

    def __eq__(self, other):
        return self.business_id == other.business_id

    def __hash__(self):
        return hash(self.business_id)

    def get_reviews(self):
        if self.reviews is None:
            # vado a leggerle dal DAO e popolo la lista
            pass
        else:
            return self.reviews
