from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT="-e ."

def get_requirements(file_path:str)->   List[str]:
    '''
        This function returns all the requirements in a List[str] form and triggers setup.py at last
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[r.replace("\n","") for r in requirements]
        
        if(HYPHEN_E_DOT in requirements):
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author='Shubham',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)