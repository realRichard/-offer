# use decorator
def singleton(cls):
    _instance = {}

    def single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return single


@singleton
class Singleton(object):
    foo = 123

    def __init__(self, value):
        self.value = value 


def test():
    s2 = Singleton(2)
    s1 = Singleton(1)
    print(id(s1))
    print(id(s2))
    print(s1.value, s1.foo)
    print(s2.value, s2.foo)


if __name__ == '__main__':
    test()