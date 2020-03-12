import os
from setuptools import find_packages
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_requirements(req_file):
    """Read requirements file and return packages and git repos separately"""
    requirements = []
    dependency_links = []
    lines = read(req_file).split("\n")
    for line in lines:
        if line.startswith("git+"):
            dependency_links.append(line)
        else:
            requirements.append(line)
    return requirements, dependency_links

#read the required files
#get the requirements from text file "requirements.txt"