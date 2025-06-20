"""
The setup.py file is an essential part of packaging and distribution python projects. It is used by setuptools to define 
the configuration of your project, such as its metadata, dependencies, and more.
"""
import os 
from setuptools import find_packages, setup
from typing import List

def get_requirements()-> List[str]:
    """
    This function will return the list of requirements 
    """
    requirement_list:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            ## Read lines from the file 
            lines = file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
                ## ignore -e. as well
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not find")

    return requirement_list

setup(

    name='NetworkSecurity',
    version='0.0.1',
    author='Mukesh',
    author_email='mks.mukesh1996@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
