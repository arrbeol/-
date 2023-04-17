import time
list1 = []
def menu():
    print('欢迎您使用大berman学生管理系统V100')
    print('-1 添加学生')
    print('-2修改学生信息')
    print('-3删除学生信息')
    print('-4查看学生信息')
    print('-5查询学生信息')
    print('-6退出大berman学生管理系统V100')
# menu()
def add():
    print('欢迎进入学生添加界面')
    name = (input('请输入学生姓名'))
    age = int(input('请输入学生年龄'))
    gender = (input('请输出学生性别'))
    for i in list1:
        if i['name'] == name and i['age'] == age and i['gender'] == gender:
            print('该学生的信息已存在')
        dict1 = {}
        dict1['name'] = name
        dict1['age'] = age
        dict1['gender'] = gender
        list1.append(dict1)
        print(list1)
        print('添加成功')
# add()
def delete():
    print('欢迎进入学生信息删除界面')
    num = int(input('请输入您所要删除的学生序号'))
    if 0 <= num <= len(list1)-1:
        delete_num = input('确定删除yes/no')
        if delete_num == 'yes':
            del list1[num]
            print('删除成功')
        elif delete_num == 'no':
            print('取消删除')
        else:
            print('输入错误，请重新输入')
# delete()
def all():
    print('欢迎来到学生信息展示功能页面')
    for i, j in enumerate(list1):
        print('序号%d, 姓名%s, 年龄%d, 性别%s' % (i, j['name'], j['age'], j['gender']))
# all()

def change():
    print('欢迎来到学生修改功能页面')
    all()
    print('以上是所有学生的信息')
    num = int(input('请输入所要修改的学生序号'))
    if 0 <= num <= len(list1)-1:
        list1[num]['name'] = input('请输入您所要修改的姓名')
        list1[num]['age'] = input('请输入您所要修改的的年龄')
        list1[num]['gender'] = input('请输入您所要修改的性别')
        print("修改成功")
        print(list1[num])
    else:
        print('请输入正确的学生序号')
# change()

def search():
    print('欢迎进入学生信息查找界面')
    name = input('请输入所要查找的学生姓名')
    for name in list1:
        if list1[name] == name:
            print('该学生存在')
        else:
            print('该学生不存在')
# search()
def main():
    while True:
        menu()
        num = int(input('请输入您所要使用的功能'))
        if num == 1:
            add()
        elif num == 2:
            change()
        elif num == 3:
            delete()
        elif num == 4:
            all()
        elif num == 5:
            search()
        elif num == 6:
            break
        """else:
            print('hhhh')"""
if __name__ == '__main__':
    main()

