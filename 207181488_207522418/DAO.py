from DTO import Hat


class _Hats:
    def __init__(self,conn):
        self._conn=conn

    def insert(self,hat):
        self._conn.execute("""
        INSERT INTO hats (id,topping,supplier,quantity) VALUES (?,?,?,?)
        """,[hat.id,hat.topping,hat.supplier,hat.quantity])

    def find(self,hat_id):
        c=self._conn.cursor()
        c.execute("""
        SELECT id,topping,supplier,quantity FROM hats WHERE id=? 
        """,[hat_id])
        return Hat(*c.fetchone())

    def findToppingSupplier(self,hat_topping):
        c=self._conn.cursor()
        c.execute("""
        SELECT supplier FROM hats WHERE topping=? ORDER BY supplier
        """,[hat_topping])
        return c.fetchall()

    def findToppingId(self, hat_topping):
        c = self._conn.cursor()
        c.execute("""
           SELECT id FROM hats WHERE topping=? ORDER BY supplier
           """, [hat_topping])
        return c.fetchone()

    def findQuantity(self, id):
        c = self._conn.cursor()
        c.execute("""
                 SELECT quantity FROM hats WHERE id=? 
                 """, [id])
        return c.fetchone()

    def update(self, id, quantity):
        self._conn.execute("""UPDATE hats SET quantity=(?) WHERE id=(?)""", [quantity, id])

    def delete(self, id):
        self._conn.execute("""DELETE FROM hats WHERE id=(?)""", [id])

class _Suppliers:
    def __init__(self,conn):
        self._conn=conn

    def insert(self,suppliers):
        self._conn.execute("""
                INSERT INTO suppliers VALUES (?,?)
                """, [suppliers.id,suppliers.name])

    def find(self, supplier_id):
            c = self._conn.cursor()
            c.execute("""
                SELECT name FROM suppliers WHERE id=? 
                """, [supplier_id])
            return c.fetchone()

class _Orders:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, orders):
        self._conn.execute("""
                   INSERT INTO orders VALUES (?,?,?)
                   """, [orders.id, orders.location,orders.hatid])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
                   SELECT name FROM suppliers WHERE id=? 
                   """, [supplier_id])
        return c.fetchone()
