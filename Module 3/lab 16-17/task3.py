import sys, os
from abc import ABC, abstractmethod, ABCMeta
BASE_DIR = os.path.dirname(__file__)
file_path= os.path.join(BASE_DIR,"input.txt")
class Subject(metaclass=ABCMeta):
    def __init__(self):
        self._observers = []
    def register_observer(self, observer):
        self._observers.append(observer)
    def notify_observers(self, data):
        for observer in self._observers:
            observer.onDataRecive(data)

class FileReader(Subject):
    def __init__(self, file_name):
        super().__init__()
        self._file_name= "input.txt"
    def read_file(self):
        with open(file_path, "r" , encoding="utf-8") as file:
            for line in file:
                self.notify_observers(line.strip())

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def onDataRecive(self, data):
        pass

class FilePrinter(Observer):
    def onDataRecive(self, data):
        print("FilePrinter received data:")
        print(data)

class WordCounter(Observer):
    def onDataRecive(self, data):
        word_count = len(data.split())
        print(f"WordCounter: The file contains {word_count} words.")

filereader= FileReader("input.txt")
fileprinter= FilePrinter()
wordcounter= WordCounter()
filereader.register_observer(fileprinter)
filereader.read_file()
filereader.register_observer(wordcounter)
print(wordcounter)