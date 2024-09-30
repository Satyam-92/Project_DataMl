from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT_ = "-e ."  # Define your marker here

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from a requirements file.
    It removes any newline characters and a specific marker if present.
    """
    requirements = []
    
    # Open the file and read lines
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
    
    # Strip newline characters and any leading/trailing whitespace
    requirements = [req.strip() for req in requirements]

    # Remove the specific marker if present
    if HYPEN_E_DOT_ in requirements:
        requirements.remove(HYPEN_E_DOT_)
    
    return requirements

# Package setup
setup(
    name='PROJECT_DATAML',
    version='0.0.1',
    author='Satyam',
    author_email='Satyamrajam03@gmail.com',
    packages=find_packages(),  # Automatically find packages
    install_requires=get_requirements('requirements.txt')  # Read requirements from file
)
