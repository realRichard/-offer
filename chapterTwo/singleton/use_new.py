# use __new__
# 我们知道，当我们实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__），实例化对象；
# 然后再执行类的__init__方法，对这个对象进行初始化，所有我们可以基于这个，实现单例模式
class Singleton(object):
    _instance = None

    @classmethod
    # __new__ method must receive args, otherwise
    # TypeError: __new__() takes 1 positional argument but 2 were given
    # do not understand
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


def test():
    s1 = Singleton(1)
    s2 = Singleton(2)
    print(id(s1))
    print(id(s2))


if __name__ == '__main__':
    test()