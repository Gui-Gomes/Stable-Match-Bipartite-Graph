class Project:
    # Constructor to initialize a Project object.
    def __init__(self, project_id, number_of_vacancies, minimum_grade_requirement):
        self.__id = project_id
        self.__number_of_vacancies = number_of_vacancies
        self.__minimum_grade_requirement = minimum_grade_requirement
        self.__total_participants = 0

    # Getter method to retrieve the project ID.
    @property
    def id(self):
        return self.__id
    
    # Setter method to set the project ID.
    @id.setter
    def id(self, value):
        self.__id = value

    # Getter method to retrieve the number of vacancies for the project.
    @property
    def number_of_vacancies(self):
        return self.__number_of_vacancies
    
    # Setter method to set the number of vacancies for the project.
    @number_of_vacancies.setter
    def number_of_vacancies(self, value):
        self.__number_of_vacancies = value

    # Getter method to retrieve the minimum grade requirement.
    @property
    def minimum_grade_requirement(self):
        return self.__minimum_grade_requirement
    
    # Setter method to set the minimum grade requirement.
    @minimum_grade_requirement.setter
    def minimum_grade_requirement(self, value):
        self.__minimum_grade_requirement = value

    # Getter method to retrieve the total number of participants.
    @property
    def total_participants(self):
        return self.__total_participants

    # Method to increment the total number of participants by 1.
    def increment_total_participants(self):
        self.__total_participants += 1

    # Method to decrement the total number of participants by 1, if greater than 0.
    def decrement_total_participants(self):
        if self.__total_participants > 0:
            self.__total_participants -= 1

    # Method to check if there are vacancies available for the project.
    def has_vacancies(self):
        return self.total_participants < self.number_of_vacancies
