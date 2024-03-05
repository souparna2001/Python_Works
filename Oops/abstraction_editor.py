from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class Vscode(Editor):

    def edit(self):
        print("editor edit")  

    def debug(self):
        print("editor debug")

    def execute(self):
        print("editor execute")

new=Vscode()
new.debug()              
new.edit()
new.execute()

