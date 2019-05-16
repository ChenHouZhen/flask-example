
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        print("---------------------- 调用 __str__ 方法 ----------------------")
        return "name:{},age:{},gender:{}".format(self.name, self.age, self.gender)

    def __eq__(self, other) -> bool:
        print("---------------------- 调用 __eq__ 方法 ----------------------")
        return (self.name == other.name) and (self.age == other.age) and (self.gender == other.gender)


if __name__ == '__main__':
    p = Person('张三', 12, '男')
    p2 = Person('张三', 12, '男')
    print('打印 ==> ', p)
    print('对等 ==> ', p == p2)