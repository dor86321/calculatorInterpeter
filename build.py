import os

# Define the directory structure in a dictionary format
project_structure = {
    "calculator_interpreter": {
        "interpreter": ["__init__.py", "calculator.py", "parser.py"],
        "tests": ["__init__.py", "test_calculator.py"],
        "utils": ["__init__.py", "constants.py"],
        "main.py": None
    }
}

def create_project_structure(base_path, structure):
    """ Recursively create directory structure with files. """
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # Create a directory
            os.makedirs(path, exist_ok=True)
            # Recursive call to create files/subdirectories within
            create_project_structure(path, content)
        elif isinstance(content, list):
            # Create a directory
            os.makedirs(path, exist_ok=True)
            # Create files in this directory
            for file_name in content:
                with open(os.path.join(path, file_name), 'w') as f:
                    f.write('# Write your Python code here\n')
        elif content is None:
            # Create a file directly under the base path
            with open(path, 'w') as f:
                f.write('# Write your Python code here\n')

# Usage
base_path = os.getcwd()  # Or any path where the project should be created
create_project_structure(base_path, project_structure)
