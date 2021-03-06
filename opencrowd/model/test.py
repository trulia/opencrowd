from opencrowd.classes.database import Database
from opencrowd.config.redis import DB_HOST, DB_PORT
import uuid

database = Database(DB_HOST, DB_PORT)


class A(object):
    def __init__(self):
        self.a = 'test'
        self.b = {}


class B(object):
    def __init__(self):
        self.b = 'b'
        self.id = uuid.uuid4()

    def b_func(self):
        print('a' + self.b)

A1 = A()
B1 = B()

A1.b[B1.id] = B1


database.set('delete', A1)
c = database.get('delete')
print(c.b[B1.id].b)
