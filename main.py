from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        return "Abstract method implemented"

class AnotherConcreteClass(AbstractClass):
    def abstract_method(self):
        return "Another implementation of abstract method"

def main():
    concrete = ConcreteClass()
    another_concrete = AnotherConcreteClass()

    print(concrete.abstract_method())
    print(another_concrete.abstract_method())

if __name__ == "__main__":
    main()
```

```python
# AbstractClass.py
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

# ConcreteClass.py
from AbstractClass import AbstractClass

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        return "Abstract method implemented"

# AnotherConcreteClass.py
from AbstractClass import AbstractClass

class AnotherConcreteClass(AbstractClass):
    def abstract_method(self):
        return "Another implementation of abstract method"

# main.py
from ConcreteClass import ConcreteClass
from AnotherConcreteClass import AnotherConcreteClass

def main():
    concrete = ConcreteClass()
    another_concrete = AnotherConcreteClass()

    print(concrete.abstract_method())
    print(another_concrete.abstract_method())

if __name__ == "__main__":
    main()
