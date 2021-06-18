"""
created by Nagaj at 18/06/2021
"""
from abc import ABC


class CRUDMixin(ABC):

    def __init__(self):
        self.objects = []

    def __getitem__(self, item):
        return self.objects[item]

    def __contains__(self, item):
        return item in self.objects

    def is_exist(self, obj):
        return obj in self.objects

    def add(self, obj):
        if not self.is_exist(obj):
            self.objects.append(obj)

    def remove(self, obj):
        if self.is_exist(obj):
            self.objects.remove(obj)

    def list(self):
        if self.objects:
            for obj in self.objects:
                print(obj)
        else:
            print("No Items Found")

    def first(self):
        if self.objects:
            return self.objects[0]

    def last(self):
        if self.objects:
            return self.objects[-1]


class Task:

    def __init__(self, title, about=None):
        self.title = title
        self.about = about

    def __repr__(self):
        return self.title


class Todo(CRUDMixin):

    def __init__(self, title, desc=None):
        super().__init__()
        self.title = title
        self.desc = desc
        self.tasks = self.objects

    def __repr__(self):
        return f"Todo(title={self.title}, des={self.desc})"


if __name__ == '__main__':
    todo = Todo("Study Flask", "you have to study flask micro framework")
    tasks = ["1-flask into", "2-install flask", "3-hello world in flask", "4-basic routes"]
    for tsk in tasks:
        todo.add(Task(tsk))
    todo.list()
    # ######### ######### ######### ######### ######### ########
    print("#" * 100)
    for task in todo:
        print(task)

    print("#" * 100)
    # ######### ######### ######### ######### ######### ########
    todo2 = Todo("Django")
    task1 = Task("1-install & config django")
    print(todo2)
    print(task1 in todo2)
    todo2.add(task1)
    for task in todo2:
        print(task)

    todo2.remove(task1)

    print(todo2.tasks)

    print(todo[-1])  # slicing on user defined obj
    print(todo.last())
    print(todo.first())
