# Агрегация полезна, когда один объект использует другой объект, но
# при этом оба объекта могут существовать независимо друг от друга.
# Это облегчает повторное использование объектов в других частях
# программы и снижает зависимость между классами.

# Задание 1: Команда разработчиков и задачи

class Developer:
    def __init__(self, name:str):
        self.name = name 
    
    
            
class Project:
    def __init__(self, project_name):
        self.project_name = project_name
        self.developers:list = []
        self.all_dev :dict = {}
      
       
    def add_developer(self, developer: Developer):
        self.developers.append(developer)
        # print(f"{developer.name} добавлена в {self.project_name}!")
       
        
    def assign_task(self, name: str, task: str):
        # Find the developer by name
        for developer in self.developers:
            if developer.name == name:
                self.all_dev[developer.name] = task
                # print(f"For {developer.name} assigned task '{task}'")
                return
        
    
    def get_project_info(self):
        for name, task in self.all_dev.items():
                print(f"{name} has task: {task}")
            
            
project = Project("Новый проект")
dev1 = Developer("Alice")
dev2 = Developer("Bob")

project.add_developer(dev1)
project.add_developer(dev2)


project.assign_task("Alice", "Fix bug #101")
project.assign_task("Bob", "Implement feature X")


project.get_project_info()