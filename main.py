from utilities.file_handler import *
from utilities.path_handler import *
from models.graph_student_project import Graph

def main():
    try:
        # Get the csv database directory path
        csv_database_dir = get_csv_directory()

        # Generate CSV files from text files in the database directory
        generate_csv_from_txt(get_first_txt_file_path_from_database(), csv_database_dir)

        # Import students and projects data from CSV files
        students_data = import_data_from_csv(csv_database_dir + "students.csv")
        projects_data = import_data_from_csv(csv_database_dir + "projects.csv")

        # Create an instance of the Graph class
        graph = Graph()

        # Add students to the graph
        for student_record in students_data:
            student_id = student_record[0]
            preferences = student_record[1:4]
            current_project = student_record[4]
            graph.add_student(student_id, preferences, current_project)

        # Add projects to the graph
        for project_record in projects_data:
            project_id = project_record[0]
            project_capacity = project_record[1]
            project_preferences = project_record[2]
            graph.add_project(project_id, project_capacity, project_preferences)

        # Perform Gale-Shapley algorithm to match students with projects
        graph.gale_shapley()

        # Print the edges of the graph (matches between students and projects)
        graph.print_edges()

        # Get the images database directory path
        images_database_dir = get_images_directory()

        # Plot the bipartite graph representing students and projects
        graph.plot_bipartite_graph(images_database_dir)

    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
