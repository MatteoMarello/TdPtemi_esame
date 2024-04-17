from Lab.Lab6.database.DAO import DAO
class Model:
    def __init__(self):
        pass

    def getYears(self):
        return DAO.getYears()

    def getBrands(self):
        return DAO.getBrands()

    def getRetailers(self):
        return DAO.getRetailers()

    def getTopVendite(self, anno, brand, codice_retailer):
        return DAO.getTopVendite(anno, brand, codice_retailer)

    def getAnalisiVendite(self, anno, brand, codice_retailer):
        return DAO.getAnalisiVendite(anno,brand,codice_retailer)
