import os
import re
import csv


# Generate CSV files from a TXT file containing project and student data.
def generate_csv_from_txt(file_path, output_dir):
    # Define paths for CSV output files
    projects_csv = os.path.join(output_dir, "projects.csv")
    students_csv = os.path.join(output_dir, "students.csv")

    # Write projects.csv
    with open(projects_csv, mode="w", newline="") as projects_file:
        projects_writer = csv.writer(projects_file)
        # Write header row
        projects_writer.writerow(
            ["Project_Code", "Number_of_Vacancies", "Minimum_Grade"]
        )

        with open(file_path, "r") as file:
            for line in file:
                if line.startswith("(P"):
                    # Using regex to extract values between parentheses and converting to integers
                    match = re.match(r"\(P(\d+), (\d+), (\d+)\)", line)
                    if match:
                        project_values = [
                            "P" + match.group(1),
                            match.group(2),
                            match.group(3),
                        ]
                        projects_writer.writerow(project_values)

    # Write students.csv
    with open(students_csv, mode="w", newline="") as students_file:
        students_writer = csv.writer(students_file)
        # Write header row
        students_writer.writerow(
            [
                "Student_ID",
                "Preferred_Project_1",
                "Preferred_Project_2",
                "Preferred_Project_3",
                "Grade",
            ]
        )

        with open(file_path, "r") as file:
            for line in file:
                if line.startswith("(A"):
                    # Using regex to extract relevant parts and converting to integers
                    match = re.match(r"\((A\d+)\):\(([^)]+)\) \((\d+)\)", line)
                    if match:
                        id_part = match.group(1)
                        # Extract preferred projects and fill with empty string if less than 3 preferred projects found
                        preferred_projects = [
                            f"P{x}" for x in re.findall(r"(\d+)", match.group(2))[:3]
                        ]
                        preferred_projects += [""] * (3 - len(preferred_projects))
                        grade = match.group(3)
                        students_writer.writerow(
                            [id_part] + preferred_projects + [grade]
                        )


# Function to import data from a CSV file
def import_data_from_csv(file_path):
    with open(file_path, "r") as file:
        # Skip the header row
        next(file)
        data_list = []
        for line in file:
            clean_line = line.strip()
            data_row = clean_line.split(",")
            # Convert numeric values to integers if possible
            data_row = [int(item) if item.isdigit() else item for item in data_row]
            data_list.append(data_row)
        return data_list
