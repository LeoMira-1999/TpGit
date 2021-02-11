class Individu :
    """Class to create individuals"""

    def __init__(self,name, firstname,phone, adress, city):
        self.name = name
        self.firstname = firstname
        self.phone = phone
        self.adress = adress
        self.city = city

    def __str__(self):
        return self.name + self.firstname + self.phone + self.adress + self.city
