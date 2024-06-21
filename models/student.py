class Student:
    # Constructor to initialize the Student object with id, preferential projects, and grade
    def __init__(self, id, preferential_projects, grade):
        self.__id = id
        self.__preferential_projects = preferential_projects
        self.__grade = grade

    # Getter method for id
    @property
    def id(self):
        return self.__id

    # Setter method for id
    @id.setter
    def id(self, id):
        self.__id = id

    # Getter method for preferential projects
    @property
    def preferential_projects(self):
        return self.__preferential_projects

    # Setter method for preferential projects
    @preferential_projects.setter
    def preferential_projects(self, preferential_projects):
        self.__preferential_projects = preferential_projects

    # Getter method for grade
    @property
    def grade(self):
        return self.__grade

    # Setter method for grade
    @grade.setter
    def grade(self, grade):
        self.__grade = grade
