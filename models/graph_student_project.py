import networkx as nx
import matplotlib.pyplot as plt
from .student import Student
from .project import Project


class Graph:
    # Constructor to initialize a Graph object
    def __init__(self):
        self.__graph = nx.Graph()  # Initialize an empty undirected graph using NetworkX
        self.__students = {}  # Dictionary to store students
        self.__projects = {}  # Dictionary to store projects

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
    def add_project(
        self, id, number_of_vacancies, minimum_grade_requirement_for_vacancies
    ):
        if id in self.projects:
            raise ValueError(f"Project with ID '{id}' already exists in the graph.")
        self.projects[id] = Project(
            id, number_of_vacancies, minimum_grade_requirement_for_vacancies
        )
        self.graph.add_node(id, bipartite=1)  # Add project node to the graph

    # Method to apply the Gale-Shapley algorithm to match students with projects.
    def gale_shapley(self, max_iterations=10):
        for i in range(max_iterations):
            print(f"ITERATION {i + 1}:")
            changes_made = (
                False  # Flag to check if any changes were made in this iteration
            )
            free_students = []

            # Collect students who are not currently matched
            for student_id in self.students:
                if self.graph.degree(student_id) == 0:
                    free_students.append(student_id)

            while free_students:
                student_id = free_students.pop(0)
                student = self.students[student_id]
                projects_preferences = student.preferential_projects

                matched = False

                for project_id in projects_preferences:
                    if project_id != "":
                        project = self.projects[project_id]

                    if project.minimum_grade_requirement <= student.grade:
                        if project.has_vacancies():
                            project.increment_total_participants()
                            self.graph.add_edge(student_id, project_id)
                            changes_made = True
                            matched = True
                            break
                        else:
                            # Find the student with the lowest grade currently matched to the project
                            lowest_grade_student_id = None
                            lowest_grade = float("inf")

                            for neighbor in list(self.graph.neighbors(project_id)):
                                if self.students[neighbor].grade < lowest_grade:
                                    lowest_grade = self.students[neighbor].grade
                                    lowest_grade_student_id = neighbor

                            # If the current student has a higher grade than the lowest grade student, replace them
                            if student.grade > lowest_grade:
                                self.graph.remove_edge(
                                    lowest_grade_student_id, project_id
                                )
                                free_students.append(lowest_grade_student_id)
                                self.graph.add_edge(student_id, project_id)
                                changes_made = True
                                matched = True
                                break

                if not matched:
                    # If student couldn't be matched with any project, remove all its edges in the graph
                    if student_id in self.graph:
                        for neighbor in list(self.graph.neighbors(student_id)):
                            self.graph.remove_edge(student_id, neighbor)
                        changes_made = True

            # Print the current state of the edges after each iteration
            self.print_edges()

            print(f"Number of edges: {nx.number_of_edges(self.graph)} \n")

            if not changes_made:
                print("No changes made in this iteration, stopping early.")
                break

    # Method to print the current edges in the graph
    def print_edges(self):
        print("Current edges in the graph:")
        for student_id, project_id in self.graph.edges():
            student = self.students.get(student_id)
            project = self.projects.get(project_id)
            if student and project:
                print(f"Student {student_id} is matched with Project {project_id}")
        print("\n")

    # Method to generate an image of the bipartite graph with increased spacing between vertices
    def plot_bipartite_graph(self, file_path, file_name="bipartite_graph.png"):
        plt.figure(figsize=(19.20, 10.80))  # Set the figure size for Full HD resolution

        # Separate student nodes and project nodes
        student_nodes = [
            n for n, d in self.graph.nodes(data=True) if d["bipartite"] == 0
        ]
        project_nodes = [
            n for n, d in self.graph.nodes(data=True) if d["bipartite"] == 1
        ]

        # Define positions for the nodes with increased spacing
        pos = nx.drawing.layout.bipartite_layout(
            self.graph, student_nodes, align="vertical", aspect_ratio=5
        )

        # Draw the nodes and edges
        nx.draw_networkx_nodes(
            self.graph,
            pos,
            nodelist=student_nodes,
            node_color="lightblue",
            node_size=1,
            label="Students",
        )
        nx.draw_networkx_nodes(
            self.graph,
            pos,
            nodelist=project_nodes,
            node_color="lightgreen",
            node_size=50,
            label="Projects",
        )
        nx.draw_networkx_edges(self.graph, pos, edge_color="lightgray")
        nx.draw_networkx_labels(self.graph, pos, font_size=3.5, font_color="black")

        # Add legend and title
        plt.legend(loc="best")
        plt.title("Bipartite Graph of Students and Projects")

        # Save the image to a file in the specified directory
        plt.savefig(file_path + file_name, dpi=700)  # Set dpi to adjust resolution
        plt.close()
