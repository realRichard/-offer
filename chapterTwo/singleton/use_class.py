import threading
import time 


# use class method, instance
class Singleton(object):
    _instance_lock = threading.Lock()
    
    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._instance_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = cls(*args, **kwargs)
        return cls._instance

    def __init__(self):
        time.sleep(1)

    @classmethod
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)


def task(args):
    obj = Singleton.instance()
    print(obj, id(obj))


def test():
    # 有限制， 调用的时候， 只能这样写
    # s1 = Singleton.instance(1)
    # s2 = Singleton.instance(2)
    # print(id(s1))
    # print(id(s2))
    # 一般情况，大家以为这样就完成了单例模式，
    # 但是这样当使用多线程时会存在问题

    for i in range(10):
        t = threading.Thread(target=task, args=[i,])
        t.start()
    # <__main__.Singleton object at 0x7fc37ade3610> 140477556733456
    # <__main__.Singleton object at 0x7fc37ade3610> 140477556733456
    # <__main__.Singleton object at 0x7fc37ade3610> 140477556733456
    # <__main__.Singleton object at 0x7fc37ade3610> 140477556733456
    # <__main__.Singleton object at 0x7fc37ade3610> 140477556733456
    # <__main__.Singleton object at 0x7fc37ade3610> 140477556733456
    # <__main__.Singleton object at 0x7fc37ade3610> 140477556733456
    # <__main__.Singleton object at 0x7fc37ade3610> 140477556733456
    # <__main__.Singleton object at 0x7fc37ade3610> 140477556733456
    # <__main__.Singleton object at 0x7fc37ade3610> 140477556733456
    # 看起来也没有问题，那是因为执行速度过快，
    # 如果在 init 方法中有一些 IO 操作，就会发现问题了，下面我们通过 time.sleep 模拟
    # <__main__.Singleton object at 0x7f222d5fda90> 139784766872208
    # <__main__.Singleton object at 0x7f222d5fdd10> 139784766872848
    # <__main__.Singleton object at 0x7f222d5fd6d0> 139784766871248
    # <__main__.Singleton object at 0x7f222d67c6d0> 139784767391440
    # <__main__.Singleton object at 0x7f222d5fd590> 139784766870928
    # <__main__.Singleton object at 0x7f222d5fd950> 139784766871888
    # <__main__.Singleton object at 0x7f222d5fdbd0> 139784766872528
    # <__main__.Singleton object at 0x7f222d5fd810> 139784766871568
    # <__main__.Singleton object at 0x7f222d5fde50> 139784766873168
    # <__main__.Singleton object at 0x7f222d5fdfd0> 139784766873552
    # 问题出现了！按照以上方式创建的单例，无法支持多线程

    # 解决办法：加锁！未加锁部分并发执行,
    # 加锁部分串行执行,速度降低,但是保证了数据安全
    # <__main__.Singleton object at 0x7fed2c4d7390> 140656627250064
    # <__main__.Singleton object at 0x7fed2c4d7390> 140656627250064
    # <__main__.Singleton object at 0x7fed2c4d7390> 140656627250064
    # <__main__.Singleton object at 0x7fed2c4d7390> 140656627250064
    # <__main__.Singleton object at 0x7fed2c4d7390> 140656627250064
    # <__main__.Singleton object at 0x7fed2c4d7390> 140656627250064
    # <__main__.Singleton object at 0x7fed2c4d7390> 140656627250064
    # <__main__.Singleton object at 0x7fed2c4d7390> 140656627250064
    # <__main__.Singleton object at 0x7fed2c4d7390> 140656627250064
    # <__main__.Singleton object at 0x7fed2c4d7390> 140656627250064
    time.sleep(5)
    obj = Singleton.instance()
    print(obj, id(obj))
    # 这样就差不多了，但是还是有一点小问题，
    # 就是当程序执行时，执行了time.sleep(5)后，下面实例化对象时，此时已经是单例模式了，
    # 但我们还是加了锁，这样不太好，再进行一些优化，把intance方法改一下
    # 这样，一个可以支持多线程的单例模式就完成了
    # 通过上面例子，我们可以知道，当我们实现单例时，为了保证线程安全需要在内部加入锁


if __name__ == '__main__':
    test()