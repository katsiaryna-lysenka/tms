class Parent1:
    person = "Parent1"


class Parent2:
    person = "Parent2"


class Parent3:
    person = "Parent3"


class MyClass(Parent1, Parent2, Parent3):
    def __init__(self):
        self.person = "MyClass"
        self.attributes = {}

    def __getitem__(self, key):
        return self.attributes[key]

    def __setitem__(self, key, value):
        self.attributes[key] = value

    def get_attribute(self, attr_name):
        if attr_name in self.attributes:
            print(f"Attribute {attr_name} found in Instance: {self}")
            return self.attributes[attr_name]
        elif hasattr(self.__class__, attr_name):
            print(f"Attribute {attr_name} found in Instance Class: {self.__class__.__name__}")
            return getattr(self.__class__, attr_name)
        else:
            for parent in self.__class__.__bases__:
                if hasattr(parent, attr_name):
                    print(f"Attribute {attr_name} found in Instance Parent Class: {parent.__name__}")
                    return getattr(parent, attr_name)
            raise AttributeError(f"{attr_name} not found")


my_object = MyClass()
print(getattr(my_object, "person"))
delattr(my_object, "person")
print(getattr(my_object, "person"))
