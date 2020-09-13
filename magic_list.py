
class Person:
    age: int = 1


class MagicList(list):
    def __init__(self, cls_type=None):
        super().__init__()
        if cls_type:
            self.my_list = [cls_type()]
        else:
            self.my_list = []
        self.index = 0

    # @classmethod
    # def from_cls(cls_type):
    #     instance = cls_type()

    def __getitem__(self, index):
        return self.my_list[index]
        # return list.__getitem__(self, index)

    def __setitem__(self, index, value):
        if index > self.index+1:
            raise ValueError
        self.index += 1
        if isinstance(value, int):
            return self.my_list.insert(index, value)
        else:
            return self.my_list.insert(index, value)
        # return list.__setitem__(self, index, value)

    def __delitem__(self, index):
        del self.my_list[index]
        # self.my_list.pop(index)
        # return list.__delitem__(self, index)

    def __str__(self):
        return str(self.my_list)

    def __repr__(self):
        return f'[Person(age={str(self.my_list)})]'




if __name__ == '__main__':
    a = MagicList()
    a[0] = 5
    print(a)
    print(a.__repr__())

    b = MagicList(cls_type=Person)
    b[0].age = 5
    print(b.__repr__())




