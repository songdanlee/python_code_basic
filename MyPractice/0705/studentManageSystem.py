from operator import itemgetter

# 学号，姓名，性别，年龄，身高；
students = [{'id': '1001', 'name': '张三', 'age': 12, 'height': 189, 'sex': '男'},
            {'id': '1002', 'name': '李四', 'age': 19, 'height': 176, 'sex': '女'},
            {'id': '1003', 'name': '王武', 'age': 20, 'height': 176, 'sex': '女'}
            ]


def sortStu(students, ke="id", bo=False):
    students = sorted(students, key=itemgetter(ke), reverse=bo)
    print(students)


def WelPrint():
    print("*" * 50)
    print("欢迎进入学员管理系统".center(40))
    print("请输入指令\n查询学员信息:1\n增加学员信息:2\n删除学员信息:3\n修改学员信息:4\n排序:5\n退出:0")
    print("*" * 50)


def AddStudent():
    id = input("请输入新学员的ID\n")
    name = input("请输入新学员的姓名\n")
    age = int(input("请输入新学员的年龄(纯数字的整数)\n"))
    height = int(input("请输入新学员的身高(纯数字的整数)\n"))
    sex = input("请输入新学员的性别，男或女\n")
    if FindStudent(id) == 0:
        students.append(dict(id=id, name=name, age=age, height=height, sex=sex))
    else:
        print("该学号已被占用")


def FindStudent(id):
    for student in students:
        if student["id"] == id:
            print("学生信息如下", student)
            return 1
    return 0

for index, student in enumerate(students):
    if student.get("id", "-1") == id:
        print("index", index, "sut", student)
        students.remove(student)
        print("已经删除学员信息")


def FindAllStudent():
    for stu in students:
        print(stu)
    return students


def DelStudent():
    id = input("请输入要删除学员的学号")
    while True:
        for index, student in enumerate(students):
            if student.get("id","-1")==id:
                print("index", index,"sut",student)
                students.remove(student)
                print("已经删除学员信息")
                return 1
        else:
            id = input("删除失败,请重新输入学员学号")


def UpdateStudent(id):
    name = input("请输入修改学员的姓名\n")
    age = int(input("请输入修改学员的年龄(纯数字的整数)\n"))
    height = int(input("请输入修改学员的身高(纯数字的整数)\n"))
    sex = input("请输入修改学员的性别，男或女\n")
    stu = dict(id=id, name=name, age=age, height=height, sex=sex)
    print(stu)
    for index, student in enumerate(students):
        if student.get(id) == stu.get(id):
            students[index] = stu
            print("修改成功啦")


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
                ke = input("请输入排序规则,学号:id,姓名:name,性别:sex,年龄:age,身高:height,默认:0")
                bo = input("是否需要逆序,1:逆序,0：默认")
                if bo == '1':
                    bo = True
                else:
                    bo = False
                if ke == '0':
                    ke = 'id'
                sortStu(students, ke, bo)
        else:
            print("输入格式非法")


main()
