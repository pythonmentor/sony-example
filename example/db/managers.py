from .database import db 

from .models import Product, Category, Store

class ProductManager:
    
    def __init__(self):
        self.table_name = "product"
        self.model = Product
        cursor = db.cursor()
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(200) NOT NULL,
                nutriscore VARCHAR(1) NOT NULL,
                url VARCHAR(255) NOT NULL
            )
            """
        )
        cursor.close()

    def get_all(self):
        cursor = db.cursor()
        cursor.execute(
            f"""
            SELECT id, name, nutriscore, url FROM {self.table_name}
            """
        )
        collection = cursor.fetchall()
        cursor.close()
        return [self.model(*data) for data in collection]

    def get_by_id(self, id):
        cursor = db.cursor()
        cursor.execute(
            f"""
            SELECT id, name, nutriscore, url 
            FROM {self.table_name}
            WHERE id = %(product_id)s
            """,
            {"product_id": id}
        )
        product = cursor.fetchone()
        cursor.close()
        return self.model(*product)

class ProductCategoryManager:
    
    def __init__(self):
        self.table_name = "product_category"
        cursor = db.cursor()
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                product_id INT NOT NULL,
                category_id INT NOT NULL,
                PRIMARY KEY (product_id, category_id),
                FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE,
                FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE
            )
            """
        )
        cursor.close()

    def get_all(self):
        cursor = db.cursor()
        cursor.execute(
            f"""
            SELECT product_id, category_id FROM {self.table_name}
            """
        )
        collection = cursor.fetchall()
        cursor.close()
        return collection

class CategoryManager:

    def __init__(self):
        self.table_name = "category"
        self.model = Category
        cursor = db.cursor()
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL UNIQUE
            )
            """
        )
        cursor.close()

    def get_all(self):
        cursor = db.cursor()

        cursor.execute(
            f"""
            SELECT id, name FROM {self.table_name}
            """
        )

        collection = cursor.fetchall()
        cursor.close()
        return [self.model(*data) for data in collection]


class ProductStoreManager:
    
    def __init__(self):
        self.table_name = "product_store"
        cursor = db.cursor()
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                product_id INT NOT NULL,
                store_id INT NOT NULL,
                PRIMARY KEY (product_id, store_id),
                FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE,
                FOREIGN KEY (store_id) REFERENCES store(id) ON DELETE CASCADE
            )
            """
        )
        cursor.close()

    def get_all(self):
        cursor = db.cursor()
        cursor.execute(
            f"""
            SELECT product_id, category_id FROM {self.table_name}
            """
        )
        collection = cursor.fetchall()
        cursor.close()
        return collection

class StoreManager:

    def __init__(self):
        self.table_name = "store"
        cursor = db.cursor()
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL UNIQUE
            )
            """
        )
        cursor.close()

    def get_all(self):
        cursor = db.cursor()

        cursor.execute(
            f"""
            SELECT id, name FROM {self.table_name}
            """
        )

        collection = cursor.fetchall()
        cursor.close()
        return [self.model(*data) for data in collection]

class FavoriteManager:
    
    def __init__(self):
        self.table_store = "favorite"
        cursor = db.cursor()
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INT PRIMARY KEY AUTO_INCREMENT,
                product_id INT NOT NULL,
                substitute_id INT NOT NULL,
                FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE,
                FOREIGN KEY (substitute_id) REFERENCES product(id) ON DELETE CASCADE
            )
            """
        )
        cursor.close()

    def get_all(self):
        cursor = db.cursor()

        cursor.execute(
            f"""
            SELECT id, product_id, substitute_id FROM {self.table_name}
            """
        )

        collection = cursor.fetchall()
        cursor.close()
        favorites = []
        for data in collection:
            id, product_id, substitute_id = data
            product = product_manager.get_by_id(product_id)
            substitute = product_manager.get_by_id(substitute_id)
            favorites.append((id, product, substitute))
        return [self.model(*data) for data in favorites]

# Instantiation unique des managers
product_manager = ProductManager()
category_manager = CategoryManager()
store_manager = StoreManager()
_product_category_manager = ProductCategoryManager()
_product_store_manager = ProductStoreManager()
favorite_manager = FavoriteManager()