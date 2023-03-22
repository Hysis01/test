class Car:
    def __init__(self, clas_, mark, year_of_issue):
        # self.__clas_
        self.__description_clas(clas_)
        self.__mark = mark
        self.__year = year_of_issue

    def get_class(self):
        return self.__clas_

    def __description_clas(self, clas_):
        if clas_ == 'A':
            clas_ += ' = motorbike'
            self.__clas_ = clas_
        elif clas_ == 'B':
            clas_ += ' = passenger'
            self.__clas_ = clas_


a = Car('A', 'qqq', 1990)
b = Car('B', 'sdf', 123)
print(a.get_class())
print(b.get_class())
