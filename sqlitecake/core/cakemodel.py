from .caketypes import CakeTypes


class CakeModel(object):
    def __init__(self):
        self.types = CakeTypes()
        super(CakeModel, self).__init__()