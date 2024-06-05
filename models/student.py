class Student:
    # Constructor to initialize the Student object with id, preferential projects, and grade
    def __init__(self, id, preferential_projects, grade):
        self._id = id
        self._preferential_projects = preferential_projects
        self._grade = grade

    # Getter method for id
    @property
    def id(self):
        return self._id
    
    # Setter method for id
    @id.setter
    def id(self, id):
        self._id = id

    # Getter method for preferential projects
    @property
    def preferential_projects(self):
        return self._preferential_projects
    
    # Setter method for preferential projects
    @preferential_projects.setter
    def preferential_projects(self, preferential_projects):
        self._preferential_projects = preferential_projects

    # Getter method for grade
    @property
    def grade(self):
        return self._grade
    
    # Setter method for grade
    @grade.setter
    def grade(self, grade):
        self._grade = grade
