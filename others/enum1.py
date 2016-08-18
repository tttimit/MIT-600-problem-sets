#枚举类
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', \
                       'Sep', 'Oct', 'Nov', 'Dec'))

##for name, member in Month.__members__.items():
##    print(name, '=>', member, ',', member.value)

from enum import Enum, unique
@unique # @unique装饰器用来检查没有重复值
class Weekday(Enum):
    sun = 0 # 默认的值是从1开始赋值的，因此我们自定义一个enum来从0赋值
    Mon = 1
    Tue = 2
    Wed = 3
    Tur = 4
    Fri = 5
    Sat = 6

#以下代码打印值均为 Weekday.Mon， 这个成员的值我们前面赋值为1
print(Weekday.Mon)
print(Weekday['Mon'])
print(Weekday(1))



    
