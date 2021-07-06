class Example:
    def a_normal_method(self, a, b):
        print(self, a, b)
    @classmethod
    def a_class_method(cls, a, b):
        print(cls, a, b)
    @staticmethod
    def a_static_method(a, b):
        print(a, b)


ex = Example()

ex.a_normal_method(1, 2)

ex.a_static_method(1, 2)

Example.a_class_method(1, 2)

Example.a_normal_method(1, 2)