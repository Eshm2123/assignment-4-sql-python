from DTO import *


class _Hats:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, hat):
        self._conn.execute("""
        INSERT INTO hats (id, topping, supplier, quantity) VALUES (?, ?, ?, ?)
        """, [hat[0], hat[1], hat[2], hat[3]])

    def find(self, hat_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM hats WHERE id = ?
            """, [hat_id])
        return Hat(*c.fetchone())

    def decrease_quantity(self, hat):
        c = self._conn.cursor()
        c.execute("""
               UPDATE hats SET quantity = ? WHERE id = ?
               """, [hat.quantity - 1, hat.id])

    def delete(self, hat):
        self._conn.execute("""
        DELETE FROM hats WHERE id = ?
        """, [hat.id])

    def find_first_supplier(self, topping):
        supplier = self._conn.execute("""SELECT * ,MIN(supplier) FROM hats WHERE topping = ?""", [topping])
        return Hat(*supplier.fetchall())


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                INSERT INTO suppliers (id, name) VALUES (?, ?)
                """, [int(supplier[0]), supplier[1]])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
                    SELECT * FROM suppliers WHERE id = ?
                    """, [supplier_id])
        return Supplier([*c.fetchone()])


class _Orders:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, order):
        self._conn.execute("""
                   INSERT INTO orders (id, location, hat) VALUES (?, ?, ?)
                   """, [order[0], order[1], order[2]])

    def find(self, order_id):
        c = self._conn.cursor()
        c.execute("""
                       SELECT * FROM orders WHERE id = ?
                       """, [order_id])
        return Order(*c.fetchone())
