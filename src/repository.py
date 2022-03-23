import atexit
import sqlite3
import sys
from DAO import _Hats, _Orders, _Suppliers


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect(sys.argv[4])
        self.hats = _Hats(self._conn)
        self.suppliers = _Suppliers(self._conn)
        self.orders = _Orders(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE hats (
            id           INTEGER     PRIMARY KEY,
            topping      STRING      NOT NULL,
            supplier     INTEGER     NOT NULL,
            quantity     INTEGER     NOT NULL,
            FOREIGN KEY(supplier)    REFERENCES suppliers(id)
        );
            
        CREATE TABLE suppliers (
            id         INTEGER      PRIMARY KEY,
            name       STRING         NOT NULL
        );
            
        CREATE TABLE orders (
            id         INTEGER      PRIMARY KEY,
            location   STRING       NOT NULL,
            hat        INTEGER      NOT NULL,
            FOREIGN KEY(hat)        REFERENCES hats(id)
        );
    """)

    def execute_order(self, order):
        hat = self.hats.find_first_supplier(order[2])
        self.hats.decrease_quantity(hat)
        ans = [order[2], self.suppliers.find(hat.supplier).name, order[1]]
        order[2] = hat.id
        if hat.quantity-1 == 0:
            self.hats.delete(hat)
        return ans


repo = _Repository()
atexit.register(repo._close)
