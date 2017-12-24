from abc import ABCMeta,abstractmethod

class Aadi:

    def __init__(self,builder):
        self.manager=builder.manager
        self.data_scientist=builder.data_scientist
        self.AI_engineer=builder.AI_engineer
    def get_manager(self):
        return self.manager
    def get_data_scientist(self):
        return self.data_scientist
    def get_ai_engineer(self):
        return self.AI_engineer

class Aadi_builder:

    def __init__(self):
        pass

    def add_manager(self,name):
        self.manager=name
        return self

    def add_data_scientist(self,name):
        self.data_scientist=name
        return self

    def add_ai_engineer(self,name):
        self.AI_engineer=name
        return self

    def build(self):
        return Aadi(self)



if __name__ == '__main__':
    aadi = Aadi_builder().add_manager('apurv').add_data_scientist('karan').add_ai_engineer('maroof').build()
    print aadi.get_manager()
    print aadi.get_data_scientist()
    print aadi.get_ai_engineer()
