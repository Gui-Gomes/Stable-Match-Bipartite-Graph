import networkx as nx
from .student import Student
from .project import Project

class Graph:
    # Constructor to initialize a Graph object
    def __init__(self):
        self.__graph = nx.Graph()  # Initialize an empty undirected graph using NetworkX
        self.__students = {}       # Dictionary to store students
        self.__projects = {}       # Dictionary to store projects

    # Getter method to retrieve the graph object.
    @property
    def graph(self):
        return self.__graph
    
    # Setter method to set the graph object.
    @graph.setter
    def graph(self, graph):
        self.__graph = graph

    # Getter method to retrieve the students dictionary.
    @property
    def students(self):
        return self.__students
    
    # Setter method to set the students dictionary.
    @students.setter
    def students(self, students):
        self.__students = students

    # Getter method to retrieve the projects dictionary.
    @property
    def projects(self):
        return self.__projects
    
    # Setter method to set the projects dictionary.
    @projects.setter
    def projects(self, projects):
        self.__projects = projects

    # Method to add a student to the graph.
    def add_student(self, id, preferential_projects, grade):
        if id in self.students:
            raise ValueError(f"Student with ID '{id}' already exists in the graph.")
        
        self.students[id] = Student(id, preferential_projects, grade)
        self.graph.add_node(id, bipartite=0)  # Add student node to the graph
    
    # Method to add a project to the graph.
    def add_project(self, id, number_of_vacancies, minimum_grade_requirement_for_vacancies):
        if id in self.projects:
            raise ValueError(f"Project with ID '{id}' already exists in the graph.")
        
        self.projects[id] = Project(id, number_of_vacancies, minimum_grade_requirement_for_vacancies)
        self.graph.add_node(id, bipartite=1)  # Add project node to the graph

    # Method to apply the Gale-Shapley algorithm to match students with projects.
    def gale_shapley(self):
        free_students = list(self.students.keys())

        # Sorting students by grade (highest to lowest)
        free_students.sort(key=lambda student_id: self.students[student_id].grade, reverse=True)

        while free_students:
            student_id = free_students.pop(0)
            student = self.students[student_id]
            projects_preferences = student.preferential_projects

            matched = False  # Flag to indicate if the student has been matched

            for project_id in projects_preferences:
                project = self.projects[project_id]

                if project.minimum_grade_requirement <= student.grade and project.has_vacancies():
                    # Project has a vacancy and student meets grade requirement
                    project.increment_total_participants()
                    self.graph.add_edge(student_id, project_id)  # Create an edge in the graph
                    matched = True
                    break  # Student is matched, move to next free student

            if not matched:
                # If student couldn't be matched with any project, remove all its edges in the graph
                if student_id in self.graph:
                    for neighbor in list(self.graph.neighbors(student_id)):
                        self.graph.remove_edge(student_id, neighbor)

    # Method to print edges representing student-project preferences.
    def print_edges(self):
        for student_id, project_id in self.graph.edges():
            student = self.students.get(student_id)
            project = self.projects.get(project_id)
            if student and project:
                print(f"Student {student_id} prefers Project {project_id}")