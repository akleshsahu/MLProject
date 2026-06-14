from setuptools import setup, find_packages
from typing import List

# FIXED: Removed the leading space inside the string
HYPHEN_E = "-e ."

def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip newlines AND any accidental surrounding whitespace from the lines
        requirements = [req.replace("\n", "").strip() for req in requirements]
        
        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)
            
    return requirements

setup(
    name='MLFIRST',
    version='0.1.0',
    author='Aklesh Sahu',
    author_email="akleshsahu684@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('req.txt')        
)