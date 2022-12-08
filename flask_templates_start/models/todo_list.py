from models.task import *



task1 = Task("Buy groceries", "Milk, Cheese, Pizza, Fruit", False)
task2 = Task("Learn Python", "Learn an awesome new programming language", True)
tasks = [task1, task2]

def add_task(new_task):
    inputted_task = Task(new_task)
    tasks.append(inputted_task)