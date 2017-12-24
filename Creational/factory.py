from abc import ABCMeta,abstractmethod

class Tech_member:
    """
    Abstract class for technical member
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_responsibility(self):
        raise NotImplementedError

class Developer(Tech_member):
    """
    Concrete class for Developer
    """
    def get_responsibility(self):
        print "Works on the infrastructure."


class Data_scientist(Tech_member):
    """
    Concrete class for Data scientist.
    """
    def get_responsibility(self):
        print "Plays with data."

class Tech_member_factory:
    """
    Factory class for instantiating Developer or Data Scientist based on runtime.
    """

    def get_member(self,type):
        if type=='developer':
            return Developer()
        elif type=='data_scientist':
            return Data_scientist()


if __name__ == '__main__':
    developer = Tech_member_factory().get_member('developer')
    data_scientist = Tech_member_factory().get_member('data_scientist')

    developer.get_responsibility()
    data_scientist.get_responsibility()
