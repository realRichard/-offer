import threading


class SingletonType(type):
    _instance_lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._instance_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class Myclass(metaclass=SingletonType):
    def __init__(self, value):
        self.value = value


def test():
    s1 = Myclass(1)
    s2 = Myclass(2)
    print(id(s1))
    print(id(s2))
    print(s1.value, s2.value)


if __name__ == '__main__':
    test()