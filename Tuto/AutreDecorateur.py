#coding:utf-8
class player:
    def __init__(self,name):
        self._name = name
    @property
    def get_name(self):
        return self._name
    @property.setter
    def set_name(self,name):
        if len(name)<=25:
            self._name = name
        else:
            print("Dépassement de capacité")
    @property.deleter
    def del_name(self):
        pass

    @staticmethod
    def one_method():
        pass
    @classmethod
    def another_method():
        pass
    """name = property(get_name,set_name)
    name = property()
    name.setter(set_name)
    
    one_method = staticmethod(one_method)
    another_method = classmethod(another_method)
    """
