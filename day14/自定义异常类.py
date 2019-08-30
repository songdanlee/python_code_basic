
class ArgumentsError(Exception):
    def __init__(self):
        self.errMasg = "参数错误"
    def __str__(self):
        return f"{self.__class__},{self.errMasg}"


def add(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a + b
    raise ArgumentsError()

val = add(10,20)
print(val)
add(10,"as")