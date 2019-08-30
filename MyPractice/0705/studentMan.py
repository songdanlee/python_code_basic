
# 学号，姓名，性别，年龄，身高；
students = {'1002': {'name': '张三', 'age': 12, 'height': 189, 'sex': '男'},
            '1001': {'name': '李四', 'age': 19, 'height': 176, 'sex': '女'},
            '1003': {'name': '王武', 'age': 20, 'height': 176, 'sex': '女'}
            }

def sortStu(students):
    students = sorted(students.items(), key=lambda x: x[0])
    print(students)


def WelPrint():
    print("*" * 50)
    print("欢迎进入学员管理系统".center(40))
    print("请输入指令\n查询学员信息:1\n增加学员信息:2\n删除学员信息:3\n修改学员信息:4\n排序:5\n退出:0")
    print("*" * 50)


def UpdateStudent(id):
    name = input("请输入学员的姓名\n")
    age = int(input("请输入学员的年龄(纯数字的整数)\n"))
    height = int(input("请输入学员的身高(纯数字的整数)\n"))
    sex = input("请输入学员的性别，男或女\n")
    stu = dict(name=name, age=age, height=height, sex=sex)
    students[id] = stu


def AddStudent():
    id = input("请输入新学员的ID\n")
    UpdateStudent(id)


def FindStudent(id):
    if students.get(id, "-1") != "-1":
        return (1, students.get(id))
    return 0


def FindAllStudent():
    for k, stu in students.items():
        print(k, stu)
    return students


def DelStudent():
    id = input("请输入要删除学员的学号")
    while True:
        if FindStudent(id) != 0:
            return students.pop(id)
        id = input("删除失败,请重新输入学员学号")


def main():
    while True:
        WelPrint()
        num = input().strip()
        if num.isdigit():
            if int(num) == 0:
                break
            elif int(num) == 1:
                choose = input("请输入查看方式，1：查看所有学员,2:查看单个学员")
                if choose == '1':
                    FindAllStudent()
                elif choose == '2':
                    id = input("请输入要查询的学号")
                    if FindStudent(id) == 0:
                        print("你要找的学员貌似不存在呀，请核实后操作")
                    else:
                        _, stu = FindStudent(id)
                        print(stu)
            elif int(num) == 2:
                AddStudent()
            elif int(num) == 3:
                DelStudent()
            elif int(num) == 4:
                id = input("请输入修改学员的ID\n")
                if FindStudent(id) == 0:
                    print("查无此人，你修改个什么呀")
                else:
                    UpdateStudent(id)
            elif int(num) == 5:
                sortStu(students)
        else:
            print("输入格式非法")


main()
