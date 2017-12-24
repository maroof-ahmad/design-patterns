from abc import ABCMeta,abstractmethod

class Product_manager:
    """
    Abstract class for product manager
    """
    @abstractmethod
    def get_description(self):
        raise NotImplementedError

class Product_team:
    """
    Abstract class for the product team
    """

    @abstractmethod
    def get_description(self):
        raise NotImplementedError

class Aadi_product_manager(Product_manager):
    """
    Concrete class for Aadi Product Manager
    """
    def get_description(self):
        print "I'm aadi product manager"

class Aadi_product_team(Product_team):
    """
    Concrete class for Aadi Product team
    """

    def get_description(self):
        print "We're aadi developer team"

class Drishti_product_manager(Product_manager):
    """
    Concrete class for drishti product Manager
    """
    def get_description(self):
        print "I'm drishti product manager"

class Drishti_product_team(Product_team):
    """
    Concrete class for drishti product Product_team
    """
    def get_description(self):
        print "We're drishti developer team"

class ProductFactory:
    """
    Abstract class for product factory
    """
    @abstractmethod
    def create_product_manager(self):
        raise NotImplementedError

    @abstractmethod
    def create_product_team(self):
        raise NotImplementedError

class Aadi_product_factory(ProductFactory):
    """
    Concrete class for aadi product Factory
    """
    def create_product_manager(self):
        return Aadi_product_manager()

    def create_product_team(self):
        return Aadi_product_team()

class Drishti_product_factory(ProductFactory):
    """
    Concrete class for drishti product Factory
    """
    def create_product_manager(self):
        return Drishti_product_manager()

    def create_product_team(self):
        return Drishti_product_team()


class Product_factory_maker:
    """
    Concrete class for product factory Product_factory_maker
    """
    @staticmethod
    def make_factory(type):
        if type=='aadi':
            return Aadi_product_factory()
        elif type=='drishti':
            return Drishti_product_factory()


class Product_creator:
    """
    Concrete class for product creator
    """
    @staticmethod
    def create_product(factory):
        manager = factory.create_product_manager()
        team = factory.create_product_team()
        return manager,team


if __name__ == '__main__':
    aadi_factory = Product_factory_maker.make_factory('aadi')
    drsihti_factory = Product_factory_maker.make_factory('drishti')

    aadi_manager,aadi_team = Product_creator.create_product(aadi_factory)
    drishti_manager,drishti_team = Product_creator.create_product(drsihti_factory)

    aadi_manager.get_description()
    aadi_team.get_description()

    drishti_manager.get_description()
    drishti_team.get_description()
