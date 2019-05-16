def myLog(func):
    def wrapper(*args, **kw):
        # 装饰器，在这里增加更多的功能
        print("-------------- 新增功能，打印日志 --------------")
        return func(*args, **kw)
    return wrapper


def myLog2(msg):
    def decorator(func):
        def wrapper(*args, **kw):
            print("-------------- 新增功能，打印日志 --------------")
            print("-------------- 传入参数：{} ".format(msg))
            return func(*args, **kw)
        return wrapper
    return decorator

@myLog
def inFun():
    print("----------- 内部方法 --------------")

@myLog2('小明')
def in2Fun():
    print("----------- 内部方法2 --------------")


if __name__ == '__main__':
    # f = myLog(inFun)
    # f()
    inFun()
    in2Fun()