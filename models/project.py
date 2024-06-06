class Project:
    # Constructor to initialize the Project object with ID, number of vacancies, and minimum grade requirement.
    def __init__(self, id, number_of_vacancies, minimum_grade_requirement_for_vacancies):
        self.__id = id
        self.__number_of_vacancies = number_of_vacancies
        self.__minimum_grade_requirement_for_vacancies = minimum_grade_requirement_for_vacancies

    # Getter method to get the project ID
    @property
    def id(self):
        return self.__id

    # Setter method to set the project ID
    @id.setter
    def id(self, id):
        self.__id = id

    # Getter method to get the number of vacancies for the project
    @property
    def number_of_vacancies(self):
        return self.__number_of_vacancies
    
    # Setter method to set the number of vacancies for the project
    @number_of_vacancies.setter
    def number_of_vacancies(self, number_of_vacancies):
        self.__number_of_vacancies = number_of_vacancies

    # Getter method to get the minimum grade requirement for the project vacancies
    @property
    def minimum_grade_requirement_for_vacancies(self):
        return self.__minimum_grade_requirement_for_vacancies
    
    # Setter method to set the minimum grade requirement for the project vacancies
    @minimum_grade_requirement_for_vacancies.setter
    def minimum_grade_requirement_for_vacancies(self, minimum_grade_requirement_for_vacancies):
        self.__minimum_grade_requirement_for_vacancies = minimum_grade_requirement_for_vacancies
