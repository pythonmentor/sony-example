"""Ajouter une docstring ici."""


class Product:
    """ajouter une docstring ici."""
    
    def __init__(self, id=None, name=None, nutriscore=None, url=None, stores=None, categories=None):
        """Ajouter une docstring ici."""
        self.id = id,
        self.name = name
        self.nutriscore = nutriscore
        self.url = url
        self.stores = stores
        self.categories = categories

class Category:
    
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

class Store:
    
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

class Favorite:
    
    def __init__(self, id=None, product, substitute):
        self.id = id
        self.product = product
        self.substitute = substitute