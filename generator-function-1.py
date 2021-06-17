lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]


def my_enumerate(iterable, start=0):
    return [(start + i, lessons[i]) for i in range(len(lessons))]


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))