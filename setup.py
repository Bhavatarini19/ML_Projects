# This will be responsible for creating this Machine Learning application as a package. 
# We can directly insall this setup.py or whenever the requirements.txt is run this can be build by mentioning "-e ." in requirements.txt

from typing import List
from setuptools import find_packages, setup 

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    This function will return a list of requiremenets 
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = 'FirstEndToEndMLProject',
    version = '0.0.1',
    author = 'Bhavatarini',
    author_email= 'bhavatarinithangaraju@gmail.com',
    packages= find_packages(), #it will check for the folders with __init__.py and consider them as a package and it tries to build it, after that we can import it anywhere
    #install_requires = ['pandas', 'numpy', 'seaborn']
    install_requires = get_requirements('requirements.txt')
)


