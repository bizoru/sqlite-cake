from sqlitecake.core import CakeModel
from sqlitecake.core import CakeSync


class Client(CakeModel):

    def __init__(self):
        super(Client, self).__init__()
        self.nombre = self.types.TextType
        self.edad = self.types.IntegerType




