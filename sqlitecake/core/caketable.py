from .caketypes import CakeTypes


class CakeTable(object):

    def __init__(self, model):
        super(CakeTable, self).__init__()
        self.model = model
        self.properties = {}

    def create_table(self):
        pass

    def disect_model(self):

        table_name = self.model.__class__.__name__
        self.properties[table_name] = {}
        for key in self.model.__dict__.keys():
            if not isinstance(self.model.__dict__[key], CakeTypes):
                # print "Key:" + key + " Value: " + self.model.__dict__[key]
                self.properties[table_name][key] = self.model.__dict__[key]
        print self.properties

